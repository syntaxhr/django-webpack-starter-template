from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from posts.mixins import ListViewUtilsMixin
from posts.settings import SORT_FILERS
from posts.models import Post, Section


class PostList(ListViewUtilsMixin, View):

    def get(self, request, *args, **kwargs):

        active_filter = self.get_active_filter(request)

        section = get_object_or_404(Section, namespace=request.current_page.application_namespace)

        # TODO remove legacy query
        posts = Post.objects.filter(section__id=section.id, published=True).distinct().order_by(active_filter)
        # posts = Post.objects.filter(section__id=section.id, published=True, legacy_images__isnull=False).distinct().order_by(active_filter)

        context = {
            "section": section,
            "posts": posts,
            "active_filter": active_filter,
            "sort_filters": SORT_FILERS,
        }

        return render(request, section.template, context)
