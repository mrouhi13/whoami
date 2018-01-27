app.factory('Auth', function () {
    return {
        setUser: function (token) {
            window.localStorage.setItem('token', token);
        },
        unsetUser: function () {
            window.localStorage.removeItem('token');
        },
        isAuthenticate: function () {
            var token = window.localStorage.getItem('token');
            return (token) ? token : false;
        }
    }
})


// app.factory('Auth', function ($http, Session, APP_CONFIG) {
//   var auth = {};
//
//   auth.signin = function (credentials) {
//     return $http
//       .post(APP_CONFIG.apiUrl + 'signin/', credentials)
//       .then(function (res) {
//         Session.create(res.data.token);
//         return res.data.user;
//       });
//   };
//
//   auth.isAuthenticated = function () {
//     return !!Session.userToken;
//   };
//
//   auth.isAuthorized = function (authorizedRoles) {
//     if (!angular.isArray(authorizedRoles)) {
//       authorizedRoles = [authorizedRoles];
//     }
//     return (auth.isAuthenticated() &&
//       authorizedRoles.indexOf(Session.userRole) !== -1);
//   };
//
//   return auth;
// });