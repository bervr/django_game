import os, json

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from gameapp.models import GameLevel, CorrectAnswers

JSON_PATH = 'gameapp/json'

# def load_from_json(file_name):
#     with open(os.path.join(JSON_PATH, file_name + '.json'), encoding='utf-8') as f:
#         return json.load(f)
#
class Command(BaseCommand):
    def handle(self, *args, **options):
        # levels = load_from_json('levels')
        # GameLevel.objects.all().delete()
        # for level in levels:
        #     new_level = GameLevel(**level)
        #     new_level.save()

#         products = load_from_json('products')
#         for product in products:
#             category_name = product['category']
#             category_obj = ProductCategory.objects.get(href = category_name)
#             product['category'] = category_obj
#             new_product = Product(**product)
#             new_product.save()

        User.objects.create_superuser('django', 'django@1.local', '123')