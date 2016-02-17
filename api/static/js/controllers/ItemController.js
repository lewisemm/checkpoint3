BucketlistApp.controller('ItemController',
	['$scope', 'BucketlistFactory', '$routeParams', '$window',
	function ($scope, BucketlistFactory, $routeParams, $window) {
		var data = {
			buck_id: $routeParams.buckId,
			item_id: $routeParams.itemId
		};
		$scope.item = BucketlistFactory.ItemDetail.getOne(data);

		$scope.updateItem = function () {
			var data = {
					buck_id: $routeParams.buckId,
					item_id: $routeParams.itemId
			};
			if ($scope.update_name) {
				data.name = $scope.update_name;
			} else {
				data.name = $scope.item.name;
			}

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