from django.contrib.auth.decorators import login_required
from Blog2.models import Post, BlogCategory
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def homeBlog(request):
    blogs = Post.objects.all()
    cats = BlogCategory.objects.all()

    paginator = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    
    context = {
        "blogs":blogs,
        'cats':cats 
    
    }

    
    return render(request, 'blog/homeBlog.html', context)


def blog_detail(request , slug):
    context = {}
    try:
        blog_obj = Post.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
    return render(request , 'blog/blog_detail.html' , context)


def category(request, url):
    cat = BlogCategory.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "blog/category.html", {'cat': cat, 'posts': posts})

def PostDetail(request, slug):
    cats = BlogCategory.objects.all()
    post = Post.objects.get(slug=slug)
    return render(request, "blog/postdetail.html", {'post': post, 'cats':cats})
