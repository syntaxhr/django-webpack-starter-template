from modeltranslation.translator import TranslationOptions, register
from posts.models import Post, Category, Section


@register(Post)
class PostTranslation(TranslationOptions):
    fields = ['title', 'slug', 'summary', 'content']


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ['name', 'slug']


@register(Section)
class SectionTranslation(TranslationOptions):
    fields = ['name', 'slug']
