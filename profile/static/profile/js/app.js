'use strict';
var app = angular.module('profile', ['ngRoute', 'ngFileUpload']);

app.constant("APP_CONFIG", {
    appVrsion: '0.0.1',
    appProducer: 'Majid Rouhi Kh.',
    apiUrl: "http://127.0.0.1:8000/api/v1/"
});

app.constant('AUTH_EVENTS', {
  signinSuccess: 'auth-signin-success',
  signinFailed: 'auth-signin-failed',
  signoutSuccess: 'auth-signout-success',
  sessionTimeout: 'auth-session-timeout',
  notAuthenticated: 'auth-not-authenticated',
  notAuthorized: 'auth-not-authorized'
});

app.constant('USER_ROLES', {
  all: '*',
  admin: 'admin',
  user: 'user',
  organizer: 'organizer'
})
