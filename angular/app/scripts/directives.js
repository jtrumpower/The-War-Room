var directives = directives || angular.module('theWarRoomApp_directives', []);

directives.directive('convertToNumber', function() {
  return {
    require: 'ngModel',
    link: function(scope, element, attrs, ngModel) {
      ngModel.$parsers.push(function(val) {
        return parseInt(val, 10);
      });
      ngModel.$formatters.push(function(val) {
        return '' + val;
      });
    }
  };
});

directives.directive('baseRow', function() {
  return {
    link: function(scope, element, attrs, ngModel) {

    },
    controller: ['$scope', 'DibFactory', 'BaseFactory', '$route', '$uibModal',
      function($scope, DibFactory, BaseFactory, $route, $uibModal) {
        $scope.row = null;
        $scope.call = function(base, member, idx) {
          console.log(base, member, idx);
          DibFactory.save({ base: base.id, member: member.id }).$promise.then(
            function success(){
              $route.reload();
            },
            function fail() {

            }
          );
          if(base.position == null) {
            base.position = idx + 1;
            BaseFactory.update({ id: base.id }, base);
          }

        };

        $scope.dibModal = function(dib) {
          console.log(dib);
          var modalInstance = $uibModal.open({
            templateUrl: "/views/modals/update-dib.html",
            controller: 'UpdateDibModalCtrl',
            size: "sm",
            resolve: {
              dib: dib
            }
          });
        };

        $scope.getMemberName = function (members, id) {
          for (var i = 0; i < members.length; i++) {
            var member = members[i];
            if(member.id == id) {
              return member.game_name;
            }
          }
        };

        $scope.getPosition = function (bases, idx) {
          for (var i = 0; i < bases.length; i++) {
            var row = bases[i];
            if(row.base.position == idx + 1) {
              return row.base
            }
          }
          return null;
        };

        $scope.getBaseIndex = function (bases, idx) {
          for (var i = 0; i < bases.length; i++) {
            var row = bases[i];
            if(row.base.position == idx + 1) {
              return i
            }
          }
          return null;
        }
      }
    ]
  };
});
