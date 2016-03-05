var controllers = controllers || angular.module('theWarRoomApp_controllers', []);

controllers.controller('WarController', ['$scope', 'WarFactory', '$routeParams', '$location',
  	function ($scope, WarFactory, $routeParams, $location) {
      if($location.path().indexOf("latest") > -1){
        WarFactory.latest({ clanId: $routeParams.id }).$promise.then(
          function(war) {
            $scope.war = war;
          },
          function() {

          }
        );
      } else {
        WarFactory.war({ clanId: $routeParams.clanId, warId: $routeParams.warId }).$promise.then(
          function(war) {
            $scope.war = war;
          },
          function() {

          }
        );
      }
  	}
  ]
);
