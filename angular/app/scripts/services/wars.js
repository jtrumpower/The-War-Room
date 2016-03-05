var services = services || angular.module("theWarRoomApp_services", []);

services.factory('WarFactory', ['$resource', function($resource){
	return $resource('http://192.168.0.2:8000/webservice/wars/:id/', null, {
    all: {
      method: 'GET',
      url: 'http://192.168.0.2:8000/webservice/clans/:clanId/wars',
      params: { clanId: '@clanId' },
      isArray: true
    },
    latest: {
      method: 'GET',
      url: 'http://192.168.0.2:8000/webservice/clans/:clanId/wars/latest',
      params: { clanId: '@clanId' },
      isArray: false
    },
    war: {
      method: 'GET',
      url: 'http://192.168.0.2:8000/webservice/clans/:clanId/wars/:warId',
      params: { clanId: '@clanId', warId: '@warId' },
      isArray: false
    }
  });
}]);
