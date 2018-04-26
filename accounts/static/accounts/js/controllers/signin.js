app.controller('signinCtrl', function ($scope, $rootScope, Auth, Account, Cookie, Validator, Notification) {
    $scope.rememberMe = false;
    $scope.credentials = {
        email: '',
        password: ''
    };

    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            Account.get().then(function (response) {
                $scope.isActive = response.data.content.is_active;

                if ($scope.isActive) {
                    window.location.replace($rootScope.appUrls.profile);
                } else {
                    window.location.replace($rootScope.appUrls.profileConfirm);
                }
            }, function (error) {
                Notification.error(error.data.message);
            });
        }

        if (localStorage.getItem('message') !== null) {
            Notification.custom(localStorage.getItem('message'), localStorage.getItem('messageType'));

            localStorage.removeItem('message');
            localStorage.removeItem('messageType');
        }
    };

    $scope.signin = function (credentials) {
        if (credentials.email.length === 0 || typeof credentials.email === 'undefined') {
            Notification.error($rootScope.messages.EMAIL_IS_BLANK);
        } else if (!Validator.emailValidation(credentials.email)) {
            Notification.error($rootScope.messages.EMAIL_VALIDATION_ERROR);
        } else if (credentials.password.length === 0 || typeof credentials.password === 'undefined') {
            Notification.error($rootScope.messages.PASSWORD_IS_BLANK);
        } else {
            Auth.signin(credentials).then(function (response) {
                var days = 0;
                if ($scope.rememberMe) {
                    days = 60;
                }

                Cookie.set('token=', response.data.content.token, days);

                localStorage.setItem('rememberMe', days);
                localStorage.setItem('message', response.data.message);
                localStorage.setItem('messageType', $rootScope.notificationType.SUCCESS);

                if (response.data.content.is_active === false) {
                    localStorage.setItem('firstSignin', false);

                    window.location.replace($rootScope.appUrls.profileConfirm);
                } else {
                    window.location.replace($rootScope.appUrls.profile);
                }
            }, function (error) {
                Notification.error(error.data.message);
            });
        }
    };
});
