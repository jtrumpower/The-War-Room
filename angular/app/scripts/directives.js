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
    controller: ['$scope', 'DibFactory',
      function($scope, DibFactory) {
        $scope.call = function(base, member) {
          console.log(base, member);
          DibFactory.save({ base: base.id, member: member.id });
        }
      }
    ]
  };
});
