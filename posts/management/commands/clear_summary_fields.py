from django.core.management import BaseCommand

from posts.models import Post
from posts.utils import get_translation_field_per_language


class Command(BaseCommand):
    help = "Clear all summaries for every language, for every post"

    def _print_info(self, id, title):
        self.stdout.write(self.style.HTTP_NOT_MODIFIED("Summary cleared for: [id={id}] {title}".format(id=id, title=title)))

    def _print_final_info(self, count):
        self.stdout.write(self.style.SUCCESS("Number of posts updated: {count}".format(count=count)))

    def add_arguments(self, parser):

        parser.add_argument('-n', '--number', type=int, default=None,
                            help='Indicates the number of posts that will have the summary field cleared“')

        parser.add_argument('-l', '--language', type=str, default=None,
                            help='Clear the summary of all posts for a specific language')

    def handle(self, *args, **options):

        number_of_items = options['number']
        language = options['language']

        posts = Post.objects.all()[:number_of_items] if number_of_items else Post.objects.all()

        for post in posts:

            translated_fields = get_translation_field_per_language('summary', language)

            for field in translated_fields:
                setattr(post, field, "")
                post.save()

            self._print_info(post.id, post.title)

        self._print_final_info(posts.count())
