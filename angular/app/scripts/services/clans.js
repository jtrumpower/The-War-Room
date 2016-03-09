var services = services || angular.module("theWarRoomApp_services", []);

services.factory('ClanFactory', ['$resource', function($resource){
	return $resource('/webservice/clans/:id/', null, {
    members: {
      method: 'GET',
      url: "/webservice/clans/:id/members/",
      isArray: true
    }
  });
}]);
