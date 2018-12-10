from django.core.management import BaseCommand

from posts.models import Section


class Command(BaseCommand):

    def handle(self, *args, **options):
        sections = Section.objects.all()

        for section in sections:
            section.save()

        self.stdout.write(self.style.SUCCESS('Successfully saved all sections'))

