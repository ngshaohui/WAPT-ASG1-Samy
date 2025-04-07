import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from polls.models import Friendship, Profile


@login_required
def view_profile(request, slug):
    friends = Friendship.objects.filter(user1=slug)
    profile = Profile.objects.get(owner=slug)
    return render(request, 'profile.html', {
        'username': slug,
        'friends': friends,
        'content': profile.content,
    })


@login_required
def update_profile(request):
    request_body = request.body.decode('utf-8')
    json_obj: dict = json.loads(request_body)
    username = request.user.username
    try:
        content = json_obj["content"]
    except KeyError as err:
        return HttpResponseBadRequest(f'Missing value {err}')

    Profile.objects.filter(owner=username).update(content=content)
    return JsonResponse({"success": True})
