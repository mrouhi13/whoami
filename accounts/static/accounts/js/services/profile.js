app.factory('Profile', function ($http, Cookie, API_URLS) {
    return {
        get: function () {
            return $http.get(API_URLS.profile, {
                headers: {'Authorization': 'Bearer ' + Cookie.get('token')}
            }).then(function (result) {
                return result;
            });
        },
        update: function (credentials) {
            return $http.put(API_URLS.profile, credentials, {
                headers: {'Authorization': 'Bearer ' + Cookie.get('token')}
            })
                .then(function (result) {
                    return result;
                });
        }
    }
});
