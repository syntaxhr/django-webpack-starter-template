from cms.models import Title
from django.shortcuts import render
from django.views import View

from posts.models import Post


class PostListSearch(View):

    template_name = 'posts/posts_search.html'

    def get(self, request, *args, **kwargs):

        posts = Post.objects.filter(published=True)
        titles = Title.objects.all()
        query_string = request.GET.get('query')

        if query_string:

            posts = posts.filter(summary__search=query_string, title__search=query_string).distinct()
            titles = titles.filter(title__search=query_string).distinct()

        context = {
            'posts': posts[:50],
            'titles': titles[:50],
            'query_string': query_string
        }

        return render(request, self.template_name, context)
