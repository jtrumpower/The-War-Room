var services = services || angular.module("theWarRoomApp_services", []);

services.factory('ClanFactory', ['$resource', function($resource){
	return $resource('/webservice/clans', null, {});
}]);


services.factory('ClanItemFactory', ['$resource', function($resource){
	return $resource('/webservice/clans/:id', { id: "@id" }, {});
}]);