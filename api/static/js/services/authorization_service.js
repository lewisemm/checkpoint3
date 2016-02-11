BucketlistApp.service('AuthorizationService', ['$cookies',
	function ($cookies) {
		var service = this;
		service.request = function (config) {
			token = $cookies.get('Authorization');
			config.headers = config.headers || {}

			if (token) {
				config.headers['Authorization'] = 'JWT ' + $cookies.get('Authorization');
			}

			return config;
		};
	}
])