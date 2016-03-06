var services = services || angular.module("theWarRoomApp_services", []);

services.factory('MemberFactory', ['$resource', function($resource){
	return $resource('http://192.168.0.2/webservice/members/:id', null, {});
}]);
