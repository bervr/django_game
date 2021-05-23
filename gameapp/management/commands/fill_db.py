import os, json

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from gameapp.models import GameLevel, CorrectAnswers, Game

JSON_PATH = 'gameapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), encoding='utf-8') as f:
        return json.load(f)
#
class Command(BaseCommand):
    def handle(self, *args, **options):
        game = load_from_json('game')
        Game.objects.all().delete()
        for item in game:
            new_game = Game(**item)
            new_game.save()

        levels = load_from_json('levels')
        GameLevel.objects.all().delete()
        for level in levels:
            game = level['level_of_game']
            game_obj = Game.objects.get(game_number=game)
            level['level_of_game'] = game_obj
            new_level = GameLevel(**level)
            new_level.save()

        answers = load_from_json('correctanswers')
        CorrectAnswers.objects.all().delete()
        for answer in answers:
            _level = answer['level']
            level_obj = GameLevel.objects.get(number= _level)
            answer['level'] = level_obj
            new_answer = CorrectAnswers(**answer)
            new_answer.save()

        # User.objects.create_superuser('django', 'django@1.local', '123')