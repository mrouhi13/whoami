app.factory('Profile', function ($http, $rootScope, Cookie) {
    return {
        get: function () {
            return $http.get($rootScope.apiUrls.profile, {
                headers: {'Authorization': 'Bearer ' + Cookie.get('token')}
            }).then(function (result) {
                return result;
            });
        },
        update: function (credentials) {
            return $http.put($rootScope.apiUrls.profile, credentials, {
                headers: {'Authorization': 'Bearer ' + Cookie.get('token')}
            })
                .then(function (result) {
                    return result;
                });
        }
    }
});
