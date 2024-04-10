from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from .models import User, Posts, Topics, Comments

from .forms import CommentForm, UserForm

from .utils import get_sha256_hash, gen_random_code
from .Captcha import Captcha


def index(request):
    posts = Posts.objects.select_related('by', 'topic').all().order_by('-date')
    return render(request, 'posts/index.html', {'posts': posts})


def login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    if username and password:
        has_user = User.objects.filter(username=username).first()
        has_pass = get_sha256_hash(password) == has_user.password

        if request.session['captcha'].lower() != request.POST.get('captcha').lower():
            return render(request, 'posts/login.html', )

        if has_pass:
            request.session['userid'] = has_user.id
            request.session['username'] = has_user.username
            request.session['avatar'] = has_user.avatar.url
            return redirect('/')

    return render(request, 'posts/login.html', )


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.password = get_sha256_hash(form.cleaned_data['password'])
            if 'avatar' in request.FILES:
                f.avatar = request.FILES['avatar']
            f.save()
            return redirect('/login')
        else:
            print(form.errors)
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
    comments = Comments.objects.filter(post=id).order_by('-date')
    return render(request, 'posts/detail.html', {'post': post, 'comments': comments})


def comment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.create_user = User.objects.get(id=request.session['userid'])
            f.post_id = id
            f.save()
        else:
            print(form.errors)
    return redirect(reverse('posts:detail', args=[id]))


def get_captcha(request):
    """验证码"""
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')
