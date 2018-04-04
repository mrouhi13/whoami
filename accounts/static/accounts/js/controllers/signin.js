app.controller('signinCtrl', function ($scope, Auth, Cookie, Validator, Notification, APP_URLS, MESSAGES) {
    $scope.rememberMe = false;
    $scope.credentials = {
        email: '',
        password: ''
    };

    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            window.location.replace(APP_URLS.profile);
        }
    };

    $scope.signin = function (credentials) {
        if (credentials.email.length === 0 || typeof credentials.email === 'undefined') {
            Notification.error(MESSAGES.EMAIL_IS_BLANK);
        } else if (!Validator.emailValidation(credentials.email)) {
            Notification.error(MESSAGES.EMAIL_VALIDATION_ERROR);
        } else if (credentials.password.length === 0 || typeof credentials.password === 'undefined') {
            Notification.error(MESSAGES.PASSWORD_IS_BLANK);
        } else {
            Auth.signin(credentials)
                .then(function (response) {
                    var days = 0;
                    if ($scope.rememberMe) {
                        days = 60;
                    }

                    Cookie.set('token=', response.data.content.token, days); // TODO: renew cookie on page refresh.

                    window.location.replace(APP_URLS.profile);
                }, function (error) {
                    Notification.error(error.data.message);
                });
        }
    };
});
