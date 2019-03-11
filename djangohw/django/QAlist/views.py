from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def all_questions(request):
    posts = Post.objects.all()
    return render(request, 'all_questions.html', {'posts': posts})

def question(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'question.html', {'post': post})

def new_question(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('question', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'new_question.html', {'form': form})

