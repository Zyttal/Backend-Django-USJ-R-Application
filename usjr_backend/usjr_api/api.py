from rest_framework import routers
from  usjr_api import views as usjr_views

router = routers.DefaultRouter()
router.register(r'colleges', usjr_views.CollegesViewSet)
router.register(r'departments', usjr_views.DepartmentsViewSet)
router.register(r'programs', usjr_views.ProgramsViewSet)
router.register(r'students', usjr_views.StudentsViewSet)