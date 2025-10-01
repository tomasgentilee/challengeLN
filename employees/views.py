from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from .models import Employee
from .serializers import EmployeeSerializer
from datetime import date
from rest_framework import status
from .automate import send_salary_report

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [filters.SearchFilter]
    search_fields = ["position", "name", "lastname"]

    # Endpoint para promedio de salarios
    @action(detail=False, methods=["get"])
    def avg_salary(self, request):
        promedio = self.get_queryset().aggregate(promedio=Avg("salary"))
        return Response(promedio)

    # Action para enviar el reporte al correo de forma manual
    @action(detail=False, methods=["get"])
    def send_report(self, request):
        try:
            send_salary_report()
            return Response({"message": "Salary report sent successfully!"})
        except Exception as e:
            return Response({"error": str(e)}, status=500)