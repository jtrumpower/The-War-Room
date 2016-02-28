var services = services || angular.module("theWarRoomApp_services", []);

services.factory('CommentFactory', ['$resource', function($resource){
	return $resource('/webservice/comments', null, {});
}]);


services.factory('CommentItemFactory', ['$resource', function($resource){
	return $resource('/webservice/comments/:id', { id: "@id" }, {});
}]);