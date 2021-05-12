
from django.urls import path, include
from .views import (
    CreateMaterial,
    ListMaterial,
    UpdateMaterial,
    DetailMaterial,
    DeleteMaterial,
    AdminMaterialListView
)

app_name = "materials"
urlpatterns = [
    path('create/', CreateMaterial.as_view(), name="create-material"),
    path('list/', ListMaterial.as_view(), name="list-material"),
    path('<int:pk>/detail/', DetailMaterial.as_view(), name="Detail_View"),
    path('<int:pk>/delete/', DeleteMaterial.as_view(), name="delete-material"),
    path('<int:pk>/update/', UpdateMaterial.as_view(), name="update-material"),
    path('approve/', AdminMaterialListView.as_view(), name="approve-material"),
]
