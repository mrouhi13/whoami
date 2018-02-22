app.factory('Auth', function ($http, Cookie, APP_CONFIG) {
    return {
        signin: function (credentials) {
            return $http.post(APP_CONFIG.apiUrl + 'signin/', credentials)
                .then(function (result) {
                    return result;
                });
        },
        signup: function (credentials) {
            return $http.post(APP_CONFIG.apiUrl + 'signup/', credentials)
                .then(function (result) {
                    return result;
                });
        },
        signout: function () {
            return $http.post(APP_CONFIG.apiUrl + 'signout/', {}, {
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
})