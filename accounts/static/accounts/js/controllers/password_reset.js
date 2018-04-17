app.controller('passwordResetCtrl', function ($scope, $rootScope, $timeout, Auth, Validator, Notification) {
    $scope.credentials = {
        email: ''
    };

    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            window.location.replace($rootScope.AppUrls.profile);
        }
    };

    $scope.passwordReset = function (credentials) {
        if (credentials.email.length === 0 || typeof credentials.email === 'undefined') {
            Notification.error($rootScope.messages.EMAIL_IS_BLANK);
        } else if (!Validator.emailValidation(credentials.email)) {
            Notification.error($rootScope.messages.EMAIL_VALIDATION_ERROR);
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
