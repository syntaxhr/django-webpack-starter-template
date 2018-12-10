from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'
    verbose_name = _('Posts')

    def ready(self):
        import posts.signals
