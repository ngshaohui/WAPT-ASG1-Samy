from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, JsonResponse
from polls.models import Friendship, Profile
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import json


def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})


USERS = [
    'alice',
    'bob',
    'charlie',
    'malory',
    'eve',
    'samy',
]


def init_user(username: str):
    User.objects.create_user(username=username,
                             is_staff=True,
                             is_superuser=True,
                             password=username)
    Profile.objects.create(owner=username,
                           content=f'I am {username}')


def seed():
    User.objects.all().delete()
    Profile.objects.all().delete()
    Friendship.objects.all().delete()
    for user in USERS:
        init_user(user)
    return JsonResponse({"success": True})


def reset(request):
    if request.method == "POST":
        confirm = request.POST.get('confirm')

        if confirm != "confirm":
            return JsonResponse({"success": False})

        seed()
        return redirect("/")
    else:
        return render(request, "reset.html")


@login_required
def add_friend(request):
    username = request.user.username
    request_body = request.body.decode('utf-8')
    json_obj: dict = json.loads(request_body)
    try:
        user_to_add = json_obj["friend"]
    except KeyError as err:
        return HttpResponseBadRequest(f'Missing value {err}')

    if username == user_to_add:
        return HttpResponseBadRequest("Unable to add yourself as a friend")

    exists = Friendship.objects.filter(
        user1=username, user2=user_to_add).exists()

    if exists:
        return HttpResponseBadRequest(f"User {user_to_add} already exists as a friend")

    Friendship.objects.create(user1=username,
                              user2=user_to_add,
                              is_pending=False)
    Friendship.objects.create(user1=user_to_add,
                              user2=username,
                              is_pending=False)
    return JsonResponse({"success": True})
