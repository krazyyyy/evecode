from django.shortcuts import render, redirect
from django.db.models import Count

from .models import Contact, Agent, Properties, Reviews, Blog, Comment
# Create your views here.
def index(request):
    prop = Properties.objects.all()
    agent_prop = Properties.objects.values('agent').annotate(Count('id'))
    agents = Agent.objects.all()
    blog = Blog.objects.all()
    city = Properties.objects.values('location',).annotate(Count('id')).order_by().filter(id__count__gt=0)
    return render(request, 'estate/index.html',{
        'prop' : prop,
        'agents' : agents,
        'blog' : blog,
        'city' : city,
        'li' : agent_prop
    })

def contact(request):
    return render(request, 'estate/contact.html')

def send_message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        message = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        message.save()
        return render(request, 'estate/contact.html', {
            'message' : "Succesfully Sended "
        })

def about(request):
    return render(request, 'estate/about.html')


def properties(request):
    properties = Properties.objects.all()
    return render(request, 'estate/properties.html', {
        "prop" : properties,
    })
    
def agent(request):
    properties = Properties.objects.values('agent').annotate(Count('id'))
    return render(request, 'estate/agent.html', {
        'agents' : Agent.objects.all(),
        'prop' : properties
    })

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'estate/blog.html',{
        'blog' : blog
    })


def services(request):
    return render(request, 'estate/services.html')

def property(request, prop_id):
    properties = Properties.objects.get(id=prop_id)
    reviews = Reviews.objects.filter(property=prop_id)
    return render(request, 'estate/properties_single.html', {
        "prop" : properties,
        "reviews" : reviews
    })

def review(request, p_id):
    properties  = Properties.objects.get(id=p_id)
    if request.method == "POST":
        name = request.POST['name']
        review = request.POST['review']
        rating = request.POST['rating']
        rev = Reviews.objects.create(name=name, review=review, rating=rating, property=properties)
        rev.save()
        return redirect(properties)


def blog_post(request, blog_id):
    blog_item = Blog.objects.get(id=blog_id)
    blogs = Blog.objects.all()
    categ = Properties.objects.values('category').annotate(Count('id'))
    return render(request, 'estate/blog-single.html',{
        'blog' : blog_item,
        "blogs" : blogs,
        'comments' : Comment.objects.filter(blog=blog_id),
        'cat' : categ
    })


def comments(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        comment = Comment.objects.create(name=name, blog=blog, email=email, message=message)
        comment.save()
        return redirect(blog)

def cat_search(request, category):
    properties = Properties.objects.filter(category=category)
    return render(request, 'estate/properties.html',{
        'prop' : properties
    })

def property_search(request, location):
    properties = Properties.objects.filter(location=location)
    return render(request, 'estate/properties.html', {
        'prop' : properties
    })

def agent_search(request, agent):
    properties = Properties.objects.filter(agent=agent)
    return render(request, 'estate/properties.html',{
        'prop' : properties
    })