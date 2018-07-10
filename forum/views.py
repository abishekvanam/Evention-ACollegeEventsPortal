from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from. import mypythoncode
from .models import *
from .forms import *
from django.utils import timezone
# Create your views here.


def indd(request):
    return render(request,'forum/ind.html',{})


def begin(request):
    return render(request,'forum/start_page.html',{})
    pass


def display_ques(request):
    #all_questions=Question.objects.all()
    all_questions = Question.objects.order_by('-question_pub_date')
    context={'all_questions':all_questions}
    return render(request,'forum/display_questions.html',context)
    pass

@login_required(login_url="logins:login_view")
def display_ans(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        obj = Answer(
            answer_text=answer,
            question_id_of_answer=question_id,
            answer_pub_date=timezone.now(),
            answered_by=request.user.username
        )
        obj.save()

    answers = Answer.objects.filter(question_id_of_answer=question_id)
    context = {'question': question, 'answers': answers}

    return render(request, 'forum/display_answers.html', context)



@login_required(login_url="logins:login_view")
def ask(request):
    return render(request, 'forum/ask_questions.html', {})

def ask_questions(request):
    if request.method == 'POST':
        form=QuestionForm(request.POST)
        question = request.POST.get('question','')
        obj=Question(question_text=question,
                     question_pub_date=timezone.now(),
                     asked_by=request.user.username
                )
        obj.save()
        all_questions = Question.objects.order_by('-question_pub_date')
        context = {'all_questions': all_questions}
        return render(request,'forum/display_questions.html',context)
    return render(request,'forum/start_page.html',{})





