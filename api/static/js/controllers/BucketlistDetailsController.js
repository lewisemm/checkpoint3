BucketlistApp.controller('BucketlistDetailsController',
	['$scope', 'BucketlistFactory', '$routeParams',
	function ($scope, BucketlistFactory, $routeParams) {
		var Bucketlist = BucketlistFactory.getOne($routeParams.buckId);

		Bucketlist.$promise.then(
			function (response) {
				$scope.items = response.item;
				$scope.bucketlist_name = response.name;

			},
			function (error) {
				console.log("Fail", error);
			}
		);
	}
]);