app.factory('Auth', function ($http, Cookie, API_URLS) {
    return {
        signin: function (credentials) {
            return $http.post(API_URLS.createToken, credentials)
                .then(function (result) {
                    return result;
                });
        },
        signup: function (credentials) {
            return $http.post(API_URLS.createUser, credentials)
                .then(function (result) {
                    return result;
                });
        },
        signout: function () {
            return $http.post(API_URLS.destroyToken, {}, {
                headers: {'Authorization': 'Bearer ' + Cookie.get('token')}
            }).then(function (result) {
                return result;
            });
        },
        isAuthenticated: function () {
            return Cookie.get('token') !== '';
        },
        passwordReset: function (credentials) {
            return $http.post(API_URLS.resetPassword, credentials)
                .then(function (result) {
                    return result;
                });
        }
    }
});
