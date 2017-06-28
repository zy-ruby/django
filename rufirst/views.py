# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.template import Context

from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from mimetypes import guess_type
from models import Post
from rufirst.forms import *



from django.db import transaction

# from models import User

from django.core.urlresolvers import reverse

# Create your views here.
@login_required()
def home(request):
    # post = Post(content='nihao',user = request.user)
    # post.save()
    items = Post.objects.all().order_by('-date')
    print "--------- "
    # print items
    # print len(items)
    print "--------- "
    username = request.user.username
    # print '----username:------'
    # print username

    return render(request, 'global.html', {'items': items,'username':username})
    # return render(request, 'global.html', {'username': username})


# def login(request):
#
#     if request.method == 'GET':
#         return render(request,'ruru.html')
#
#     username = request.POST['username']
#     password = request.POST['password']
#
#     userdb = User.objects.get(username=username)
#     if userdb == None:
#         print "no user"
#     else:
#         print userdb
#         usernamedb = userdb.username
#         passworddb = userdb.password
#
#         # items = Post.objects.all().order_by('-date')
#         if(password == passworddb ):
#             return redirect('global', username)
#             # render(request,'global.html',{'username':usernamedb,'items':items})
#
#
#     return render(request, 'ruru.html')


def register(request):
    # Just display the registration form if this is a GET request
    context = {}

    if request.method == 'GET':
        context['form'] = RegisterForm()
        return render(request, 'register.html',context)

    new_user = User()
    form = RegisterForm(request.POST, instance=new_user)


    if not form.is_valid():
        print  "--------- form not valid"
        context['form'] = form
        return render(request, 'register.html', context)

    print  "--------- form valid"

    form.save();
    profile = Profile()
    profile.user = new_user
    profile.save()

    login(request, new_user)

    return redirect('global')

@login_required()
def editprofile(request):

    context = {}
    thisuser = request.user
    profileEntry = get_object_or_404(Profile, user=thisuser)

    form = EditProfileForm(request.POST, request.FILES, instance=profileEntry)
    context['form'] = form

    if request.method == 'GET':

        return render(request, 'editprofile.html', context)


    if not form.is_valid():
        print "edit profile form not valid"

        return render(request,'editprofile.html',context)

    form.save()

    return redirect('global')

@login_required()
def photo(request, username):
    thisuser = User.objects.get(username=username)
    profile = get_object_or_404(Profile, user = thisuser)
    if not profile.photo:
        # raise Http404
        print "======default===="
        return HttpResponse( "{% static 'default.jpg' %}" )
    print "======not default===="
    content_type = guess_type(profile.photo.name)
    return HttpResponse(profile.photo, content_type=content_type)

@login_required()
def newpost(request):
    if request.method == 'GET':
        return render(request, 'global.html')
    postcontent = request.POST.get('content', False)
    thisuser = request.user
    newpost = Post(content = postcontent, user=thisuser)

    print "======= "
    print newpost
    print "======= "

    print 'postcontent:'
    print postcontent
    print ''
    newpost.save()

    # items = Post.objects.all().order_by('-date')
    # return render(request, 'global.html',{'username':username,'items':items} )
    return redirect('global')

@login_required()
def profile(request,username):
    # user = request.user
    thisuser = User.objects.get(username=username)
    items = Post.objects.all().filter(user = thisuser).order_by('-date')

    profile = Profile.objects.get(user =thisuser)
    return render(request,'profile.html',{'user':thisuser, 'items':items, 'profile':profile})

# @login_required()
# def globalstream(request,username):
#     items = Post.objects.all().order_by('-date')
#     return render(request,'global.html',{'items':items})