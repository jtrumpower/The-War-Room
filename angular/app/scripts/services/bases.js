var services = services || angular.module("theWarRoomApp_services", []);

services.factory('BaseFactory', ['$resource', function($resource){
	return $resource('/webservice/bases/:id/', null, {
    update: {
      method: 'PUT',
      isArray: false
    }
  });
}]);
