from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='product_list'),
    path('create/', views.CreateView.as_view(), name='producto_create'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='producto_update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='producto_delete'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='producto_detail'),
]
