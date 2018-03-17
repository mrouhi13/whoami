app.factory('Auth', function ($http, Cookie, APP_CONFIG) {
    return {
        signin: function (credentials) {
            return $http.post(APP_CONFIG.apiUrl + 'token/create/', credentials)
                .then(function (result) {
                    return result;
                });
        },
        signup: function (credentials) {
            return $http.post(APP_CONFIG.apiUrl + 'users/create/', credentials)
                .then(function (result) {
                    return result;
                });
        },
        signout: function () {
            return $http.post(APP_CONFIG.apiUrl + 'token/destroy/', {}, {
                headers: {'Authorization': 'Bearer ' + Cookie.get('token')},
            })
                .then(function (result) {
                    return result;
                });
        },
        isAuthenticated: function () {
            return Cookie.get('token') != '';
        },
        passwordReset: function (credentials) {
            return $http.post(APP_CONFIG.apiUrl + 'password-reset/', credentials)
                .then(function (result) {
                    return result;
                });
        },
    }
});
