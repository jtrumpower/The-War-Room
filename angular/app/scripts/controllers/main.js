var controllers = controllers || angular.module('theWarRoomApp_controllers', []);

controllers.controller('MainController', ['$scope', '$uibModal', 'ClanFactory',
  function ($scope, $uibModal, ClanFactory) {

    /*$scope.createClan = function() {
      var modalInstance = $uibModal.open({
        templateUrl: "/views/modals/new-clan.html",
        controller: 'CreateClanModalCtrl',
        size: "sm"
      });
    }*/

    $scope.searchForClan = function() {
      var modalInstance = $uibModal.open({
        templateUrl: "/views/modals/search-clans.html",
        controller: 'SearchClanModalCtrl',
        size: "sm"
      });
    }

    $scope.createWar = function() {
      var modalInstance = $uibModal.open({
        templateUrl: "/views/modals/create-war.html",
        controller: 'CreateWarModalCtrl'
      });
    }
  }
]);
