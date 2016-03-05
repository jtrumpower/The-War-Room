var controllers = controllers || angular.module('theWarRoomApp_controllers', []);

controllers.controller('ClansController',
  function ($scope, ClanFactory, $routeParams) {

    ClanFactory.query().$promise.then(
      function success(json) {
        $scope.clans = json;
      },
      function fail() {

      }
    );
  }
);
