app.controller('passwordResetCtrl', function ($scope, $rootScope, $timeout, Auth, Account, Validator, Notification) {
    $scope.credentials = {
        email: ''
    };

    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            Account.get().then(function (response) {
                if (response.data.content.is_active) {
                    window.location.replace($rootScope.appUrls.profile);
                } else {
                    window.location.replace($rootScope.appUrls.profileActivate);
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

    $scope.passwordReset = function (credentials) {
        if (credentials.email.length === 0 || typeof credentials.email === 'undefined') {
            Notification.error($rootScope.messages.EMAIL_IS_BLANK);
        } else if (!Validator.emailValidation(credentials.email)) {
            Notification.error($rootScope.messages.EMAIL_VALIDATION_ERROR);
        } else {
            Auth.passwordReset(credentials).then(function (response) {
                Notification.success(response.data.message);
            }, function (error) {
                Notification.error(error.data.message);
            });
        }
    };
});
