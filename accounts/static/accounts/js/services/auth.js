app.factory('Auth', function ($http, $rootScope, Cookie) {
    return {
        signin: function (credentials) {
            return $http.post($rootScope.apiUrls.createToken, credentials)
                .then(function (result) {
                    return result;
                });
        },
        signup: function (credentials) {
            return $http.post($rootScope.apiUrls.createUser, credentials)
                .then(function (result) {
                    return result;
                });
        },
        signout: function () {
            return $http.post($rootScope.apiUrls.destroyToken, {}, {
                headers: {'Authorization': 'Bearer ' + Cookie.get('token')}
            }).then(function (result) {
                return result;
            });
        },
        isAuthenticated: function () {
            return Cookie.get('token') !== '';
        },
        passwordReset: function (credentials) {
            return $http.post($rootScope.apiUrls.resetPassword, credentials)
                .then(function (result) {
                    return result;
                });
        }
    }
});
