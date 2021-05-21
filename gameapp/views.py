from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse

from .models import Game, GameLevel, CorrectAnswers, UserAnswers, Promt
from .form import GetUserAnswer
from django.views.generic import DetailView
from django.views.generic.list import ListView

# Create your views here.




class GameLevelView(DetailView):
    model = GameLevel
    template_name = 'game.html'
    context_object_name = 'level'


    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args,**kwargs)



    def get_context_data(self, **kwargs):

        # if request.method == 'POST':
        #     register_form = GetUserAnswer(request.POST, request.FILES)
        #
        #     if register_form.is_valid():
        #         register_form.save()
        #         return HttpResponseRedirect(reverse('level:level'))
        # else:
        #     register_form = GetUserAnswer()

        context = super().get_context_data(**kwargs)
        level =  self.get_object()
        correct_answers = CorrectAnswers.objects.filter(level_id = level)
        user_answers = UserAnswers.objects.all()
        context.update({'title':level.name,
                        'correct_answers':correct_answers,
                        'user_answers':user_answers,
                        # 'register_form': register_form,
                        })
        return context