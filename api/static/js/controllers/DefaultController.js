BucketlistApp.controller('DefaultController',
	function ($rootScope, $cookies, $window) {
		$rootScope.signOutLabel = "Sign Out";
		$rootScope.showSignIn = true;
		$rootScope.showSignOut = false;

		$rootScope.signOut = function () {
			$rootScope.showSignIn = true;
			$rootScope.showSignOut = false;
			$rootScope.signOutLabel = "Sign Out";
			$cookies.remove('Authorization');
			$window.location.href = '#/';
			var $toastContent = $('<strong style="color: #4db6ac;">You have successfully logged out</strong>');
			Materialize.toast($toastContent, 5000);
		}
	}
);