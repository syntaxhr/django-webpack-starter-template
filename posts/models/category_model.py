from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from posts.models import Section
from posts.settings import POSTS_LIST_BY_CATEGORY_TEMPLATE, POSTS_CATEGORY_DETAIL_URL, category_templates


def get_now():
    return timezone.now()


class Category(models.Model):
    section = models.ForeignKey(
        Section,
        blank=True,
        null=True,
        default="",
        on_delete=models.SET_NULL,
        related_name="categories",
        verbose_name=_("Section")
    )
    name = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255)
    template = models.CharField(_("Template"), max_length=255, default=POSTS_LIST_BY_CATEGORY_TEMPLATE, choices=category_templates)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True, null=True)
    updated = models.DateTimeField(_("Edited"), auto_now=True)
    typo3_id = models.IntegerField(_("Typo 3 id"), null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.section.name, self.name)

    def get_absolute_url(self):
        return reverse('%s:%s' % (self.section.namespace, POSTS_CATEGORY_DETAIL_URL), args=[self.id, self.slug])

    class Meta:
        ordering = ("order",)
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
