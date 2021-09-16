from django.contrib import auth
from django.shortcuts import redirect, render
from home import models

# Create your views here.


def blog(request):
    blogs = models.Blog.objects.all().order_by('-date')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context)


def singleBlog(req, id):
    blog = models.Blog.objects.get(id=id)
    relatedBlogs = models.Blog.objects.filter(
        genre=blog.genre).order_by('-date')[:10]
    context = {
        'blog': blog,
        'relatedBlogs': relatedBlogs
    }
    return render(req, 'singleBlog.html', context)


def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST['title']
            genre = request.POST['genre']
            description = request.POST['description']

            x = models.Blog.objects.create(
                title=title, genre=genre, author=request.user.username, description=description)
            x.save()
            return redirect('blog')

        else:
            return render(request, 'create.html')
    else:
        return redirect('login')


def delete(request, id):
    if request.user.is_authenticated:
        b = models.Blog.objects.get(id=id)
        if b.author == request.user.username:
            models.Blog.objects.filter(id=id).delete()
            return redirect('blog')

        else:
            return redirect(f'/blog/{id}')
