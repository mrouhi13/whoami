app.controller('signinCtrl', function ($scope, $http, Auth, APP_CONFIG) {
  $scope.showCard = false;
  $scope.error = '';
  $scope.init = function () {
      if (Auth.isAuthenticate()) {
          window.location.replace("/profile");
      }
  };

  $scope.signin = function (data) {
      var content = {
          "email": data.email,
          "password": data.password
      }

      $http.post(APP_CONFIG.apiUrl + "signin/", content)
          .then(function (response) {
              Auth.setUser(response.data.content.token);
              window.location.replace("/profile");
          }, function (error) {
              $scope.error = error.data.message;
              $scope.showCard = true;
          });
  };
});


// app.controller('signinCtrl', function ($scope, $rootScope, $http, AUTH_EVENTS, Auth) {
//   $scope.credentials = {
//     username: '',
//     password: ''
//   };
//   $scope.signin = function (credentials) {
//     Auth.signin(credentials).then(function (user) {
//       $rootScope.$broadcast(AUTH_EVENTS.signinSuccess);
//       $scope.setCurrentUser(user);
//     }, function () {
//       $rootScope.$broadcast(AUTH_EVENTS.signinFailed);
//     });
//   };
// });