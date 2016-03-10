var controllers = controllers || angular.module('theWarRoomApp_controllers', []);

/*controllers.controller('CreateClanModalCtrl', ['$scope', '$uibModalInstance', 'ClanFactory',
  function ($scope, $uibModalInstance, ClanFactory) {
    $scope.ok = function () {
      ClanFactory.save($scope.clan).$promise.then(
        function success() {
          $uibModalInstance.close($scope.clan);
        },
        function fail(response) {
          var data = response.data;
          if(data.detail != undefined) {
            $scope.error = data.detail;
          } else {
            $scope.error = "An error occured while adding clan";
          }
        }
      );
    };

    $scope.cancel = function () {
      $uibModalInstance.dismiss('cancel');
    };
  }
]);*/

controllers.controller('SearchClanModalCtrl', ['$scope', '$uibModalInstance', 'ClanFactory', '$location',
  function ($scope, $uibModalInstance, ClanFactory, $location) {
    $scope.ok = function () {
      if($scope.clan.clan_tag != "") {
        ClanFactory.get({ id: $scope.clan.clan_tag.substring(1) }).$promise.then(
          function success(json) {
            $location.path("/clans/" + json.clan_tag);
            $uibModalInstance.dismiss('cancel');
          },
          function fail(response) {
            var data = response.data;
            if(data.detail != undefined) {
              $scope.error = data.detail;
            } else {
              $scope.error = "An error occured while adding clan";
            }
          }
        );
      }
    };

    $scope.cancel = function () {
      $uibModalInstance.dismiss('cancel');
    };
  }
]);

controllers.controller('CreateWarModalCtrl', ['$scope', '$uibModalInstance', 'WarFactory', '$location',
  function ($scope, $uibModalInstance, WarFactory, $location) {
    $scope.options = [
      { name: "10 vs 10", value: 10 },
      { name: "15 vs 15", value: 15 },
      { name: "20 vs 20", value: 20 },
      { name: "25 vs 25", value: 25 },
      { name: "30 vs 30", value: 30 },
      { name: "35 vs 35", value: 35 },
      { name: "40 vs 40", value: 40 },
      { name: "45 vs 45", value: 45 },
      { name: "50 vs 50", value: 50 }
    ]
    $scope.ok = function () {
      $scope.war.size = $scope.war.size.value
      WarFactory.save($scope.war).$promise.then(
        function success(json) {
          $location.path("/clans/" + json.clan + "/wars/latest");
          $uibModalInstance.dismiss('cancel');
        },
        function fail(response) {
          var data = response.data;
          if(data.detail != undefined) {
            $scope.error = data.detail;
          } else {
            $scope.error = "An error occured while adding clan";
          }
        }
      );
    };

    $scope.cancel = function () {
      $uibModalInstance.dismiss('cancel');
    };
  }
]);

controllers.controller('UpdateDibModalCtrl',
  function ($scope, $uibModalInstance, dib, DibFactory) {
    $scope.dib = dib;
    var initStars = dib.stars;
    var initDest = dib.destruction;
    $scope.ok = function () {
      console.log(dib);
      DibFactory.update({ id: dib.id }, dib).$promise.then(
        function success(json) {
          $uibModalInstance.dismiss('done');
        },
        function fail(response) {
          var data = response.data;
          if(data.detail != undefined) {
            $scope.error = data.detail;
          } else {
            $scope.error = "An error occured while adding clan";
          }
        }
      );
    };

    $scope.$on("modal.closing", function(result, dismissed, a, c) {
      console.log(result, dismissed, a, c);
      if(dismissed != "done") {
        dib.stars = initStars;
        dib.destruction = initDest;
      }
    });

    $scope.cancel = function () {
      $uibModalInstance.dismiss('cancel');
    };
  }
);
