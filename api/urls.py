from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import viewsets


# create a router and register viewsets with it
router = DefaultRouter()
router.register(r'bucketlist', viewsets.BucketListViewSet)
router.register(r'item', viewsets.ItemViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(
		r'^api-auth/',
		include('rest_framework.urls', namespace='rest_framework')
	)
]
