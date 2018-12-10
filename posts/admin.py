from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from cms.admin.placeholderadmin import PlaceholderAdminMixin, FrontendEditableAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from commons.utils import duplicate_records
from posts.models import Post, Category, Section, Gallery



class GalleryAdminInline(admin.TabularInline):
    model = Gallery
    extra = 0


@admin.register(Section)
class SectionAdmin(TranslationAdmin):
    list_display = ('name', 'namespace',)
    exclude = ('namespace',)
    prepopulated_fields = {'slug': ('name',)}

    def get_form(self, request, obj=None, **kwargs):
        if hasattr(obj, "pk"):
            self.exclude = ('create_page',)
        else:
            pass

        form = super(SectionAdmin, self).get_form(request, obj, **kwargs)
        return form


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, TranslationAdmin):
    list_display = ('name', 'section',)
    list_filter = ('section',)
    exclude = ('typo3_id',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin, TranslationAdmin):
    # inlines = [GalleryAdminInline,]
    filter_horizontal = ['categories',]
    list_display = ('title', 'section', 'author', 'date', 'published', 'show_detail_url',)
    list_editable = ('published',)
    list_filter = ('published', 'section')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'
    actions = [duplicate_records,]
    view_on_site = True

    fieldsets = [
        (_('Published'), {
            'fields': (('published',),)
        }),
        (_('Post info'), {
            'fields': ('section', 'title', 'slug', 'author', 'date')
        }),
        (_('Category'), {
            # 'classes': ('collapse',),
            'fields': ('categories',)
        })

    ]

    def show_detail_url(self, obj):
        # If saved from frontend for some reason cannot resolve 'post_detail' url
        try:
            url = obj.get_absolute_url()
        except:
            url = "#"

        return format_html('<a href="{}" target="_blank">{}</a>',
                           url, _("Pregledaj"))

    show_detail_url.short_description = _("Prikaži na webu")
