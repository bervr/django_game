from django.shortcuts import render
import git

# Create your views here.

def main(request):
    return render(request, 'index.html')

def update_server(request):
    if request.method == 'POST':
        repo = git.Repo('https://github.com/bervr/django_game.git')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400



