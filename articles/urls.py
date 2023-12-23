from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


app_name = "articles"
urlpatterns = [
    path('', views.articles_list, name = "list"),
    path('<slug>', views.article_detail, name = "detail")
]

