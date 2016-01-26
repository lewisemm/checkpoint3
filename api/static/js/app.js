var BucketlistApp = angular.module("BucketlistApp", ['ngRoute', 'ngResource']);

// conflicts with Django's templating warrants this change
BucketlistApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

BucketlistApp.config(['$resourceProvider', function ($resourceProvider) {
	$resourceProvider.defaults.stripTrailingSlashes = false;
}]);

BucketlistApp.config(function ($routeProvider) {
	$routeProvider
	.when('/', {
		templateUrl: 'static/views/index.html'
	})
	.when('/login', {
		templateUrl: 'static/views/login.html',
		controller: 'LoginController'
	})
	.when('/bucketlist', {
		templateUrl: 'static/views/bucketlist.html',
		controller: 'BucketlistController'
	})
	.when('/bucketlist/:buckId/', {
		templateUrl: 'static/views/bucketlist_details.html',
		controller: 'BucketlistDetailsController'
	});

});