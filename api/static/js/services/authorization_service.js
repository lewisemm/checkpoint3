BucketlistApp.service('AuthorizationService', ['$cookies', '$window', '$rootScope',
	function ($cookies, $window, $rootScope) {
		var service = this;
		service.request = function (config) {
			var token = $cookies.get('Authorization');
			config.headers = config.headers || {}

			if (token) {
				config.headers['Authorization'] = 'JWT ' + $cookies.get('Authorization');
				$rootScope.signOutLabel = "Sign Out, " + $cookies.get('Username');
			}

			return config;
		};

		service.responseError = function (response) {
			if (response.status === 401) {
				if (response.data.detail === 'Signature has expired.') {
					swal(
						{
							title: "Your current session has expired!",
							text: "Please login again to refresh it.",
							type: "error",
							showCancelButton: true,
							confirmButtonColor: "#4db6ac",
							confirmButtonText: "Proceed to Sign In!",
							closeOnConfirm: true
						},
						function () {
							$window.location.href = "/#/login/";
						}
					);

				} else if (response.data.detail === 'Authentication credentials were not provided.') {
					swal(
						{
							title: "Authentication Required!",
							text: "You need to be authenticated to perform this action.",
							type: "error",
							showCancelButton: true,
							confirmButtonColor: "#4db6ac",
							confirmButtonText: "Proceed to Sign In!",
							closeOnConfirm: true
						},
						function () {
							$window.location.href = "/#/login/";
						}
					);
				}
			} else if (response.status === 403) {
				if (response.data.detail === 'You do not have permission to perform this action.') {
					sweetAlert("Write operations denied!", "Only the bucketlist owner is permitted to perform this action.", "error");
				}
			}

			return response;
		};
	}
])