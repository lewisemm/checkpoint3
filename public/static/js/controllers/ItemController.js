BucketlistApp.controller('ItemController',
	['$scope', 'BucketlistFactory', '$routeParams', '$window', '$rootScope',
	function ($scope, BucketlistFactory, $routeParams, $window, $rootScope) {
		$rootScope.loginPage=false;
		var data = {
			buck_id: $routeParams.buckId,
			item_id: $routeParams.itemId
		};
		BucketlistFactory.ItemDetail.getOne(data).$promise.then(
			function (response) {
				$scope.update_name = response.name;
			},
			function (error) {
				console.log(error);
			}
		);

		// for the breadcrumb
		BucketlistFactory.Bucketlist.getOne(data).$promise.then(
			function (response) {
				$scope.bucketlist = response;
			},
			function (error) {
				console.log(error);
			}
		);

		$scope.updateItem = function () {
			var data = {
					buck_id: $routeParams.buckId,
					item_id: $routeParams.itemId
			};
			data.name = $scope.update_name;

			if ($scope.update_done) {
				data.done = $scope.update_done;
			} else {
				data.done = false;
			}

			BucketlistFactory.ItemDetail.edit(data).$promise.then(
				function (response) {
					var $toastContent = $('<strong style="color: #4db6ac;">Item updated.</strong>');
					Materialize.toast($toastContent, 5000);
					$window.location.href = "#bucketlist/" + $routeParams.buckId + "/";
				},
				function (error) {
					var $toastContent = $('<strong style="color: #f44336;">Failed to update item.</strong>');
					Materialize.toast($toastContent, 5000);
				}
			);
		};

		$scope.dismiss = function () {
			$window.location.href = "#bucketlist/" + $routeParams.buckId + "/";
		}
	}
]);