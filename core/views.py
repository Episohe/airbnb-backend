from django.core import serializers
from django.http import HttpResponse

from rooms.models import Room


# Create your views here.


def list_rooms(request):
    # rooms = Room.objects.all()
    # rooms_json = []
    # for room in rooms:
    #     rooms_json.append(json.dumps(room))
    # response = HttpResponse(content=rooms_json)

    data = serializers.serialize("json", Room.objects.all())
    response = HttpResponse(content=data)
    return response
