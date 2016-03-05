var controllers = controllers || angular.module('theWarRoomApp_controllers', []);

controllers.controller('WarsController', ['$scope', 'WarFactory', '$routeParams',
  	function ($scope, WarFactory, $routeParams) {
  		WarFactory.all({ clanId: $routeParams.id }).$promise.then(
  			function(wars) {
  				$scope.wars = wars;
  			},
  			function(){

  			}
  		);
  	}
]);
