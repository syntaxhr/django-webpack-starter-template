from django.utils.translation import ugettext_lazy as _
from django.db import models

from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField

from commons.settings import cms_plugin_text_image_alignement


class WidgetPlugin(CMSPlugin):
    title = models.CharField(_("Title"), max_length=255, blank=True, null=True)
    subtitle = models.CharField(_("Subtitle"), max_length=255, blank=True, null=True)
    image = FilerImageField(verbose_name=_("Image"), blank=True, null=True)
    content = models.TextField(_("Content"), blank=True, null=True)
    content_html = HTMLField(_("Content"), blank=True, null=True)
    link = models.CharField(_("Link"), blank=True, null=True, max_length=255)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    def __str__(self):
        return "%s" % self.title if self.title else "%s" % _("CMS Widget")

    class Meta:
        verbose_name = _("Widget plugin")
        verbose_name_plural = _("Widget plugins")


class Settings(models.Model):
    address = models.CharField(_('Address'), max_length=255, blank=True, null=True)
    mobile = models.CharField(_('Mobile (call)'), max_length=255, blank=True, null=True)
    mobile_display = models.CharField(_('Mobile (display on site)'), max_length=255, blank=True, null=True)
    phone = models.CharField(_('Phone (call)'), max_length=255, blank=True, null=True)
    phone_display = models.CharField(_('Phone (display on site)'), max_length=255, blank=True, null=True)
    fax = models.CharField(_('Fax'), max_length=255, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=255, blank=True, null=True)
    share_image = FilerImageField(verbose_name=_("Share image"), blank=True, null=True)
    facebook = models.CharField(
        'Facebook',
        max_length=255,
        help_text=_('Link na službenu Facebook stranicu'),
        blank=True,
        null=True
    )
    twitter = models.CharField(
        'Twitter',
        max_length=255,
        help_text=_('Link na službeni Twitter profil'),
        blank=True,
        null=True
    )
    instagram = models.CharField(
        'Instagram',
        max_length=255,
        help_text=_('Link na službeni Instagram profil'),
        blank=True,
        null=True
    )
    youtube = models.CharField(
        'Youtube',
        max_length=255,
        help_text=_('Link na službeni Youtube profil'),
        blank=True,
        null=True
    )

    def __str__(self):
        return '%s' % _('Settings')

    @property
    def cms_edit_text(self):
        return _('Edit information')

    class Meta:
        verbose_name = _('Settings')
        verbose_name_plural = _('Settings')

