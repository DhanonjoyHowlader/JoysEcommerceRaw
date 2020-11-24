"""JoysEcommerceRaw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ProductManagement import views as product_views
from ProductManagement import views as slider_views
from UserManagement import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', product_views.showProducts, name='products_list'),

    path('products/<int:product_id>', product_views.showDetails, name='detail_view'),

    path('cart/', product_views.view_cart, name='cart'),

    path('updatecart/<int:product_id>', product_views.update_cart, name='update-cart'),

    path('deletefromcart/<int:product_id>', product_views.delete_from_cart, name='delete-from-cart'),

    path('myorders/', product_views.my_orders, name='my-orders'),

    path('orderproduct/<int:product_id>', product_views.make_order, name='order-product'),

    path('bkash/<int:product_id>', product_views.bkash_order, name='bkash-order-product'),

    path('review/<int:product_id>', product_views.review_after_complete, name='review'),

    path('signup/', user_views.register, name='register'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('profile/', user_views.ViewProfile, name='show_profile'),

    path('createprofile/', user_views.CreateProfile, name='create_profile'),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
