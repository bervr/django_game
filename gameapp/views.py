from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse

from .models import Game, GameLevel, CorrectAnswers, UserAnswers, Promt
from .form import GetUserAnswer


# Create your views here.
@user_passes_test(lambda u: u.is_active)
def game_level(request, pk, game = 1):
    now_game= Game.objects.get(game_number = game)
    game_started = now_game.Game_go
    now_level = get_object_or_404(GameLevel, pk=pk)
    next_level = get_object_or_404(GameLevel, pk=pk+1)
    active_level = GameLevel.objects.filter(level_active = True)[0]

    if game_started:
        level = GameLevel.objects.get(number=pk)
        correct_answers = CorrectAnswers.objects.filter(level= level)

        if now_level.level_active or next_level.level_active and not now_level.level_last:
            if request.method == 'POST':
                form = GetUserAnswer(request.POST, request.FILES)
                if form.is_valid():
                    last_user_answer = form.instance.answer
                    form.save()
                    for answer in correct_answers:
                        if str(answer.answer).lower() == str(last_user_answer).lower():
                            now_level.level_done = True
                            next_level.level_active = True
                            now_level.level_active = False
                            now_level.save()
                            next_level.save()
                            if next_level.level_last == True:
                               now_game.Game_go =False
                               now_game.save()
                               context = {
                                    'title': 'Игра завершена. Вы победили, поздравляем!',
                                }
                               return render(request, 'index.html', context)
                            return HttpResponseRedirect(reverse('game:level', args=[next_level.number]))
                        else:
                            return HttpResponseRedirect(reverse('game:level', args=[now_level.number]))
            else:
                form = GetUserAnswer(initial={'level': level})
            user_answers = UserAnswers.objects.all().order_by('-created')
            if len(user_answers) >= 2:
                last_user_answer = user_answers[0]
                other_user_answer = user_answers[1:]
            elif len(user_answers) == 1:
                last_user_answer = user_answers[0]
                other_user_answer = ''
            else:
                last_user_answer = ''
                other_user_answer = ''
            context = {
                'title': level.name,
                'form': form,
                'pk': pk,
                'correct_answers': correct_answers,
                'level': level,
                'now_level':now_level,
                'last_user_answer': last_user_answer,
                'other_user_answer': other_user_answer
            }

            if now_level.number == pk:
                return render(request, 'game.html', context)
            else:
                return HttpResponseRedirect(reverse('game:level', args=[active_level.number]))
                # context.update({'pk':active_level.number})
                # return render(request, 'game.html', context)
            # else:
            #     for level in other_levels:
            #         if  level.level_active:
            #             return render(request, 'game.html', context)
            #         else:
            #             return HttpResponseRedirect(reverse('game:level', args=[now_level.number]))


        else:
            return HttpResponseRedirect(reverse('game:level', args=[active_level.number]))
    else:
        context = {
            'title':'Игра завершена или еще не началась',
            'now_level':active_level.number,
        }
        return render(request, 'index.html', context)
