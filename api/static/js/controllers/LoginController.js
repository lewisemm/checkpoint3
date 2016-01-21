BucketListApp.controller('LoginController', ['$scope', '$http', function($scope, $http) {
	var login_user = this;
	login_user.login = function() {
		var data = {
			username: $scope.login_username,
			password: $scope.login_password
		}
		$http.post(
			"http://localhost:8000/auth/login/",
			data
		).then(function(response) {
			$scope.token = response.data.token;
		});
	};

}]);