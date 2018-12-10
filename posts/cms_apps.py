from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from posts.menu import PostMenu
from .cms_app_base import CMSConfigApp


@apphook_pool.register
class PostApp(CMSConfigApp):
    from posts.models import Section

    app_config = Section
    app_name = 'post'
    menus = [PostMenu]
    name = _('Posts')

    def get_urls(self, page=None, language=None, **kwargs):
        return ['posts.urls']
