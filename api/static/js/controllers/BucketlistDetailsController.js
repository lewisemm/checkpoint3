BucketlistApp.controller('BucketlistDetailsController',
	['$scope', 'BucketlistFactory', '$routeParams', '$window', '$filter',
	function ($scope, BucketlistFactory, $routeParams, $window, $filter) {
		var data = {
			buck_id: $routeParams.buckId
		};

		BucketlistFactory.Bucketlist.getOne(data).$promise.then(
			function (response) {
				$scope.bucketlist = response;
				if (typeof($scope.bucketlist.item) === 'object') {
					if ($scope.bucketlist.item.length > 0) {
						$scope.showBucketlistItems =true;
						$scope.showNTSHBucketlist = false;
					} else {
						$scope.showBucketlistItems =false;
						$scope.showNTSHBucketlist = true;
					}
				}
			},
			function (error) {
				console.log(error);
			}
		);

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
						$scope.bucketlist = BucketlistFactory.Bucketlist.getOne({buck_id: data.buck_id});
						var $toastContent = $('<strong style="color: #4db6ac;">Bucketlist item created successfully.</strong>');
						Materialize.toast($toastContent, 5000);
						$scope.new_item_name = "";
						$scope.new_item_status = false;

						if ($scope.showNTSHBucketlist) {
							$scope.showNTSHBucketlist = false;
							$scope.showBucketlistItems = true;
						}
					},
					function (error) {
						console.log(error);
						var $toastContent = $('<strong style="color: #f44336;">Error creating bucketlist item.</strong>');
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
		};

		$scope.clickedAsDone = function (item_id) {
			// retrieve the item object with id of "item_id" from $scope.bucketlist
			var itemClickedArray = $filter('filter')($scope.bucketlist.item, {item_id: item_id}, function (actual, expected) {
				return angular.equals(actual, expected);
			});
			// only allow updates for items whose done status is false
			// when the user clicks on the checkbox
			var itemClicked = itemClickedArray[0];

			if (!itemClicked.done) {
				//
				swal(
					{
						title: "Proceed to mark item as 'done'?",
						text: "You are about to mark this item as done!",
						type: "warning",
						showCancelButton: true,
						confirmButtonColor: "#f44336",
						confirmButtonText: "Yes, update item!",
						closeOnConfirm: false
					},
					function () {
						var data = {
							buck_id: $routeParams.buckId,
							item_id: item_id,
							done: true,
							name: itemClicked.name
						};
						BucketlistFactory.ItemDetail.edit(data).$promise.then(
							function (response) {
								console.log(response);
								swal("Item status updated!", "The item has now been marked as done!", "success");
							},
							function (error) {
								console.log(error);
								swal("Oops...!", "Something went wrong when updating the done status", "error");
							}
						);
					}
				);

			} else {
				// when the done status was already true, tell the user to press the
				// edit button where they will be redirected to edit page
				swal("Item already marked as done!", "Please use the edit button if you still wish to change something.");
			}
			BucketlistFactory.Bucketlist.getOne({buck_id: $routeParams.buckId}).$promise.then(
				function (response) {
					$scope.bucketlist = response;
				},
				function (error) {

				}
			);

		};

		$scope.deleteItem = function (item_id) {
			var data = {
				buck_id: $routeParams.buckId,
				item_id: item_id
			};
			swal(
				{
					title: "Are you sure?",
					text: "You will not be able to undo this operation!",
					type: "warning",
					showCancelButton: true,
					confirmButtonColor: "#f44336",
					confirmButtonText: "Yes, delete it!",
					closeOnConfirm: false
				},
				function () {
					BucketlistFactory.ItemDetail.deleteItem(data)
					.$promise.then(
						function (response) {
							swal("Deleted!", "Item " + data.item_id + " in Bucketlist " + data.buck_id + " has been deleted.", "success");
							$scope.bucketlist = BucketlistFactory.Bucketlist.getOne({buck_id: data.buck_id});
						}, function (error) {

						}
					);
				}
			);
		};
	}
]);