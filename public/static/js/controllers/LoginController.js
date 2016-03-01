
BucketlistApp.controller('LoginController',
	['$scope', '$http', '$window', '$cookies', '$rootScope', 'APIAccessFactory',
	function ($scope, $http, $window, $cookies, $rootScope, APIAccessFactory) {
		$rootScope.loginPage=true;

		// if someone is/had logged in, show sign in button and remove existing
		// auth token
		if ($cookies.get('Authorization')) {
			$rootScope.showSignIn = true;
			$cookies.remove('Authorization');
			$cookies.remove('Username');
		}

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

				APIAccessFactory.NewUser.create(data).$promise.then(
					function (response) {

						var $toastContent = $('<strong style="color: #4db6ac;">User successfully signed up. You can proceed to Sign In.</strong>');
						Materialize.toast($toastContent, 5000);
						$(document).ready(function(){
							$('ul.tabs').tabs('select_tab', 'signin');
						});
						$scope.new_password = '';
						$scope.new_username = '';
						console.log(response);
					},
					function (error) {
						console.log(error);
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


				APIAccessFactory.User.login(data).$promise.then(
					function (response) {
						// attach token to authorization header
						var token = response.token;
						if (token) {
							$cookies.put('Authorization', token);
							$cookies.put('Username', data.username);
							$rootScope.showSignIn = false;

							if ($cookies.get('Authorization')) {
								$window.location.href = '#bucketlist';
							}
						} else {
							$scope.accessDenied = response.non_field_errors[0];
						}



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