BucketlistApp.controller('LoginController', ['$scope', '$http', '$window',
	function ($scope, $http, $window) {

		$scope.login = function () {
			var data = {
				username: $scope.login_username,
				password: $scope.login_password
			};
			$http.post(
				'http://localhost:8000/auth/login/',
				data
			)
			.then(function (response) {
				// attach token to authoruzation header
				$window.location.href = "#bucketlist";
			});
		};
	}
]);