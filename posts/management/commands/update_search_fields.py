from django.core.management import BaseCommand
from djangocms_text_ckeditor.models import Text

from posts.models import Post, CMSPlugin


class Command(BaseCommand):

    current_post = None

    def _get_cms_plugins(self):
        plugins = CMSPlugin.objects.filter(placeholder=self.current_post.content.id)
        for plugin in plugins:

            if plugin.plugin_type == 'TextPlugin':
                try:
                    text_plugin = Text.objects.get(cmsplugin_ptr=plugin)
                    self.current_post.search_field += text_plugin.body
                    self.current_post.save()
                except Text.DoesNotExist:
                    pass

    def _reset_search_field(self):
        self.current_post.search_field = ''
        self.current_post.save()

    def handle(self, *args, **options):
        posts = Post.objects.all()

        for post in posts:
            self.current_post = post
            self._reset_search_field()
            self._get_cms_plugins()

