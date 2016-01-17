BucketListApp.controller('BucketListController', ['$scope', 'bucketlists', function($scope, bucketlists) {
	$scope.age = 10;
	bucketlists.success(function(data) {
		$scope.bucketlists = data;
		// console.log($age);
	});
}]);