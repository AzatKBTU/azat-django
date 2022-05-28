from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import ListBook, DetailBook, DetailJournal, ListJournal

urlpatterns = [
    path('<int:pk>/', DetailBook.as_view()),
    path('', ListBook.as_view()),
    path('<int:pk>/', DetailJournal.as_view()),
    path('', ListJournal.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]
