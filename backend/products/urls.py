from django.urls import path
from .views import PrdouctDetailAPIView

urlpatterns = [
    path("<int:pk>/", PrdouctDetailAPIView.as_view())
]
