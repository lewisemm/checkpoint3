BucketlistApp.controller('BucketlistController', ['$scope', '$window', 'BucketlistFactory',
	function ($scope, $window, BucketlistFactory) {
		$scope.bucketlists = BucketlistFactory.getAll();
		$scope.view_items = function (buck_id) {
			$window.location.href = "#bucketlist/" + buck_id + "/";
		}
	}
]);