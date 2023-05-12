from django.shortcuts import render,redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def uheng(request):
    blogs = Blog.objects
    return render(request,'lion.html',{'blogs': blogs})

def edit(request, id):
    edit_blog = Blog.objects.get(id= id)
    return render(request, 'edit.html', {'blog': edit_blog})
def update(request, id):
    update_blog = Blog.objects.get(id= id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()

    return redirect('detail', update_blog.id)