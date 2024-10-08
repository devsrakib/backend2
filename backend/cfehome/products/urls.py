from django.urls import path
from . import views


urlpatterns = [
    path("", views.product_list_create_view, name="product-list"),
    path("<int:pk>/update/", views.product_update_view, name="product-edit"),
    path("<int:pk>/", views.product_details_view, name="product-detail"),
]
