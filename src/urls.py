from django.urls import path
from . import views
from .views import show_item

urlpatterns = [
    path('show_data/', views.show_data, name='show_data'),
    path('submit_data/', views.submit_data, name='submit_data'),
    path('item/<int:item_id>/',views.show_item, name='show_item')
]