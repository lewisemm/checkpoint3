BucketlistApp.controller('LoginController', ['$scope', '$http', '$window',
	function ($scope, $http, $window) {

		$scope.login = function () {
			if (!$scope.login_username) {
				$scope.accessDenied = 'Username missing';
			}
			else if (!$scope.login_password) {
				$scope.accessDenied = 'Password missing';
			}
			else {
				var data = {
					username: $scope.login_username,
					password: $scope.login_password
				};
				$http.post(
					'http://localhost:8000/auth/login/',
					data
				)
				.then(
					function (response) {
						// attach token to authorization header
						var token = response.data.token;
						if (token) {
							$cookies.put('Authorization', token);
						}
						$window.location.href = '#bucketlist';
					},
					function (error) {
						$scope.accessDenied = 'Incorrect username and/or password';
					}
				);

			}
		};

		$scope.removeMsg = function() {
			$scope.accessDenied = '';
		}
	}
]);