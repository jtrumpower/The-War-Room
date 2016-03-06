var controllers = controllers || angular.module('theWarRoomApp_controllers', []);

controllers.controller('ClanController',
  function ($scope, ClanFactory, $routeParams) {

    ClanFactory.get({ id: $routeParams.id }).$promise.then(
      function success(json) {
        $scope.clan = json;
      },
      function fail() {

      }
    );

    ClanFactory.members({ id: $routeParams.id }).$promise.then(
      function success(json) {
        $scope.members = json;
      },
      function fail(json) {

      }
    );
  }
);
