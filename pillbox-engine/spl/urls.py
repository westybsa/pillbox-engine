from rest_framework.routers import DefaultRouter
from spl import views

router = DefaultRouter()
router.register(r'sync', views.SyncSpl, base_name='sync')
router.register(r'download', views.DownloadViewSet, base_name='download')
urlpatterns = router.urls
