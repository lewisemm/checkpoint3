from django.conf.urls import url, include

from rest_framework_nested import routers as nested_router

from .viewsets import BucketListViewSet, ItemViewSet, UserViewSet
from api import views

router = nested_router.SimpleRouter()
router.register(r'bucketlists', BucketListViewSet)
router.register(r'users', UserViewSet)

bucket_router = nested_router.NestedSimpleRouter(
	router,
	r'bucketlists',
	lookup='bucketlist'
)
bucket_router.register(r'items', ItemViewSet, base_name='bucketlist-items')

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^', include(bucket_router.urls)),
	url(r'^$', views.index, name='index'),
	url(r'^auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api/docs/', include('rest_framework_swagger.urls')),
]
