var controllers = controllers || angular.module('theWarRoomApp_controllers', []);

controllers.controller('WarsController', ['$scope', 'WarFactory', '$routeParams',
  	function ($scope, WarFactory, $routeParams) {
  		WarFactory.all({ clanId: $routeParams.clanId }).$promise.then(
  			function(wars) {
  				$scope.wars = wars;
  			},
  			function(){

  			}
  		);
  	}
]);
