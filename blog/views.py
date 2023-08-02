from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from . forms import FormPost


def post_list(request):
    posts = Post.objects.all()
    return render(request, template_name='blog/post_list.html', context={'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, template_name='blog/post_detail.html', context={'post': post})


def post_new(request):
    if request.method == "POST":
        form = FormPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = FormPost()
        return render(request, template_name='blog/post_edit.html', context={'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = FormPost(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = FormPost(instance=post)
    return render(request, template_name='blog/post_edit.html', context={'form': form})
