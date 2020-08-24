from django.urls import path

from .views import (ProductListView,
                    ProductDetailView,
                    ProductFeaturedDetailView,
                    ProductFeaturedListView,
                    product_list_view,
                    product_detail_view,
                    ProductDetailSlugView
                    )


urlpatterns = [
    path("", ProductListView.as_view()),
    path("fbv/", product_list_view),
    path("<int:pk>/", ProductDetailView.as_view()),
    path('fbv/<int:pk>/', product_detail_view),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    path('slug/', ProductDetailSlugView.as_view())
]