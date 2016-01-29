BucketlistApp.controller('ItemController',
	['$scope', 'BucketlistFactory', '$routeParams',
	function ($scope, BucketlistFactory, $routeParams) {
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

			console.log(data);
			BucketlistFactory.ItemDetail.edit(data);
		};
	}
]);