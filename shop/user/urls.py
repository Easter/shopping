from django.urls import path,include
from . import views
import shopping

app_name = "user"

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('login/logon/commodities/',views.logon,name="logon"),
    path('apply/',views.apply,name="apply"),
    path('<int:pk>/search',views.search,name="search"),
    path('<int:user_pk>/<int:commodity_pk>/add-to-commodities',views.add,name="add_commodity"),
    path('add/',views.number_add,name="number_add"),
    path('sub/',views.number_sub,name="number_sub"),
    # path('test/',views.test,name="test")
]