BucketListApp.factory('bucketlists', ['$http', function($http) {
	return $http.get('http://localhost:8000/bucketlists/')
	.success(function(data) {
		return data;
	})
	.error(function(data) {
		return data;
	});
}]);