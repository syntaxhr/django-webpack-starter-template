from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import View
from posts.models import Post
from posts.settings import *
from django.utils.translation import ugettext_lazy as _


class PostDetail(View):

    @staticmethod
    def _create_cms_toolbar(request, post):
        menu = request.toolbar.get_or_create_menu(CMS_TOOLBAR_APP_NAME, _('Posts'))
        menu.add_modal_item(_('Edit this post'), url=reverse('admin:posts_post_change', args=[post.id]))
        menu.add_sideframe_item(_('Delete this post'), url=reverse('admin:posts_post_delete', args=[post.id]))
        menu.add_sideframe_item(_('Show History of this post'), url=reverse('admin:posts_post_history', args=[post.id]))

    def get(self, request, post_id, post_slug, *args, **kwargs):

        post = get_object_or_404(Post, pk=post_id)
        self._create_cms_toolbar(request=request, post=post)

        context = {
            "post": post,
            "section": post.section,
            "request": request
        }

        return render(request, post.template, context)
