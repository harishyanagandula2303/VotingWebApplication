from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import  Question, Choice

def index(request):
    return render(request, 'polls/index.html')

def view_questions(request):
    questions = Question.objects.all()
    return render(request, 'polls/view_questions.html', {'questions': questions})



def conduct_poll(request, question_id=None):  # Accept question_id as an optional argument
    if request.method == 'POST':
        question_text = request.POST['question']
        choices = request.POST.getlist('choices[]')

        question = Question.objects.create(question_text=question_text)

        for choice_text in choices:
            question.choice_set.create(choice_text=choice_text, votes=0)

        return HttpResponseRedirect(reverse('polls:view_questions'))

    else:
        return render(request, 'polls/conduct_poll.html')


def view_results(request):
    questions = Question.objects.all()
    return render(request, 'polls/view_results.html', {'questions': questions})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        selected_choice = get_object_or_404(Choice, pk=selected_choice_id)
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:view_results_single', args=(question.id,)))
    return render(request, 'polls/vote.html', {'question': question})

def view_results_single(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/view_results_single.html', {'question': question})
# --------------------------------

from django.shortcuts import render
from django.http import JsonResponse

def signup_view(request):
    if request.method == 'POST':
        # Handle signup form submission
        # Process form data, save to database, etc.
        return JsonResponse({'message': 'User registered successfully'})

    return render(request, 'polls/signup.html')

def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        # Check credentials, log in user, set session, etc.
        return JsonResponse({'success': True, 'message': 'Login successful'})

    return render(request, 'polls/login.html')


def view_user(request):
    # Your view logic here
    return render(request, 'htmlwebsite/user_info.html')