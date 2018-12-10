from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from posts.settings import POSTS_LIST_TEMPLATE, POSTS_LIST_URL, section_templates


class Section(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    namespace = models.CharField(_("Namespace"), blank=True, null=True, max_length=255)
    template = models.CharField(_("Template"), max_length=255, default=POSTS_LIST_TEMPLATE, choices=section_templates)

    # Audit
    created = models.DateTimeField(_("Created"), auto_now_add=True, null=True)
    updated = models.DateTimeField(_("Edited"), auto_now=True)

    typo3_uid = models.IntegerField(null=True)
    typo3_pid = models.IntegerField(null=True)

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('%s:%s' % (self.namespace, POSTS_LIST_URL))

    def latest_posts(self):
        from posts.models.post_model import Post
        return Post.objects.filter(section=self, published=True).order_by('-date')[:6]

    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Section")
