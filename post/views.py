from django.shortcuts import render
from django.http import HttpResponse
from . models import Post, Comment
from . forms import PostForm, CommentForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from django.core.paginator import Paginator, PageNotAnInteger , EmptyPage


@login_required(login_url='accounts/login')
def homePage(request):
    posts = Post.objects.all()



    page = request.GET.get('page')
    num_of_items = 6
    paginator = Paginator(posts, num_of_items)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)
    
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)

    context = {
        'posts': posts,
        'paginator': paginator,
      

    }
    return render(request, 'post/home.html', context)


@login_required(login_url='home')
def homeDetail(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'post/home_detail.html', context)


@login_required(login_url='home')
def AuthorPage(request):
    
    posts = Post.objects.all()
    context = {
        'posts': posts

    }
    return render(request, 'post/author.html', context)





@login_required(login_url='home')
def addPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    context = {
        "form":form
    }

    return render(request, 'post/addPost.html', context)




@login_required(login_url='home')
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            posti = Post.objects.filter(first_name__icontains=query) 
            return render(request, 'post/searchbar.html', {'posti':posti})
        else:
            print("No information to show")
            return render(request, 'post/searchbar.html', {})


def add_comment(request, slug):
    post = Post.objects.get(slug=slug)

    form = CommentForm(instance=post)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=post)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(post=post, commenter_name=name, comment_body=body, )
            c.save()
            return redirect('home')
        else:
            print('form is invalid')    
    else:
        form = CommentForm()    


    context = {
        'form': form
    }

    return render(request, 'post/add_comment.html', context)


