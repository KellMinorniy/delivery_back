from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import add_to_cart


urlpatterns = [
    path('', views.index),
    path('add-to-cart/<int:menu_item_id>/', views.add_to_cart, name='add-to-cart'),
    path('', views.cart, name='cart'),
    path('cart/remove/<int:menu_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('order/', views.order, name='order'),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('finish/', views.finish, name='finish')
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)