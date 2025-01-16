from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
from django.db import connection
import random


class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args: Any, **options: Any):
        #delete eisting data
        Post.objects.all().delete()
        
        # Reset auto-increment to 1
        with connection.cursor() as cursor:
            cursor.execute("ALTER TABLE blog_post AUTO_INCREMENT = 1;")

        # Titles, contents, and image URLs
        titles = [
            "Misty Pines: A Forest of Tranquility",
            "The Majestic Oak: Nature's Ancient Wonder",
            "Cherry Blossoms in Full Bloom",
            "The Lush Green Rainforest",
            "Waves of Serenity on a Sandy Beach",
            "Sunset Calm: The Peaceful Sea",
            "Clear Waters: The Hidden Reefs",
            "Stormy Seas: The Fury of the Ocean",
            "Rolling Hills Beneath the Open Sky",
            "Winter's Touch on Snow-Capped Hills",
            "Wildflower Hills: A Blanket of Color",
            "Golden Hills: A Sunset Retreat",
            "A Sunflower's Radiant Field",
            "Roses in Bloom: A Botanical Paradise",
            "The Meadow of Wildflowers",
            "Tulips Blooming: The Spring Awakening",
            "A Vibrant Sushi Platter",
            "A Pizza Feast: Freshly Baked and Tasty",
            "Berry Bliss: A Bowl of Freshness",
            "Gourmet Burger: The Perfect Bite",
        ]
        
        contents = [
            "Tall pine trees in a misty forest.",
            "Ancient oak tree with sprawling branches.",
            "Cherry blossom trees in full bloom.",
            "A dense rainforest with lush green trees.",

    # Sea
            "Waves crashing on a sandy beach.",
            "A calm sea with a beautiful sunset.",
            "Crystal-clear waters with coral reefs visible.",
            "A stormy sea with dramatic waves.",

    # Hills
            "Rolling green hills under a blue sky.",
            "Snow-capped hills during winter.",
            "Hills covered in wildflowers.",
            "Golden hills during sunset.",

    # Flowers
            "A vibrant field of sunflowers.",
            "Roses in a botanical garden.",
            "A meadow full of wildflowers.",
            "Tulips blooming in spring.",

    # Food
            "A plate of colorful sushi rolls.",
            "A freshly baked pizza with toppings.",
            "A bowl of mixed berries and yogurt.",
            "A gourmet burger with fries.",
        ]
        
        img_urls = [
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/27/800/400",
            "https://picsum.photos/id/13/800/400",
            "https://picsum.photos/id/82/800/400",
            "https://picsum.photos/id/431/800/400",
            "https://picsum.photos/id/19/800/400",
            "https://picsum.photos/id/29/800/400",
            "https://picsum.photos/id/14/800/400",
            "https://picsum.photos/id/106/800/400",
            "https://picsum.photos/id/429/800/400",
            "https://picsum.photos/id/25/800/400",
            "https://picsum.photos/id/54/800/400",
            "https://picsum.photos/id/16/800/400",
            "https://picsum.photos/id/152/800/400",
            "https://picsum.photos/id/493/800/400",
            "https://picsum.photos/id/28/800/400",             
            "https://picsum.photos/id/79/800/400",
            "https://picsum.photos/id/44/800/400",
            "https://picsum.photos/id/306/800/400",
            "https://picsum.photos/id/63/800/400",
        ]
        
        categories = Category.objects.all()
        # Insert new posts
        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
