from cms.menu_bases import CMSAttachMenu
from django.utils.translation import ugettext_lazy as _
from menus.base import NavigationNode
from menus.menu_pool import menu_pool


class PostMenu(CMSAttachMenu):
    name = _('Posts menu')

    def get_nodes(self, request):
        from posts.models import Category

        categories = Category.objects.filter(section__namespace=self.namespace)
        nodes = [NavigationNode(category.name, category.get_absolute_url(), category.id,) for category in categories]
        return nodes


menu_pool.register_menu(PostMenu)
