var services = services || angular.module("theWarRoomApp_services", []);

services.factory('MemberFactory', ['$resource', function($resource){
	return $resource('/webservice/members', null, {});
}]);


services.factory('MemberItemFactory', ['$resource', function($resource){
	return $resource('/webservice/members/:id', { id: "@id" }, {});
}]);