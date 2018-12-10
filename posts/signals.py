from cms.api import create_page, create_title
from cms.constants import TEMPLATE_INHERITANCE_MAGIC
from django.db import IntegrityError
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.html import strip_tags
from django.utils.text import slugify
from djangocms_text_ckeditor.models import Text

from ida.settings import LANGUAGE_CODE, LANGUAGES
from posts.cms_apps import PostApp
from posts.models import Section, Post
from posts.utils import get_translation_fields_per_language


@receiver(post_save, sender=Section)
def create_section_page(sender, instance, created, raw, using, update_fields, **kwargs):

    if not instance.slug:
        instance.slug = slugify(instance.name)

    if created:
        if instance.namespace == "" or not instance.namespace:
            instance.namespace = slugify(instance.name)

        if instance.create_page:

            page = create_page(
                title=instance.name,
                template=TEMPLATE_INHERITANCE_MAGIC,
                language=LANGUAGE_CODE,
                slug=instance.slug,
                apphook=PostApp,
                apphook_namespace=instance.namespace,
                published=True,
                in_navigation=True
            )

            for code, lang in LANGUAGES:

                if code != LANGUAGE_CODE:
                    title = getattr(instance, "name_%s" % code, instance.name)
                    slug = getattr(instance, "slug_%s" % code, instance.slug)

                    try:
                        create_title(
                            language=code,
                            title=title,
                            page=page,
                            slug=slug
                        )
                    except IntegrityError:
                        pass

        instance.save()


@receiver(pre_save, sender=Post)
def update_summary_fields(sender, instance, *args, **kwargs):
    translated_fields = get_translation_fields_per_language("content", "summary", None)

    for field in translated_fields:
        references = getattr(instance, field["from_field"], False)

        if references:
            references_list = references.cmsplugin_set.all()
            texts_model = Text.objects.filter(cmsplugin_ptr__in=references_list)

            if texts_model:
                texts_body = [text.body for text in texts_model]
                text = ' '.join(texts_body)

                clean_text = strip_tags(text).replace('&shy;', '')
                setattr(instance, field["to_field"], clean_text)
