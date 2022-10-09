from django.urls import path
from .views import (
    index, 
    car_detail,
    category_filter,
    ProductCreateView, 
    ProductUpdateView,
    ProductDeleteView,
)

app_name = "main"

urlpatterns = [
    path('post/<int:pk>delete',  ProductDeleteView.as_view() , name='post_delete'),
    path('post/<int:pk>edit',  ProductUpdateView.as_view(), name='post_edit'),
    path('post/new/', ProductCreateView.as_view(), name= 'post_new' ),
    path('', index, name="index" ),
    path('product/<int:car_detail>',  car_detail ,name='car_detail'),
    path('category/<int:category_id>',category_filter,   name= 'category_filter'),

]