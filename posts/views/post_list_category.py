from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from posts.mixins import ListViewUtilsMixin
from posts.models import Post, Category
from posts.settings import SORT_FILERS


class PostListCategory(ListViewUtilsMixin, View):

    def get(self, request, category_id, category_slug, *args, **kwargs):

        active_filter = self.get_active_filter(request)

        category = get_object_or_404(Category, pk=category_id)
        posts = Post.objects.filter(categories__in=[category]).order_by(active_filter)

        context = {
            "section": category.section,
            "posts": posts,
            "category": category,
            "active_filter": active_filter,
            "sort_filters": SORT_FILERS,
            'request': request,
        }

        return render(request, category.template, context)
