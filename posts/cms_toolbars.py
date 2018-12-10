from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from posts.settings import CMS_TOOLBAR_APP_NAME


@toolbar_pool.register
class PostToolbar(CMSToolbar):

    def populate(self):

        if self.is_current_app:
            menu = self.toolbar.get_or_create_menu(CMS_TOOLBAR_APP_NAME, _('Posts'))
            url = reverse('admin:posts_post_changelist')
            menu.add_sideframe_item(_('Posts overview'), url=url)
