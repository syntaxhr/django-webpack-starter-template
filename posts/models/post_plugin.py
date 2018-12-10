from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from posts.models import Section, Category


class PostsPlugin(CMSPlugin):
    section = models.ForeignKey(
        Section,
        default="",
        on_delete=models.SET_DEFAULT,
        related_name="plugin_section",
        verbose_name=_("Section")
    )
    categories = models.ManyToManyField(
        Category,
        related_name="plugin_categories",
        verbose_name=_("Category"),
        blank=True
    )
    count = models.PositiveSmallIntegerField(_('Number of posts'), default=6)

    def __str__(self):
        return self.section.name

    def copy_relations(self, old_instance):
        self.categories = old_instance.categories.all()

    class Meta:
        verbose_name = _("Posts plugin")
        verbose_name_plural = _("Posts plugins")
