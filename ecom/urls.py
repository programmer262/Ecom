from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('chekout/',views.chekout,name='chekout'),
    path('cart/',views.cart,name='cart'),
    path('view/<str:pk>',views.view,name='view'),
    path('contact/',views.contact,name='contact'),
    path('map/',views.map,name='map'),
    path('thanks/',views.thanks,name='thanks'),
    path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]