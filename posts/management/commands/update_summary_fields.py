from django.core.management import BaseCommand
from django.utils.html import strip_tags
from djangocms_text_ckeditor.models import Text

from posts.models import Post
from posts.utils import get_translation_fields_per_language


class Command(BaseCommand):
    help = "Update all summary fields from content fields per language"

    def _print_info_title(self, language, id, title):
        self.stdout.write(self.style.HTTP_NOT_MODIFIED("[{language}] Summary updated for: [id={id}] {title}".format(language=language, id=id, title=title)))

    def _print_summary(self, summary):
        self.stdout.write(self.style.HTTP_SUCCESS("{summary}\n".format(summary=summary)))

    def _print_final_info(self, count):
        self.stdout.write(self.style.SUCCESS("Number of summaries updated: {count}".format(count=count)))

    def add_arguments(self, parser):

        parser.add_argument('-n', '--number', type=int, default=None,
                            help='Indicates the number of posts that will have copied the content to the summary field')

        parser.add_argument('-l', '--language', type=str, default=None,
                            help='Copy the content to the summary field of all posts for a specific language')

    def handle(self, *args, **options):
        counter = 0
        number_of_items = options['number']
        language = options['language']

        posts = Post.objects.all()[:number_of_items] if number_of_items else Post.objects.all()

        for post in posts:

            translated_fields = get_translation_fields_per_language('content', 'summary', language)

            for field in translated_fields:

                references = getattr(post, field["from_field"], False)

                if references:
                    references_list = references.cmsplugin_set.all()
                    texts_model = Text.objects.filter(cmsplugin_ptr__in=references_list)

                    if texts_model:
                        counter += 1
                        texts_body = [text.body for text in texts_model]

                        text = ' '.join(texts_body)

                        clean_text = strip_tags(text).replace('&shy;', '')
                        setattr(post, field["to_field"], clean_text)
                        post.save()

                        self._print_info_title(field["lang"], post.id, getattr(post, field["title"], "No title"))
                        self._print_summary(getattr(post, field["to_field"], "No summary"))

        self._print_final_info(counter)
