from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data['title'],
                photo=form.cleaned_data['photo'],
            )
        return redirect('post_list')
    else:
        form = PostForm()
        context = {
            'form': form,
        }
    return render(request, 'post/post_create.html', context)


def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('post_list')
    return HttpResponse('Permission Denied', status=403)

