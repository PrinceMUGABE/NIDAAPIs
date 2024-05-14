from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('citizen', views.RwandanViewSet, basename='rwandan')

urlpatterns = [
    path('', include(router.urls)),  # Include the URLs from the router
    path('all/', views.RwandanViewSet.as_view({'get': 'list_all'}), name='rwandan-list-all'),
    path('create/', views.RwandanViewSet.as_view({'post': 'create'}), name='rwandan-create'),
    path('update/<int:pk>/', views.RwandanViewSet.as_view({'put': 'update_by_id'}), name='rwandan-update-by-id'),
    path('update_by_identity_no/<str:identity_no>/', views.RwandanViewSet.as_view({'put': 'update_by_identity_no'}), name='rwandan-update-by-identity-no'),
    path('delete/<int:pk>/', views.RwandanViewSet.as_view({'delete': 'delete_by_id'}), name='rwandan-delete-by-id'),
    path('delete_by_identity_no/<str:identity_no>/', views.RwandanViewSet.as_view({'delete': 'delete_by_identity_no'}), name='rwandan-delete-by-identity-no'),
    path('retrieve/<int:pk>/', views.RwandanViewSet.as_view({'get': 'retrieve_by_id'}), name='rwandan-retrieve-by-id'),
    path('retrieve_by_identity_no/<str:identity_no>/', views.RwandanViewSet.as_view({'get': 'retrieve_by_identity_no'}), name='rwandan-retrieve-by-identity-no'),
]
