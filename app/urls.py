from rest_framework import routers
from .views import UserViewSet, ProjectViewSet, TestSuiteViewSet, TestCaseViewSet, IssueViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'testsuites', TestSuiteViewSet)
router.register(r'testcases', TestCaseViewSet)
router.register(r'issues', IssueViewSet)