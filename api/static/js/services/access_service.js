BucketlistApp.factory('APIAccessFactory', ['$resource',
	function ($resource) {
		return {
			User: $resource('/auth/login/', {}, {
				login:{
					method: 'POST'
				}
			}),
			NewUser: $resource('/users/', {}, {
				create:{
					method: 'POST'
				}
			}),
			UserExists: $resource('/users/', {}, {
				search:{
					method: 'GET'
				}
			})
		}
	}
]);