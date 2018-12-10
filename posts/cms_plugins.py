from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from posts.models import PostsPlugin, Category, Post
from posts.settings import CMS_PLUGIN_MODULE


class PostsPlugin(CMSPluginBase):
    model = PostsPlugin
    module = CMS_PLUGIN_MODULE
    cache = False
    filter_horizontal = ['categories', ]

    def render(self, context, instance, placeholder):
        context = super(CMSPostsPlugin, self).render(context, instance, placeholder)

        posts = Post.objects.filter(section=instance.section, published=True)

        if instance.categories.all():
            posts = posts.filter(categories__id__in=[category.id for category in instance.categories.all()])

        posts = posts.distinct()[:instance.count]

        context.update({'posts': posts})
        return context

    def get_form(self, request, obj=None, **kwargs):
        if hasattr(obj, "pk"):
            self.section = obj.section
        else:
            self.exclude = ('categories',)

        form = super(CMSPostsPlugin, self).get_form(request, obj, **kwargs)
        return form

    def formfield_for_manytomany(self, db_field, request, **kwargs):

        if db_field.name == "categories":
            kwargs["queryset"] = Category.objects.filter(section__id=self.section.id)

        return super(CMSPostsPlugin, self).formfield_for_manytomany(db_field, request, **kwargs)



@plugin_pool.register_plugin
class CMSPostsPlugin(PostsPlugin):
    name = _("Posts")
    render_template = "posts/cms/posts.html"
