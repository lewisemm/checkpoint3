BucketlistApp.service('AuthorizationService', ['$cookies',
	function ($cookies) {
		var service = this;
		service.request = function (config) {
			config.headers['Authorization'] = 'JWT ' + $cookies.get('Authorization');
			return config;
		};
	}
])