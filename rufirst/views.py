# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.template import Context

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from models import Post

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
    if request.method == 'GET':
        return render(request, 'register.html')


    new_username = request.POST['username']
    new_password = request.POST['password']
    new_confirm = request.POST['confirmpassword']


    # print testUser.size()
    if User.objects.filter(username=new_username) or (not(new_password==new_confirm)):
        print "----------"
        return render(request, 'register.html')
    # Creates the new user from the valid form data
    new_user =  User.objects.create_user(username=new_username,password= new_password,\
                    first_name=request.POST['firstname'] ,last_name=request.POST['lastname'])

    new_user.save()

    # authenticate() will check the backend, and return user object
    #  when being verified, and return null when not
    new_user = authenticate(username=new_username, password = new_password, )

    login(request, new_user)

    return redirect('global')

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
    return render(request,'profile.html',{'user':thisuser, 'items':items})

# @login_required()
# def globalstream(request,username):
#     items = Post.objects.all().order_by('-date')
#     return render(request,'global.html',{'items':items})