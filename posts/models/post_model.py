from cms.models import PlaceholderField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.files import get_thumbnailer

from posts.models import Section, Category
from posts.settings import POST_DETAIL_TEMPLATE, post_templates, POST_DETAIL_URL


def get_now():
    return timezone.now()


class Post(models.Model):
    section = models.ForeignKey(
        Section,
        default=None,
        on_delete=models.SET_DEFAULT,
        related_name="posts",
        verbose_name=_("Section")
    )
    categories = models.ManyToManyField(Category, related_name="posts", verbose_name=_("Category"), blank=True)
    title = models.CharField(_("Title"), default="", max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    image = PlaceholderField(slotname='post_image', related_name='featured_image')
    author = models.CharField(_("Author"), default="", max_length=255, blank=True)
    date = models.DateTimeField(_("Publish date"), default=get_now)
    summary = models.TextField(_("Summary"), blank=True, null=True)
    content = PlaceholderField(slotname='post_content')
    published = models.BooleanField(_("Published"), default=False)
    template = models.CharField(_("Template"), max_length=255, default=POST_DETAIL_TEMPLATE, choices=post_templates)
    created = models.DateTimeField(_("Created"), auto_now_add=True, null=True)
    updated = models.DateTimeField(_("Edited"), auto_now=True)
    typo3_uid = models.IntegerField(_("Typo3 ID", ), null=True)
    typo3_pid = models.CharField(_("Typo3 Related", ), null=True, max_length=255)

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('%s:%s' % (self.section.namespace, POST_DETAIL_URL), args=[self.id, self.slug])

    def get_formatted_date(self):
        return self.date.strftime('%d.%m.%Y.')

    @property
    def cms_edit_text(self):
        return _('Edit information')

    class Meta:
        ordering = ("-date",)
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
