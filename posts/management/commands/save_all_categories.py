from django.core.management import BaseCommand

from posts.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = Category.objects.all()

        for category in categories:
            category.save()

        self.stdout.write(self.style.SUCCESS('Successfully saved all categories'))

