from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r"empleados", EmployeeViewSet, basename="empleados")

urlpatterns = router.urls