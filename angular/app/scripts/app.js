'use strict';

/**
 * @ngdoc overview
 * @name theWarRoomApp
 * @description
 * # theWarRoomApp
 *
 * Main module of the application.
 */
angular
  .module('theWarRoomApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngTouch',
    'theWarRoomApp_controllers',
    'theWarRoomApp_services',
    'ui.bootstrap'
  ])
  .config(function ($routeProvider, $locationProvider, $resourceProvider, $httpProvider) {
    $locationProvider.html5Mode(true);
    $resourceProvider.defaults.stripTrailingSlashes = false;
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainController',
        controllerAs: 'main'
      })
      .when('/clans', {
        templateUrl: 'views/clans.html',
        controller: 'ClansController',
        controllerAs: 'clans'
      })
      .when('/clans/:id', {
        templateUrl: 'views/clan.html',
        controller: 'ClanController',
        controllerAs: 'clan'
      })
      .when('/clans/:id/wars', {
        templateUrl: 'views/wars/wars.html',
        controller: 'WarsController',
        controllerAs: 'clans'
      })
      .when('/clans/:id/wars/latest', {
        templateUrl: 'views/wars/war.html',
        controller: 'WarController',
        controllerAs: 'war'
      })
      .when('/clans/:clanId/wars/:warId', {
        templateUrl: 'views/wars/war.html',
        controller: 'WarController',
        controllerAs: 'war'
      })
      .when('/members', {
        templateUrl: 'views/members.html',
        controller: 'MembersController',
        controllerAs: 'members'
      })
      .when('/members/:id', {
        templateUrl: 'views/member.html',
        controller: 'MemberController',
        controllerAs: 'member'
      })
      .otherwise({
        redirectTo: '/'
      });

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  });
