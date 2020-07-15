from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Question
from .models import Answer
from .models import UserGroup
# Create your views here.

@login_required
def question_view(request):

    nr = int(request.GET.get('nr'))
    group = request.GET.get('group')
    if group==None:
        group='public'

    maxnr = len(Question.objects.all())

    #go to matches
    if(nr>maxnr):
        return redirect('/match?group='+group)

    if request.method=="POST":
        val = int(request.POST.get('answer'))
        q=Question.objects.get(id=nr)
        ug=UserGroup.objects.get(user=request.user, group=group)

        try:
            answer = Answer.objects.get(question=q,usergroup=ug)
            answer.answer = val
            answer.save()
        except:
            answer = Answer(question=q,usergroup=ug,answer=val)
            answer.save()

        

        return redirect('/question?nr='+str(int(nr)+1)+'&group='+group)

    
    q = Question.objects.get(id=nr)
    
    context = {
        "object": q,
        "user": request.user,
        "group": group,
        "nr": nr,
        "maxnr": maxnr
    }

    return render(request, 'question.html', context)

@login_required
def startup_view(request):
    if request.method == 'POST':
        ug = UserGroup.objects.get_or_create(user=request.user, group=request.POST.get('group'))
        ug[0].save()
        return redirect('/question?nr=1&group='+request.POST.get('group'))
    
    return render(request, 'begin.html', {})
    

@login_required
def matches_view(request):
    group = request.GET.get('group')
    if group==None:
        group='public'

    my_answers = Answer.objects.filter(usergroup__in=UserGroup.objects.filter(user=request.user, group=group))
    other_answers = Answer.objects.filter(usergroup__in=UserGroup.objects.filter(group=group).exclude(user=request.user))

    scoredict = dict()
    

    maxnr = len(Question.objects.all())

    for i in range(1,maxnr+1):
        
        try:
            my_ans_i = Answer.objects.get(usergroup=UserGroup.objects.get(user=request.user, group=group),question__id=i)
        except:
            my_ans_i = Answer(usergroup=UserGroup.objects.get(user=request.user, group=group),question=Question.objects.get(id=i),answer=2)
            my_ans_i.save()
        
        others = UserGroup.objects.filter(group=group).exclude(user=request.user)

        for j in others:
            try:
                other_answer = Answer.objects.get(usergroup=j,question__id=i)
            except:
                other_answer = Answer(UserGroup=j,question=Question.objects.get(id=i),answer=2)
                other_answer.save()

            scoredict.setdefault(j.user.username,0)
            scoredict[j.user.username]+=my_ans_i.score(other_answer)
    
    for key,value in scoredict.items():
        scoredict[key] = str(int(float(value/maxnr*100)))+"%"

    context = {
        'scores':scoredict,
        'group':group
    }
    return render(request, 'matches.html', context)

    