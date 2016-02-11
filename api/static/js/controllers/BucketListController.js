BucketlistApp.controller('BucketlistController',
	['$scope', '$window', 'BucketlistFactory', '$cookies',
	function ($scope, $window, BucketlistFactory, $cookies) {
		var nextPage = 1, pages = 1, itemsPerPage = 20;

		var pageRequested = function (pageClicked) {
			nextPage = pageClicked;
			$scope.currentpage = pageClicked;

			BucketlistFactory.Bucketlist.getAll({limit: itemsPerPage, page: pageClicked}).$promise.then(
				function (response) {
					$scope.bucketlists = response;
				},
				function (error) {

				}
			);
		};

		$scope.setpage = function(currentpage){
			pageRequested(currentpage);
		};

		$scope.rightChevron = function () {
			nextPage += 1;
			if ( nextPage <= pages) {
				pageRequested(nextPage);
			}
		};

		$scope.leftChevron = function () {
			if ( (nextPage - 1) >= 1) {
				nextPage -= 1;
				pageRequested(nextPage);
			}
		};

		$scope.loadBucketlists = function (eventObj) {

			if ( typeof($scope.custom_page_size) === 'undefined') {
				itemsPerPage = 20;
			} else {
				itemsPerPage = $scope.custom_page_size;
			}

			// if the enter key has been pressed, reload the page
			if (eventObj === 'initializer' || eventObj.keyCode === 13) {
				if (itemsPerPage < 1) {
					// page size should not be less than 1 (obviously)
					itemsPerPage = 1;
				} else if (itemsPerPage > 100) {
					// page size should be at 100 max
					itemsPerPage = 100;
				}

				BucketlistFactory.Bucketlist.getAll({limit: itemsPerPage}).$promise.then(
					function (response) {
						$scope.bucketlists = response;
						if (typeof(response.results) === 'object') {
							if ($scope.bucketlists.results.length > 0) {
								$scope.showBucketlist = true;
								$scope.showNTSH = false;

								var blCount = response.count;
								$scope.pages = new Array(Math.ceil(blCount/itemsPerPage));
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
			}
		};
		// load the page with default page size 20
		$scope.loadBucketlists('initializer');

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
		};

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
		};

		$scope.del = function (buck_id) {
			var data = {
				buck_id: buck_id
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
					BucketlistFactory.Bucketlist.deleteBucket(data).$promise.then(
						function (response) {
							swal("Deleted!", "Bucketlist " + data.buck_id + " has been deleted.", "success");
						},
						function (error) {
							console.log(error);
							if (error.status === 403) {
								sweetAlert("Oops...", "You are not authorized to delete this bucketlist", "error");
							} else {
								sweetAlert("Oops...", error.statusText, "error");
							}

						}
					);

				}
			);
		};

		$scope.viewItems = function(buck_id) {
			$window.location.href = "#bucketlist/" + buck_id + "/";
		};

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

		};
	}
]);
