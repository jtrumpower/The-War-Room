var controllers = controllers || angular.module('theWarRoomApp_controllers', []);

controllers.controller('WarController', ['$scope', 'WarFactory', '$routeParams',
  	function ($scope, WarFactory, $routeParams) {
    	WarFactory.get({ id: $routeParams.id }).$promise.then(
    		function(war) {
    			$scope.war = war;
    		},
    		function() {

    		}
    	);
  	}
  ]
);
