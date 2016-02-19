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
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/wars', {
        templateUrl: 'views/wars.html',
        controller: 'warsCtrl',
        controllerAs: 'wars'
      })
      .when('/wars/new', {
        templateUrl: 'views/new-war.html',
        controller: 'newWarCtrl',
        controllerAs: 'newWar'
      })
      .when('/wars/:war-id', {
        templateUrl: 'views/war.html',
        controller: 'warCtrl',
        controllerAs: 'war'
      })
      .when('/members', {
        templateUrl: 'views/members.html',
        controller: 'membersCtrl',
        controllerAs: 'members'
      })
      .when('/members/:member-id', {
        templateUrl: 'views/member.html',
        controller: 'memberCtrl',
        controllerAs: 'member'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
