from django.conf.urls import url, include

from rest_framework_nested import routers

from .viewsets import BucketListViewSet, ItemViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(r'bucketlists', BucketListViewSet)
router.register(r'users', UserViewSet)

bucket_router = routers.NestedSimpleRouter(
	router,
	r'bucketlists',
	lookup='bucketlist'
)
bucket_router.register(r'items', ItemViewSet, base_name='bucketlist-items')

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^', include(bucket_router.urls)),
]
