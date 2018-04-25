app.factory('Account', function ($http, $rootScope, Cookie) {
    return {
        get: function () {
            return $http.get($rootScope.apiUrls.account, {
                headers: {'Authorization': 'Bearer ' + Cookie.get('token')}
            }).then(function (result) {
                return result;
            });
        },
    }
});
