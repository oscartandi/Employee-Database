from employeeapi.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee',EmployeeViewset)

router.urls

#localhost:p/api/
#Get,POST, UPDATE, DELETE
#list, retrive



