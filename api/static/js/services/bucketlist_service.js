BucketlistApp.factory('BucketlistFactory', ['$resource',
	function ($resource) {
		return {
			getAll: function () {
				var resource = $resource('/bucketlists');
				return resource.query();
			},
			getOne: function (id) {
				var resource = $resource('/bucketlists/' + id);
				return resource.get();
			}
		};
	}
]);