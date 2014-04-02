# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib import auth
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from blog.models import BlogPost, Comments
from blog.forms import CommentsForm

def posts(request):
    return render_to_response('posts.html', {'posts': BlogPost.objects.all(),
                                             'username': auth.get_user(request).username
                                            }
                                )

def post(request, post_id=1):
    comments_form = CommentsForm
    args = {}
    args.update(csrf(request))
    args['post'] = BlogPost.objects.get(id = post_id)
    args['comments'] = Comments.objects.filter(comments_blogpost_id = post_id)
    args['form'] = comments_form
    args['username'] = auth.get_user(request).username
    return render_to_response('post.html', args)

    ############old release###########################################################################################
    # return render_to_response('post.html', {'post': BlogPost.objects.get(id = post_id),
    #                                         'comments': Comments.objects.filter(comments_blogpost_id = post_id)
    #                                         }
    #                         )
    ##################################################################################################################

def style(request):
    return render_to_response('style.html')

def likeme(request, post_id):
    try:
        if post_id in request.COOKIES:
            redirect('/')
        else:
            post = BlogPost.objects.get(id = post_id)
            post.blogpost_likes += 1
            post.save()
            response = redirect('/')
            response.set_cookie(post_id, "likeme")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def newcomment(request, post_id):
    if request.POST and ('justamoment' not in request.session):
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_blogpost = BlogPost.objects.get(id = post_id)
            form.save()
            request.session.set_expiry(120)
            request.session['justamoment'] = True
    return redirect('/post/%s/' % post_id)

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = u"Пользователь не найден!"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')