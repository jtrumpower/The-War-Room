var controllers = controllers || angular.module('theWarRoomApp_controllers', []);

controllers.controller('WarsController', ['$scope', 'WarFactory', 
  	function ($scope, WarFactory) {
  		WarFactory.query().$promise.then(
  			function(wars) {
  				$scope.wars = wars;
  			},
  			function(){

  			}
  		);
  	}
]);