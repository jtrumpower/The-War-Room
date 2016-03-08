var services = services || angular.module("theWarRoomApp_services", []);

services.factory('WarFactory', ['$resource', function($resource){
	return $resource('/webservice/wars/:id/', null, {
    all: {
      method: 'GET',
      url: '/webservice/clans/:id/wars',
      params: { id: '@id' },
      isArray: true
    },
    latest: {
      method: 'GET',
      url: '/webservice/clans/:id/wars/latest',
      params: { id: '@id' },
      isArray: false
    },
    war: {
      method: 'GET',
      url: '/webservice/clans/:clanId/wars/:warId',
      params: { clanId: '@clanId', warId: '@warId' },
      isArray: false
    },
    bases: {
      method: 'GET',
      url: '/webservice/wars/:id/bases',
      params: { id: '@id' },
      isArray: true
    }
  });
}]);
