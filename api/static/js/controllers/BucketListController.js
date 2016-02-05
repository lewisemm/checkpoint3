BucketlistApp.controller('BucketlistController',
	['$scope', '$window', 'BucketlistFactory', '$cookies',
	function ($scope, $window, BucketlistFactory, $cookies) {
		var nextPage = 1, pages = 1;

		var pageRequested = function (pageClicked) {
			nextPage = pageClicked;
			$scope.currentpage = pageClicked;

			BucketlistFactory.Bucketlist.getAll({page:pageClicked}).$promise.then(
				function (response) {
					$scope.bucketlists = response;
				},
				function (error) {

				}
			);
		};

		$scope.setpage = function(currentpage){
			pageRequested(currentpage);
		}

		$scope.rightChevron = function () {
			nextPage += 1;
			if ( nextPage <= pages) {
				pageRequested(nextPage);
			}
		}

		$scope.leftChevron = function () {
			if ( (nextPage - 1) >= 1) {
				nextPage -= 1;
				pageRequested(nextPage);
			}
		}

		BucketlistFactory.Bucketlist.getAll().$promise.then(
			function (response) {
				$scope.bucketlists = response;
				if (typeof(response.results) === 'object') {
					if ($scope.bucketlists.results.length > 0) {
						$scope.showBucketlist = true;
						$scope.showNTSH = false;

						var blCount = response.count;
						$scope.pages = new Array(Math.ceil(blCount/2));
						pages = $scope.pages.length;

					} else {
						$scope.showBucketlist = false;
						$scope.showNTSH = true;
					}
				}

			},
			function (error) {
				console.log(error);
			}
		);

		// if ($scope.bucketlists.next) {
 	// 		$scope.nextPage = $scope.bucketlists.next;
		// }
		// if ($scope.bucketlists.previous) {
		// 	$scope.prevPage = $scope.bucketlists.previous;
		// }

		$scope.edit = function(buck_id) {
			var new_name = prompt('New bucketlist name');

			if (new_name) {
				var data = {
					buck_id: buck_id,
					name: new_name
				};
				BucketlistFactory.Bucketlist.edit(data);
				$scope.bucketlists = BucketlistFactory.Bucketlist.getAll();
				var $toastContent = $('<strong style="color: #4db6ac;">Bucketlist successfully edited.</strong>');
				Materialize.toast($toastContent, 5000);

				//$window.location.href = "#bucketlist/";
			} else {
				var $toastContent = $('<strong style="color: #f44336;">Bucketlist not edited.</strong>');
				Materialize.toast($toastContent, 5000);
			}
		}

		$scope.addBucketlist = function (data) {
			var data = {
				name: $scope.bucketlist_name
			}
			if (data.name != null) {
				BucketlistFactory.Bucketlist.create(data)
				.$promise.then(
					function (response) {
						$scope.bucketlists = BucketlistFactory.Bucketlist.getAll();
						var $toastContent = $('<strong style="color: #4db6ac;">' + response.message + '</strong>');
						Materialize.toast($toastContent, 5000);
						$scope.bucketlist_name = "";
					}, function (error) {
						var $toastContent = $('<strong style="color: #f44336;">Error Creating bucketlist.</strong>');
						Materialize.toast($toastContent, 5000);
					});
			}
			else {
				var $toastContent = $('<strong style="color: #f44336;">Bucketlist name missing.</strong>');
				Materialize.toast($toastContent, 5000);
			}
		}

		$scope.del = function (buck_id) {
			var conf = confirm('Are you sure you want to delete?');

			if (conf) {
				var data = {
					buck_id: buck_id
				};
				BucketlistFactory.Bucketlist.deleteBucket(data);
				$window.location.href = "#bucketlist/";
				var $toastContent = $('<strong style="color: #f44336;">Bucketlist successfully deleted.</strong>');
				Materialize.toast($toastContent, 5000);
			}
			else {
				var $toastContent = $('<strong style="color: #4db6ac;">Bucketlist not deleted.</strong>');
				Materialize.toast($toastContent, 5000);
			}

		}

		$scope.viewItems = function(buck_id) {
			$window.location.href = "#bucketlist/" + buck_id + "/";
		}

		$scope.itemsDone = function (bucketlist) {
			if (bucketlist.item) {
				var allItems = 0;
				var done = 0;
				if (bucketlist.item.length > 0) {
					allItems = bucketlist.item.length;

					for (i = 0; i < allItems; i++) {
						if (bucketlist.item[i].done) {
							done += 1;
						}
					}
				}
				$scope.allItems = allItems;
				// $scope.bucketlist.buck_id = done;
			}

		}
	}
]);