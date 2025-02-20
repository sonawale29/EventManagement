from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUser, CreateEvent, EventList, PurchaseTicketView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('events/', EventList.as_view(), name='event_list'),
    path('events/create/', CreateEvent.as_view(), name='event_create'),
    path('events/<int:event_id>/purchase/', PurchaseTicketView.as_view(), name='purchase_ticket'),
]
