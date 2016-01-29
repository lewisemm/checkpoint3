BucketlistApp.controller('BucketlistDetailsController',
	['$scope', 'BucketlistFactory', '$routeParams', '$window',
	function ($scope, BucketlistFactory, $routeParams, $window) {
		var data = {
			buck_id: $routeParams.buckId
		};
		$scope.bucketlist = BucketlistFactory.Bucketlist.getOne(data);

		$scope.addItem = function () {
			if ($scope.new_item_name) {
				var data = {
					buck_id: $routeParams.buckId,
					name: $scope.new_item_name,
					done: $scope.new_item_status
				};
				BucketlistFactory.Item.create(data);
			}

		};

		$scope.editItem = function(buck_id, item_id) {
			$window.location.href = "#bucketlist/" + buck_id + "/edit/" + item_id + "/";
		}

		$scope.deleteItem = function (item_id) {
			var data = {
				buck_id: $routeParams.buckId,
				item_id: item_id
			};
			BucketlistFactory.ItemDetail.deleteItem(data);
		}

	}
]);