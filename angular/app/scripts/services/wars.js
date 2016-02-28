var services = services || angular.module("theWarRoomApp_services", []);

services.factory('WarFactory', ['$resource', function($resource){
	return $resource('/webservice/wars/:id', null, {});
}]);
