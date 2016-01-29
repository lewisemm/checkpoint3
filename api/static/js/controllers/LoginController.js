BucketlistApp.controller('LoginController',
	['$scope', '$http', '$window', '$cookies',
	function ($scope, $http, $window, $cookies) {

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
				// attach token to authorization header
				var token = response.data.token;
				if (token) {
					$cookies.put('Authorization', token);
				}
				$window.location.href = "#bucketlist";
			});
		};
	}
]);