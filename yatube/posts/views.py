from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group, User
from .forms import PostForm


def index(request):
    post_list = Post.objects.order_by("-pub_date").all()
    paginator = Paginator(post_list, 10) # показывать по 10 записей на странице.

    page_number = request.GET.get('page') # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number) # получить записи с нужным смещением
    return render(request, 'index.html', {'page': page})

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group = group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group":group, "posts":posts})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        return render(request, 'new.html', {'form':form})
    form = PostForm()
    return render(request, 'new.html', {'form':form})

def profile(request, username):
    # тут тело функции
    user = get_object_or_404(User, username=username)
    post_list = user.posts.order_by("-pub_date").all()
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page') 
    page = paginator.get_page(page_number) 
    return render(request, "profile.html", {"user":user, 'page':page})
     

def post_view(request, username, post_id):
        # тут тело функции
    post = Post.objects.get(id=post_id)
    return render(request, "post.html", {"post":post})

def post_edit(request, username, post_id):
    post = get_object_or_404(Post, id=post_id)
    current_user = request.user
    if current_user == post.author:
        form = PostForm(request.POST or None, instance = post)
        if form.is_valid():
            form.save()
            return redirect('post', username=current_user.username, post_id = post.id)
        return render(request, 'post_edit.html', {'form':form})
        # тут тело функции. Не забудьте проверить, 
        # что текущий пользователь — это автор записи.
        # В качестве шаблона используйте шаблон для создания новой записи,
        # который вы использовали раньше (вы могли назвать шаблон иначе)
    return render(request, "post_new.html", {"form":form})