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
				BucketlistFactory.Item.create(data)
				.$promise.then(
					function (response) {
						$scope.bucketlist = BucketlistFactory.Bucketlist.getOne({buck_id: $routeParams.buckId});
						var $toastContent = $('<strong style="color: #4db6ac;">Bucketlist created successfully.</strong>');
						Materialize.toast($toastContent, 5000);
						$scope.new_item_name = "";
						$scope.new_item_status = "";
					},
					function (error) {
						var $toastContent = $('<strong style="color: #f44336;">Error Creating bucketlist.</strong>');
						Materialize.toast($toastContent, 5000);
					}
				);
			}
			else {
				var $toastContent = $('<strong style="color: #f44336;">Item name not provided.</strong>');
				Materialize.toast($toastContent, 5000);
			}

		};

		$scope.editItem = function(buck_id, item_id) {
			$window.location.href = "#bucketlist/" + buck_id + "/edit/" + item_id + "/";
		}

		$scope.deleteItem = function (item_id) {
			var conf = confirm('Proceed and delete?');

			if (conf) {
				var data = {
					buck_id: $routeParams.buckId,
					item_id: item_id
				};
				BucketlistFactory.ItemDetail.deleteItem(data)
				.$promise.then(
					function (response) {
						var $toastContent = $('<strong style="color: #4db6ac;">Bucketlist successfully deleted.</strong>');
						Materialize.toast($toastContent, 5000);
						$scope.bucketlist = BucketlistFactory.Bucketlist.getOne({buck_id: $routeParams.buckId});
					}, function (error) {
						var $toastContent = $('<strong style="color: #f44336;">Bucketlist not edited.</strong>');
						Materialize.toast($toastContent, 5000);
					}
				);
			}

		}

	}
]);