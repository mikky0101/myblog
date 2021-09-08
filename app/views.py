from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import DetailView, ListView, TemplateView, View
from app.models import Category, Comment, Post, Author,Contact, Reply
from django.db.models import Count, Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import CommentForm, PostForm, ContactForm

# Create your views here.

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def get_category_count():
    queryset = Post \
        .objects \
        .values('Category__name') \
        .annotate(Count('Category__name'))
    return queryset


def home(request):
    category_count = get_category_count()
    print(category_count)
    featured = Post.objects.filter(featured=True)
    category = Category.objects.all()
    # print(category)
    posts = Post.objects.all()
    latest = Post.objects.order_by('-timestamp')[0:3]
    print(posts)
    print(featured)
    context = {
        "featured": featured,
        'posts': posts,
        "latest": latest,
        "category_count": category_count,
        "category": category
    }
    return render(request, "index.html", context)

def search(request):
    queryset = Post.objects.all()
    latest = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category_count()
    category = Category.objects.all()
    query = request.GET.get('q')
    if query:
       queryset = queryset.filter(
          Q(title__icontains=query) |
          Q(overview__icontains=query)
       ).distinct()
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)  
    context = {
      'queryset': users,
      "category": category,
       "category_count": category_count,
      "latest": latest
    }    
    return render(request, "search.html", context)    

def technology(request):
    queryset = Post.objects.filter(main_cat="Technology")
    latest = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category_count()
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    print(queryset)
    print(queryset)
    category = Category.objects.all()
    context = {
        'queryset': users,
        "category_count": category_count,
        "latest": latest,
        "category": category
    }
    return render(request, "technology.html", context)

def sports(request):
    queryset = Post.objects.filter(main_cat="sports")
    latest = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category_count()
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    print(queryset)
    print(queryset)
    category = Category.objects.all()
    context = {
        'queryset': users,
        "category_count": category_count,
        "latest": latest,
        "category": category
    }
    return render(request, "sport.html", context)         

def nature(request):
    queryset = Post.objects.filter(main_cat="nature")
    latest = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category_count()
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    print(queryset)
    print(queryset)
    category = Category.objects.all()
    context = {
        'queryset': users,
        "category_count": category_count,
        "latest": latest,
        "category": category
    }
    return render(request, "nature.html", context)           

def entertainment(request):
    queryset = Post.objects.filter(main_cat="entertainment")
    latest = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category_count()
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    print(queryset)
    print(queryset)
    category = Category.objects.all()
    context = {
        'queryset': users,
        "category_count": category_count,
        "latest": latest,
        "category": category
    }
    return render(request, "entertainment.html", context)    

def education(request):
    queryset = Post.objects.filter(main_cat="education")
    latest = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category_count()
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    print(queryset)
    print(queryset)
    category = Category.objects.all()
    context = {
        'queryset': users,
        "category_count": category_count,
        "latest": latest,
        "category": category
    }
    return render(request, "education.html", context)        

def blog(request):
    posts = Post.objects.all()
    latest = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category_count()
    category = Category.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)  
    context = {
        "posts": users,
        "category_count": category_count,
        "latest": latest,
        "category": category
    }
    return render(request, "blog.html", context)  

class BlogDetailView(DetailView):
    model = Post
    template_name = "post-details.html"

def details(request, pk):
    category_count = get_category_count()
    post = Post.objects.get(id=pk)
    category = Category.objects.all()
    latest = Post.objects.order_by('-timestamp')[0:3]
    comment = Comment.objects.filter(post=post).order_by('-timestamp')
    reply = Reply.objects.filter(comment__in = comment)
    print(reply)
    page = request.GET.get('page', 1)
    paginator = Paginator(comment, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages) 
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("blog:detail", kwargs={
                'pk': post.pk
            }))
    context = {
        "post": post,
        "latest": latest,
        "category_count": category_count,
        "form": form,
        "reply": reply,
        "category": category,
        "comment": users
    }
    return render(request, "post-details.html", context)      


def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("blog:detail", kwargs={
                'pk': form.instance.id
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "post-create.html", context)

def post_update(request, id):
    title = 'Update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(
        request.POST or None,
        request.FILES or None,
        instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("blog:detail", kwargs={
                'pk': form.instance.id
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "post-create.html", context)    


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("post-list"))


def contact(request):
    form = ContactForm()
    print(form)
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            Contact.objects.create(name=name, email=email, subject=subject, text=message)
            return redirect(reverse("blog:home"))
    context = {
        "form": form
    }        
    return render(request, "contact.html", context)    

def author_profile(request, pk):
    author = Author.objects.get(id=pk)
    post = Post.objects.filter(author=author)
    latest = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category_count()
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 4)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages) 

    context = {
        "author": author,
        "posts": users,
        "latest": latest,
        "category_count": category_count
    }

    return render(request, "profile.html", context)


def about(request):
    authors = Author.objects.all()
    context = {
        "authors": authors
    }
    return render(request, "about.html", context)