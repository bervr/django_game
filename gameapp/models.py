from django.db import models


class Game(models.Model):
    game_number = models.IntegerField(
        primary_key=True,
    )
    game_name = models.CharField(max_length=64, verbose_name='название игры')
    Game_go = models.BooleanField(default=False)

    @property
    def now_level(self):
        now_level = models.IntegerField(default=1)
        return now_level

    def __str__(self):
        return self.game_name


class GameLevel(models.Model):
    level_of_game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        verbose_name='игра',
    )
    number = models.IntegerField(
        primary_key=True,
    )
    name = models.CharField(max_length=64, unique=True, verbose_name='название уровня')
    task = models.TextField(verbose_name='текст задания', )
    image = models.ImageField(
        upload_to='level_img',
        blank=True,
    )
    level_active = models.BooleanField(default=False)
    level_done = models.BooleanField(default=False)
    level_last = models.BooleanField(default=False)
    started = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'({self.number} - {self.name})'


class CorrectAnswers(models.Model):
    level = models.ForeignKey(
        GameLevel,
        on_delete=models.CASCADE,
        verbose_name='уровень',

    )
    answer = models.CharField(max_length=256)
    def __str__(self):
        return f'({self.level} - {self.answer})'

class UserAnswers(models.Model):
    level = models.ForeignKey(
        GameLevel,
        on_delete=models.CASCADE,
        verbose_name='уровень',
    )
    answer = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.answer




class Promt(models.Model):
    level = models.ForeignKey(
        GameLevel,
        on_delete=models.CASCADE,
        verbose_name='уровень',
    )
    promt = models.CharField(max_length=256, blank=True, verbose_name='подсказка')
    image = models.ImageField(
        upload_to='promt_img',
        blank=True,
    )
    counter = models.IntegerField(
    )
    def __str__(self):
        return f'(Уровень {self.level} подсказка {self.counter})'
