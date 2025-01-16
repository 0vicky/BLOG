from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args: Any, **options: Any):
        #delete eisting data

        Category.objects.all().delete()
        
        categories = ['Trees', 'Hills', 'Sea', 'Flower', 'Food']

        for category_name in categories:
            Category.objects.create(name = category_name)

            self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
        
        # Reset auto-increment to 1
     

        # Titles, contents, and image URLs
        
        
        # Insert new posts


        
