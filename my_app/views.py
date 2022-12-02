from django.shortcuts import render, HttpResponse
from .models import Debate
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def debate_list(request):
    obj = Debate.objects.all()
    return render(request, 'dashboard.html', {'obj': obj})


@login_required
def debate_challenge(request,pk):
    debate = Debate.objects.get(pk=pk)
    debate.debator = request.user
    debate.save()

    obj = Debate.objects.all()
    return render(request,'dashboard.html', {'obj': obj})


@login_required
def debatelistforuser(request):
    a = Debate.objects.filter(debator = request.user)
    return render(request, 'challenge.html', {'a': a})

