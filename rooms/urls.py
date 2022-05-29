from django.urls import path

from rooms import views

app_name = "rooms"

urlpatterns = [
    # path("", views.rooms_view),
    # path("<int:pk>/", views.SeeRoomView.as_view()),
    path("", views.RoomsView.as_view()),
    path("<int:pk>/", views.RoomView.as_view()),
]
