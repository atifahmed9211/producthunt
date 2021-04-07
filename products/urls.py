from django.urls import path
from . import views
urlpatterns=[
    path('create/',views.create,name='create'),
    path('<int:product_id>/',views.productDetail,name='productDetail'),
    path('<int:product_id>/upvote',views.upvote,name="upvote")
 ]
