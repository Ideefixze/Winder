from django.shortcuts import render, redirect
from .models import Question
from .models import Answer
from .models import User
# Create your views here.

def question_view(request):
    if('user' not in request.session or 'group' not in request.session):
        return redirect ('/')

    nr = request.GET.get('nr')
    maxnr = len(Question.objects.all())

    if request.method=="POST":
        answer = Answer.objects.get(question=Question.objects.get(id=nr), user=User.objects.get(nickname=request.session['user'], group=request.session['group']))
        if answer is not None:
            answer.answer = request.POST.get('answer')
            answer.save()
        else:
            answer = Answer(question=Question.objects.get(id=nr), 
                            user=User.objects.get(nickname=request.session['user'], group=request.session['group']),
                            answer=request.POST.get('answer'))
            answer.save()
        
        return redirect('/question?nr='+str(int(nr)+1))

    
    q = Question.objects.get(id=nr)
    
    context = {
        "object": q,
        "user": request.session['user'],
        "group": request.session['group'],
        "nr": nr,
        "maxnr": maxnr
    }

    return render(request, 'question.html', context)

def startup_view(request):
    if request.method == 'POST':
        request.session['user'] = request.POST.get("user","")
        request.session['group'] = request.POST.get("group","")
        u = User.objects.get_or_create(nickname=request.session['user'], group=request.session['group'])
        u[0].save()
        return redirect('/question?nr=1')
    
    return render(request, 'home.html', {})
    
