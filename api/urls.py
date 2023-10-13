from django.urls import path
from .views import BookListCreateView,MyModelDetailView

urlpatterns = [
    path('book/', BookListCreateView.as_view(), name='yourmodel-list-create'),
    path('book/<int:pk>/', MyModelDetailView.as_view(), name='mymodel-detail'),
]
