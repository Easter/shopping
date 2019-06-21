from django.urls import path
from . import views
from user.models import User_commodity
app_name = "shopping"

urlpatterns = [
    path('user/<int:user_pk>/',views.index,name="index"),
    # path('',views.index,name="index"),
    path('user/<int:user_pk>/delete/<int:commodity_pk>/',views.delete,name="delete"),
    path('user/<int:user_pk>/deleteAll/',views.deleteAll,name="deleteAll"),
    path('admin/<int:pk>/add',views.add,name="add")
]