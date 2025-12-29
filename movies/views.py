from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from movies.models import  Faviorites, Movies, Reviews,Contact
from django.contrib.auth.decorators import login_required
from accounts.models import Register_user
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    movies=Movies.objects.all()
    # print(movies[0].poster)
    if request.GET.get('search'):
       movies=movies.filter(title__icontains=request.GET.get('search'))
    if request.GET.get('sort_by'):
        if request.GET.get('sort_by')=='sort_low':
            movies=movies.order_by('rating')
        elif request.GET.get('sort_by')=='sort_high':
            movies=movies.order_by('-rating')

    
    context={
        'movies':movies[:50],
        
    }
    
    return render(request,'index.html',context)

@login_required(login_url='login_view')
def new_movies(request):
    movies=Movies.objects.all().order_by('-relese_date')
    if request.GET.get('search'):
        movies=movies.filter(hero_name__icontains=request.GET.get('search'))
    context={
        'movies':movies,     
    }
    return render(request,'new_movies.html',context)

def about(request):
    return render(request,'About.html')
@login_required(login_url='login_view')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        problem=request.POST.get('problem')
        Contact.objects.create(
            name=name,
            email=email,
            problem=problem
        )
        messages.success(request,'We reach you soon...')
        return redirect('contact')

    return render(request,'Contact.html')

def help(request):
    return render(request,'Help.html')

@login_required(login_url='login_view')
def detail_view(request,id):
    movie=Movies.objects.get(id=id)
    if request.method=='POST':
        person_name=request.POST.get('person_name')
        comment=request.POST.get('comment')
    # print(person_name,comment)
        review=Reviews.objects.create(
            person_name=person_name,
            comment=comment,
            movie_name=movie
        )
        messages.success(request,"Comment Successfully")
        return redirect('detail_view',id=id)
    movie = Movies.objects.get(id=id)
    is_faviorite=Faviorites.objects.filter(
        user=request.user,
        movie=movie
    ).exists()
    
    
    context={
        'movie':movie,
        'reviews':movie.movie_name.all(),
        'is_faviorite':is_faviorite,
    }
    return render(request,'detail_page.html',context)
@login_required(login_url='login_view')
def profile_view(request):
    return render(request,'profile.html')
@login_required(login_url='login_view')
def edit_profile(request,id):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')

        user=Register_user.objects.get(id=id)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        messages.success(request,'profile update succesfully')
        return redirect('edit_profile',id=id)

    return render(request,'edit_profile.html')
@login_required(login_url='login_view')
def faviorites(request):
    # user=User.objects.get(id=request.user.id)
    
    faviorites=Faviorites.objects.filter(user=request.user).select_related('movie')
    print(faviorites)
    context={
        'faviorites':faviorites
    }
    return render(request,'faviorites.html',context)
@login_required(login_url='login_view')
def add_to_faviorites(request,id):
    user=User.objects.get(id=request.user.id) #it used because we have two tables User and Register_user but we use User because request.user use the User table
    movie=Movies.objects.get(id=id)
    
    faviorite,created=Faviorites.objects.get_or_create(
        user=user,
        movie=movie
    )
    if not created:
        faviorite.delete()
    return redirect('detail_view', id=id)





