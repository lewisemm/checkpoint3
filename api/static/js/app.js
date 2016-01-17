var BucketListApp = angular.module('BucketListApp', ['ngRoute']);

// conflicts with Django's templating warrants this change
BucketListApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('<<');
    $interpolateProvider.endSymbol('>>');
  });