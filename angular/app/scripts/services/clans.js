var services = services || angular.module("theWarRoomApp_services", []);

services.factory('ClanFactory', ['$resource', function($resource){
	return $resource('http://192.168.0.2:8000/webservice/clans/:id', null, {
    members: {
      method: 'GET',
      url: "http://192.168.0.2:8000/webservice/clans/:id/members",
      isArray: true
    }
  });
}]);
