from django.urls import path
from . import views
app_name = "myapp"
urlpatterns = [
    path('events/',views.event_list,name="events"),
    path('events/<int:id>',views.event_detail,name="event_detail"),
    path('events/create',views.create_event,name="create_event"),
    path('events/edit/<int:id>',views.edit_event,name="edit_event"),
    path('events/delete/<int:id>',views.delete_event,name="delete_event"),
    path('dashboard/',views.dashboard,name="dashboard"),

]