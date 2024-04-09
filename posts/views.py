import hashlib
from django.shortcuts import render, redirect

from .models import User, Posts, Topics


def index(request):
    posts = Posts.objects.select_related('by', 'topic').all().order_by('-date')
    return render(request, 'posts/index.html', {'posts': posts})


def login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    if username and password:
        has_user = User.objects.filter(username=username).first()
        has_pass = hashlib.sha256(password.encode()).hexdigest() == has_user.password
        if has_pass:
            request.session['userid'] = has_user.id
            request.session['username'] = has_user.username
            return redirect('/')

    return render(request, 'posts/login.html', )


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        desc = request.POST.get('desc', None)
        if username and password:
            User.objects.create(
                username=username,
                password=hashlib.sha256(password.encode()).hexdigest(),
                email=email,
                desc=desc
            )
            return redirect('/login')

    return render(request, 'posts/register.html',)


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        topic = Topics.objects.filter(id=request.POST.get('topic')).first()
        by = User.objects.filter(id=request.session['userid']).first()
        Posts.objects.create(title=title, content=content, topic=topic, by=by)
        return redirect('/')

    topics = Topics.objects.all()
    return render(request, 'posts/create.html', {'topics': topics})


def user(request, by_id):
    posts = Posts.objects.filter(by=by_id).order_by('-date')
    return render(request, 'posts/user.html', {'posts': posts})


def detail(request, id):
    post = Posts.objects.select_related('topic').filter(id=id).first()
    return render(request, 'posts/detail.html', {'post': post})
