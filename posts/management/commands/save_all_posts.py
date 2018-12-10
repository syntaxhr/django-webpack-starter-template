from django.core.management import BaseCommand

from posts.models import Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        posts = Post.objects.all()

        for post in posts:
            post.save()

        self.stdout.write(self.style.SUCCESS('Successfully saved all posts'))

