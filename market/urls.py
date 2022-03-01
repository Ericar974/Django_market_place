from django.urls import URLPattern, path
from . import views

app_name ='market'
urlpatterns = [
    path('', views.TestList.as_view(), name="index"),
    #path('<int:test_id>', views.details, name ='detail'),
    #path('<int:test_id>/results', views.result, name ='result'),
    #path('<int:test_id>', views.vote, name ='vote'),
    path('add', views.edit, name='add'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>', views.detail, name='detail'),
]