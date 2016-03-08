var controllers = controllers || angular.module('theWarRoomApp_controllers', []);

controllers.controller('WarController', ['$scope', '$routeParams', '$location', 'WarFactory', 'ClanFactory', 'BaseFactory',
  	function ($scope, $routeParams, $location, WarFactory, ClanFactory, BaseFactory) {
      if($location.path().indexOf("latest") > -1){
        WarFactory.latest({ id: $routeParams.id }).$promise.then(
          function(json) {
            $scope.war = json.war;
            $scope.bases = json.bases;
            $scope.members = json.members;
          },
          function() {

          }
        );
      } else {
        WarFactory.war({ clanId: $routeParams.clanId, warId: $routeParams.warId }).$promise.then(
          function(json) {
            $scope.war = json.war;
            $scope.bases = json.bases;
            $scope.members = json.members;
          },
          function() {

          }
        );
      }
  	}
  ]
);
