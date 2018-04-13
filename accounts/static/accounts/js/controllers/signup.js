app.controller('signupCtrl', function ($scope, $timeout, Auth, Validator, Notification, APP_URLS, MESSAGES) {
    $scope.credentials = {
        email: '',
        confirmEmail: '',
        password: ''
    };

    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            window.location.replace(APP_URLS.profile);
        }
    };

    $scope.signup = function (credentials) {
        if (credentials.email.length === 0 || typeof credentials.email === 'undefined') {
            Notification.error(MESSAGES.EMAIL_IS_BLANK);
        } else if (!Validator.emailValidation(credentials.email)) {
            Notification.error(MESSAGES.EMAIL_VALIDATION_ERROR);
        } else if (credentials.confirmEmail.length === 0 || typeof credentials.confirmEmail === 'undefined') {
            Notification.error(MESSAGES.CONFIRM_EMAIL_IS_BLANK);
        } else if (!Validator.emailValidation(credentials.confirmEmail)) {
            Notification.error(MESSAGES.CONFIRM_EMAIL_VALIDATION_ERROR);
        } else if (credentials.email !== credentials.confirmEmail) {
            Notification.error(MESSAGES.PASSWORD_MISMATCH_ERROR);
        } else if (credentials.password.length === 0 || typeof credentials.password === 'undefined') {
            Notification.error(MESSAGES.PASSWORD_IS_BLANK);
        } else {
            Auth.signup(credentials)
                .then(function () {
                    Notification.success(MESSAGES.REGISTRATION_SUCCESSFUL);
                }, function (error) {
                    Notification.error(error.data.message);
                });
        }
    };
});
