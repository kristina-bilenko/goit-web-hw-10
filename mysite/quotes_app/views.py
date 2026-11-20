from django.http import HttpResponse
from .mongo_models import Authors, Quotes
from django.shortcuts import render, redirect
from .forms import RegisterForm, AuthorForm, QuoteForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from .mongo_connection import connection
from django.contrib.auth.decorators import login_required



def home(request):
    quotes = Quotes.objects.all()
    return render(request, 'quotes_app/home.html', {'quotes': quotes})


def author_detail(request, author_id):
    author = Authors.objects(id=author_id).first()

    if not author:
        return HttpResponse("Author not found", status=404)

    return render(request,'quotes_app/author_detail.html',{'author': author})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    
    return render(request, 'quotes_app/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'quotes_app/login.html', {'form': form})


def user_logout(request):
    auth_logout(request)
    return redirect('home')

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            Authors(
                fullname=form.cleaned_data['fullname'],
                born_date=form.cleaned_data['born_date'],
                born_location=form.cleaned_data['born_location'],
                description=form.cleaned_data['description']
            ).save()

            return redirect('home')
    else:
        form = AuthorForm()

    return render(request, 'quotes_app/add_author.html', {'form': form})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)

        if form.is_valid():
            author = Authors.objects(id=form.cleaned_data['author']).first()

            tags = [
                tag.strip()
                for tag in form.cleaned_data['tags'].split(',')
                if tag.strip()
            ]

            Quotes(
                quote=form.cleaned_data['quote'],
                author=author,
                tags=tags
            ).save()

            return redirect('home')
    else:
        form = QuoteForm()

    return render(request, 'quotes_app/add_quote.html', {'form': form})
