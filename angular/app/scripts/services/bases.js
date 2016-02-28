var services = services || angular.module("theWarRoomApp_services", []);

services.factory('BaseFactory', ['$resource', function($resource){
	return $resource('/webservice/bases', null, {});
}]);


services.factory('BaseItemFactory', ['$resource', function($resource){
	return $resource('/webservice/bases/:id', { id: "@id" }, {});
}]);