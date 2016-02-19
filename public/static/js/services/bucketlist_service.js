BucketlistApp.factory('BucketlistFactory', ['$resource',
	function ($resource) {
		return {
			Bucketlist: $resource('/bucketlists/:buck_id/', {buck_id:'@buck_id'}, {
				getAll:{
					method: 'GET',
					isArray: false
				},
				getOne: {
					method: 'GET',
					isArray: false
				},
				deleteBucket:{
					method: 'DELETE'
				},
				create:{
					method: 'POST'
				},
				edit:{
					method: 'PUT'
				}
			}),
			Item: $resource('/bucketlists/:buck_id/items/', {buck_id:'@buck_id'}, {
				create:{
					method: 'POST'
				}
			}),
			ItemDetail: $resource('/bucketlists/:buck_id/items/:item_id/', {buck_id:'@buck_id'}, {
				edit:{
					method: 'PUT',
					params: {
						item_id: '@item_id'
					}
				},
				deleteItem: {
					method: 'DELETE'
				},
				getOne: {
					method: 'GET',
					isArray: false
				}
			})
		}
	}
]);