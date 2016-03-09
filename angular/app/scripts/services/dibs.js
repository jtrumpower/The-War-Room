var services = services || angular.module("theWarRoomApp_services", []);

services.factory('DibFactory', ['$resource', function($resource){
	return $resource('http://192.168.0.2:8000/webservice/dibs/:id/', { id: "@id" }, {});
}]);
