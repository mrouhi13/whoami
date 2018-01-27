app.controller('recoverPasswordCtrl', function ($scope, $http, Auth, APP_CONFIG) {
    $scope.init = function () {
        if (Auth.isAuthenticate()) {
            window.location.replace("/profile");
        }
    };
});
