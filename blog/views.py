from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Haroon',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'06-Jan-2020'
    },
    {
        'author':'Zain',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'07-Jan-2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})