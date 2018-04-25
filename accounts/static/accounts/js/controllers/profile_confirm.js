app.controller('profileConfirmCtrl', function ($scope, $rootScope, $timeout, Auth, Account, Cookie, Notification) {
    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            Account.get().then(function (response) {
                $scope.isActive = response.data.content.is_active;

                if ($scope.isActive) {
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

        if (localStorage.getItem('message') !== '') {
            Notification.custom(localStorage.getItem('message'), localStorage.getItem('messageType'));

            localStorage.setItem('message', '');
        }

        $scope.firstSignin = localStorage.getItem('firstSignin');
    };

    $scope.resendConfirmationEmail = function () {
        Auth.sendConfirmationEmail(credentials).then(function (response) {
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
