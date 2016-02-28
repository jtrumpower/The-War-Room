var services = services || angular.module("theWarRoomApp_services", []);

services.factory('DibFactory', ['$resource', function($resource){
	return $resource('/webservice/dibs/', null, {});
}]);


services.factory('DibItemFactory', ['$resource', function($resource){
	return $resource('/webservice/dibs/:id', { id: "@id" }, {});
}]);