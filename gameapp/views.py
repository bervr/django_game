from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse

from .models import Game, GameLevel, CorrectAnswers, UserAnswers, Promt
from .form import GetUserAnswer


# Create your views here.

def game_level(request, pk):

    level = GameLevel.objects.get(number=pk)
    correct_answers = CorrectAnswers.objects.filter(level= level)
    user_answers = UserAnswers.objects.all().order_by('-created')
    last_user_answer = user_answers[0]
    other_user_answer = user_answers[1:]

    if request.method == 'POST':
        form = GetUserAnswer(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('game:level', args=[pk]))
    else:
        form = GetUserAnswer(initial={'level': level})

    content = {
        'title': level.name,
        'form': form,
        'pk': pk,
        'correct_answers': correct_answers,
        'user_answers': user_answers,
        'level': level,
        'last_user_answer': last_user_answer,
        'other_user_answer': other_user_answer
    }

    return render(request, 'game.html', content)