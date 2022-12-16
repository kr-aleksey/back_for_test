from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from .views import NomenclatureViewSet, WorkOrderViewSet, ProductViewSet

app_name = 'api'

v1_router = routers.DefaultRouter()
v1_router.register('nomenclatures', NomenclatureViewSet)
v1_router.register('workorders', WorkOrderViewSet)
v1_router.register(
    r'workorders/(?P<work_order_id>\d+)/products',
    ProductViewSet,
    basename='products',
)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
