
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'booking', views.BookingViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view())
]
