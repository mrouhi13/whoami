app.controller('signupCtrl', function ($scope, $rootScope, $timeout, Auth, Validator, Notification) {
    $scope.credentials = {
        email: '',
        confirmEmail: '',
        password: ''
    };

    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            window.location.replace($rootScope.appUrls.profile);
        }
    };

    $scope.signup = function (credentials) {
        if (credentials.email.length === 0 || typeof credentials.email === 'undefined') {
            Notification.error($rootScope.messages.EMAIL_IS_BLANK);
        } else if (!Validator.emailValidation(credentials.email)) {
            Notification.error($rootScope.messages.EMAIL_VALIDATION_ERROR);
        } else if (credentials.confirmEmail.length === 0 || typeof credentials.confirmEmail === 'undefined') {
            Notification.error($rootScope.messages.CONFIRM_EMAIL_IS_BLANK);
        } else if (!Validator.emailValidation(credentials.confirmEmail)) {
            Notification.error($rootScope.messages.CONFIRM_EMAIL_VALIDATION_ERROR);
        } else if (credentials.email !== credentials.confirmEmail) {
            Notification.error($rootScope.messages.PASSWORD_MISMATCH_ERROR);
        } else if (credentials.password.length === 0 || typeof credentials.password === 'undefined') {
            Notification.error($rootScope.messages.PASSWORD_IS_BLANK);
        } else {
            Auth.signup(credentials)
                .then(function () {
                    Notification.success($rootScope.messages.REGISTRATION_SUCCESSFUL);
                    window.location.replace($rootScope.appUrls.signupSuccessful);
                }, function (error) {
                    Notification.error(error.data.message);
                });
        }
    };
});
