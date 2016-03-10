var services = services || angular.module("theWarRoomApp_services", []);

services.factory('DibFactory', ['$resource', function($resource){
	return $resource('/webservice/dibs/:id/', { id: "@id" }, {
    update: {
      method: 'PUT',
      isArray: false
    }
  });
}]);
