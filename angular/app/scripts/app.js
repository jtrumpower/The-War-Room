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
    'theWarRoomApp_services'
  ])
  .config(function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainController',
        controllerAs: 'main'
      })
      .when('/wars', {
        templateUrl: 'views/wars/wars.html',
        controller: 'WarsController',
        controllerAs: 'wars'
      })
      .when('/wars/new', {
        templateUrl: 'views/wars/new-war.html',
        controller: 'NewWarController',
        controllerAs: 'newWar'
      })
      .when('/wars/:id', {
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
  });
