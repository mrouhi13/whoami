app.controller('passwordResetCtrl', function ($scope, $timeout, Auth, Validator, Notification, APP_URLS, MESSAGES) {
    $scope.credentials = {
        email: ''
    };

    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            window.location.replace(APP_URLS.profile);
        }
    };

    $scope.passwordReset = function (credentials) {
        if (credentials.email.length === 0 || typeof credentials.email === 'undefined') {
            Notification.error(MESSAGES.EMAIL_IS_BLANK);
        } else if (!Validator.emailValidation(credentials.email)) {
            Notification.error(MESSAGES.EMAIL_VALIDATION_ERROR);
        } else {
            Auth.passwordReset(credentials)
                .then(function (response) {
                    Notification.success(response.data.message);
                }, function (error) {
                    Notification.error(error.data.message);
                });
        }
    };
});
