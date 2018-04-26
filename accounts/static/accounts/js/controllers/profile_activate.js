app.controller('profileActivateCtrl', function ($scope, $rootScope, $timeout, Auth, Account, Cookie, Notification) {
    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            Account.get().then(function (response) {
                if (response.data.content.is_active) {
                    window.location.replace($rootScope.appUrls.profile);
                }
            }, function (error) {
                if (error.data.status === 401) {
                    $scope.signout();
                } else {
                    Notification.error(error.data.message);
                }
            });

            Cookie.set('token=', Cookie.get('token'), sessionStorage.getItem('rememberMe'));
        } else {
            window.location.replace($rootScope.appUrls.signin);
        }

        if (localStorage.getItem('message') !== null) {
            Notification.custom(localStorage.getItem('message'), localStorage.getItem('messageType'));

            localStorage.removeItem('message');
            localStorage.removeItem('messageType');
        }

        $scope.firstSignin = localStorage.getItem('firstSignin');
    };

    $scope.resendActivationEmail = function () {
        Auth.resendActivationEmail(credentials).then(function (response) {
            Notification.success(response.data.message);
        }, function (error) {
            if (error.data.status === 401) {
                $scope.signout();
            } else {
                Notification.error(error.data.message);
            }
        });
    };

    $scope.signout = function () {
        Auth.signout().then(function () {
        }, function (error) {
            localStorage.setItem('message', error.data.message);
            localStorage.setItem('messageType', $rootScope.notificationType.ERROR);
        });

        Cookie.remove('token');

        $timeout(function () {
            window.location.replace($rootScope.appUrls.signin);
        }, 200);
    }
});
