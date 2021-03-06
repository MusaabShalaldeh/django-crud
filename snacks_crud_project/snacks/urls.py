from django.urls import path
from .views import (
                    SnackListView,
                    SnackDetailView,
                    SnackCreateView,
                    SnackUpdateView,
                    SnackDeleteView,
)

urlpatterns = [
    path('', SnackListView.as_view(), name="snacks"),
    path('<int:pk>/snack/',SnackDetailView.as_view(), name="snack_detail"),
    path('snack_create/',SnackCreateView.as_view(), name="snack_create"),
    path('<int:pk>/snack_update/',SnackUpdateView.as_view(), name="snack_update"),
    path('<int:pk>/snack_delete/',SnackDeleteView.as_view(), name="snack_delete"),
]
