var controllers = controllers || angular.module('theWarRoomApp_controllers', []);

controllers.controller('WarController', ['$scope', '$routeParams', '$location', 'WarFactory', 'ClanFactory', 'BaseFactory',
  	function ($scope, $routeParams, $location, WarFactory, ClanFactory, BaseFactory) {
      if($location.path().indexOf("latest") > -1){
        WarFactory.latest({ id: $routeParams.id }).$promise.then(
          function(war) {
            $scope.war = war;
            getBases(war.id);
          },
          function() {

          }
        );

        getMembers($routeParams.id);
      } else {
        WarFactory.war({ clanId: $routeParams.clanId, warId: $routeParams.warId }).$promise.then(
          function(war) {
            $scope.war = war;
          },
          function() {

          }
        );

        getMembers($routeParams.clanId);

        getBases($routeParams.warId);

      }

      function getBases(warId) {
        WarFactory.bases({ id: warId }).$promise.then(
          function success(bases) {
            $scope.bases = bases;
          },
          function fail() {
            $scope.bases = [];
          }
        );
      }

      function getMembers(clanId) {
        ClanFactory.members({ id: clanId }).$promise.then(
          function success(members) {
            $scope.members = members;
          },
          function fail() {
            $scope.members =  [];
          }
        );
      }
  	}
  ]
);
