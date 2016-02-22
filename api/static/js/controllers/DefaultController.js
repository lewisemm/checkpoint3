BucketlistApp.controller('DefaultController',
	function ($rootScope, $cookies, $window) {
		$rootScope.loginPage=false;
		// if there's no authorization token, show signIn button
		if (!$cookies.get('Authorization')) {
			$rootScope.showSignIn = true;
		}


		$rootScope.signOut = function () {
			$rootScope.showSignIn = true;
			$rootScope.signOutLabel = "Sign Out";
			$cookies.remove('Authorization');
			$cookies.remove('Username');
			$window.location.href = '#/';
			var $toastContent = $('<strong style="color: #4db6ac;">You have successfully logged out</strong>');
			Materialize.toast($toastContent, 5000);
		}
	}
);