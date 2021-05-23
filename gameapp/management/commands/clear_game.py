

from django.core.management.base import BaseCommand

from gameapp.models import GameLevel, CorrectAnswers, Game

#
class Command(BaseCommand):
    def handle(self, *args, **options):
        game = Game.objects.get(pk=1)
        game.Game_go =True
        game.save()

        levels = GameLevel.objects.all()
        for level in levels:
            if level.number == 1:
                level.level_active =True
            else:
                level.level_active =False
            level.level_done = False
            level.save()

