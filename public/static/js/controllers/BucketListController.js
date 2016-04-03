BucketlistApp.controller('BucketlistController',
	['$scope', '$window', 'BucketlistFactory', '$cookies', '$rootScope',
	function ($scope, $window, BucketlistFactory, $cookies, $rootScope) {
		$rootScope.loginPage=false;
		var nextPage = 1, pages = 1, itemsPerPage = 5;

		var pageRequested = function (pageClicked) {
			nextPage = pageClicked;
			$scope.currentpage = pageClicked;
			var queryStrings = {
				limit: itemsPerPage,
				page: pageClicked
			};

			BucketlistFactory.Bucketlist.getAll(queryStrings).$promise.then(
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
			if ( (nextPage + 1) <= pages) {
				nextPage += 1;
				pageRequested(nextPage);
			}
		};

		$scope.leftChevron = function () {
			if ( (nextPage - 1) >= 1) {
				nextPage -= 1;
				pageRequested(nextPage);
			}
		};

		$scope.loadBucketlists = function (pageSize) {
			nextPage = 1; pages = 1; itemsPerPage = 5;
			if ( typeof(pageSize) === 'undefined') {
				itemsPerPage = 5;
			} else {
				itemsPerPage = pageSize;
			}

			$cookies.put('pageSize', itemsPerPage);

			var queryStrings = {};
			queryStrings.limit = itemsPerPage;


			BucketlistFactory.Bucketlist.getAll(queryStrings).$promise.then(
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
					// console.log(error);
				}
			);

		};

		if ($cookies.get('pageSize')) {
			$scope.loadBucketlists($cookies.get('pageSize'));
			console.log($cookies.get('pageSize'));
		} else {
			$scope.loadBucketlists(itemsPerPage);
		}

		$scope.edit = function(buck_id) {
			swal(
				{
					title: "Don't like the current name?",
					text: "You can edit the bucketlist name here:",
					type: "input",   showCancelButton: true,
					closeOnConfirm: true,
					animation: "slide-from-top",
					inputPlaceholder: "Type in new bucketlist name"
				},
				function (inputValue) {
					if (inputValue === false)
						return false;
					if (inputValue === "" || inputValue.length < 1) {
						swal.showInputError("You need to write something (meaningful)!");
						return false
					}
					var data = {
						buck_id: buck_id,
						name: inputValue
					};
					BucketlistFactory.Bucketlist.edit(data).$promise.then(
						function (response) {
							// swal("Success!", "Bucketlist: " + buck_id + "'s name updated");
							var $toastContent = $('<strong style="color: #4db6ac;">Bucketlist updated to ' + inputValue + '</strong>');
							Materialize.toast($toastContent, 5000);
							// refresh bucketlists
							if ($cookies.get('pageSize')) {
								$scope.loadBucketlists($cookies.get('pageSize'));
							} else {
								$scope.loadBucketlists(itemsPerPage);
							}
						},
						function (error) {
							if (error.status === 403) {
								sweetAlert("Update operation failed...", "You don't have permissions to edit this Bucketlist", "error");
							} else {
								sweetAlert("Update operation failed...", "Bucketlist not edited.", "error");
							}
						}
					);

				}
			);
		};

		$scope.addBucketlist = function (data) {
			swal({
					title: "Create a new Bucketlist",
					text: "Enter a bucketlist name below",
					type: "input",
					showCancelButton: true,
					closeOnConfirm: true,
					animation: "slide-from-top",
					inputPlaceholder: "Write something"
				},
				function (inputValue) {
					if (inputValue === false) return false;
					if (inputValue === "") {
						swal.showInputError("Bucketlist name missing!");
						return false
					}
					var data = {
						name: inputValue
					}
					if (data.name != null) {
						BucketlistFactory.Bucketlist.create(data)
						.$promise.then(
							function (response) {
								var $toastContent = $('<strong style="color: #4db6ac;">' + response.message + '</strong>');
								Materialize.toast($toastContent, 5000);
								$scope.bucketlist_name = "";
								if ($cookies.get('pageSize')) {
									$scope.loadBucketlists($cookies.get('pageSize'));
								} else {
									$scope.loadBucketlists(itemsPerPage);
								}
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
			);
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
					closeOnConfirm: true
				},
				function () {
					BucketlistFactory.Bucketlist.deleteBucket(data).$promise.then(
						function (response) {
							var $toastContent = $('<strong style="color: #4db6ac;">Bucketlist has been deleted.</strong>');
							Materialize.toast($toastContent, 5000);
							if ($cookies.get('pageSize')) {
								$scope.loadBucketlists($cookies.get('pageSize'));
							} else {
								$scope.loadBucketlists(itemsPerPage);
							}
						},
						function (error) {

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
