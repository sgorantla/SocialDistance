__author__ = 'sgorantla'
from django.http import HttpResponse
from models import Poll
from models import SocialUser
from django.template import Context, loader
from django.http import Http404
from django.shortcuts import render_to_response
from urllib2 import urlopen
from json import loads
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
        })
    return HttpResponse(t.render(c))

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('polls/detail.html', {'poll': p})


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

def new_distance(request):
    return render_to_response('social_users/new_distance.html', {})

def social_users(request):
    social_user_list = SocialUser.objects.all()
    t = loader.get_template('social_users/user_list.html')
    print( social_user_list)
    c = Context({
        'social_user_list': social_user_list
    })
    return HttpResponse(t.render(c))

def auth_callback(request):
    access_token = request.GET.get('access_token', None)
    if access_token is None:
        code = request.GET.get('code')
        url = "https://graph.facebook.com/oauth/access_token?client_id=349761381783116&" \
              "redirect_uri=http://localhost:3000/auth_callback&" \
              "client_secret=da240fd7d77a5afb900372791568a396&" \
              "code="+code+"&response_type=token"
        token_string = urlopen(url).read()

        access_token = token_string[13 : token_string.find("&expires=")]

        file = urlopen("https://graph.facebook.com/me?access_token="+access_token).read()
        json = loads(file)

        su = SocialUser(name = json['name'], email = json['email'], access_token = access_token, account_id = json['id'], created_date = datetime.now(), updated_date =  datetime.now())
        su.save()

        t = loader.get_template('social_users/auth_callback.html')
        c = Context({
        'code': code,
        "access_token": access_token
        })
        return HttpResponse(t.render(c))

found_names = []
path_names = []

@csrf_exempt
def find_distance(request):
    count = 0
    global path_names
    global found_names
    path_names = []
    found_names = []

    start_name = request.POST['start_name']
    end_name = request.POST['end_name']
    find_friend(start_name, end_name)
    print path_names
    return render_to_response('social_users/new_distance.html', {})


def find_friend(start_name, name_to_find):
    if start_name not in found_names:
        found_names.append(start_name)
        path_names.append(start_name)

        if start_name.lower() == name_to_find.lower():
            return True
        users = SocialUser.objects.filter(name = start_name)
        su = None
        if len(users) > 0:
            su = users[0]
        if su is not None :
            url = "https://graph.facebook.com/me/friends?access_token="+su.access_token
            json_content = loads(urlopen(url).read())
            for friend in json_content['data']:
                friend_name = friend['name']
                if friend_name.lower() != start_name.lower():
                    if find_friend(friend_name, name_to_find):
                        return True

        path_names.pop()

        return False



