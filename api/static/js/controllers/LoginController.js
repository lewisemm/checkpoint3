BucketlistApp.controller('LoginController', ['$scope', '$http', '$window',
	function ($scope, $http, $window) {

		$scope.signUp = function() {
			if (!$scope.new_username) {
				$scope.signUpResponse = 'Sign Up username not provided';
			}
			else if ( (!$scope.new_password) || (!$scope.conf_new_password) ) {
				$scope.signUpResponse = 'Password and confirmation required';
			}
			else if ($scope.new_password != $scope.conf_new_password) {
				$scope.signUpResponse = 'Password and confirmation do not match';
			}
			else {
				var data = {
					username: $scope.new_username,
					password: $scope.new_password
				};
				$http.post(
					'http://localhost:8000/users/',
					data
				)
				.then(
					function (response) {
						console.log('Signed up');
						var $toastContent = $('<strong style="color: #4db6ac;">User successfully signed up. Proceed to Sign In.</strong>');
						Materialize.toast($toastContent, 5000);
						$scope.new_password = '';
						$scope.new_username = '';
					},
					function (error) {
						$scope.signUpResponse = 'User sign up failed';
					}
				);
			}

		}

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

		$scope.removeSignUpMsg = function () {
			$scope.signUpResponse = '';
		}

		$scope.removeMsg = function() {
			$scope.accessDenied = '';
		}
	}
]);