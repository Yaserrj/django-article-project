from django.shortcuts import render, redirect,get_object_or_404
from .models import Articleitem, Comment,contactos
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def main_Page(request):
    context = {
        'Articleitems' : Articleitem.objects.all()
    }
    
    return render(request , "index.html" , context)

def article(request):
    context = {
        'Articleitems' : Articleitem.objects.all()
    }
    if request.POST:
        search = request.POST.get("q")
        context['Articleitems']= Articleitem.objects.filter(Q(title__icontains=search) | Q(description__icontains=search)  )
        
    return render( request ,"articles.html",context)

def contact(request):
    if request.POST:
        
        fullname =  request.POST.get("name")
        emails = request.POST.get("email")
        messages_T = request.POST.get("message")
        contactos.objects.create(fname_lname=fullname, Email=emails, Message=messages_T)      
        
        messages.success(request, "✅ Your message has been sent successfully.")
        return redirect('/contact/')
    
    context = {
        'contactUs': contactos.objects.all()
    }
    
    return render (request , "contact.html",context)


def article_detail(request ,id):
    article = get_object_or_404(Articleitem,id=id)
    comments = article.comments.all().order_by('-created_at')  # فقط کامنت‌های این مقاله

    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")

        Comment.objects.create(
            article=article,
            name=name,
            text=text
        )

        messages.success(request, "✅ Your comment was submitted successfully.")
        return redirect('article_detail', id=article.id)

    context = {
        'article': article,
        'comments': comments
    }
    return render(request, "article_detail.html", context)