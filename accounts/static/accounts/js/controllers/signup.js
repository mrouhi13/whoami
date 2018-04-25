app.controller('signupCtrl', function ($scope, $rootScope, $timeout, Auth, Account, Validator, Notification) {
    $scope.credentials = {
        email: '',
        confirmEmail: '',
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

        if (localStorage.getItem('message') !== '') {
            Notification.custom(localStorage.getItem('message'), localStorage.getItem('messageType'));

            localStorage.setItem('message', '');
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
            Auth.signup(credentials).then(function () {
                Auth.signin(credentials).then(function (response) {
                    localStorage.setItem('message', response.data.message);
                    localStorage.setItem('messageType', $rootScope.notificationType.SUCCESS);

                    window.location.replace($rootScope.appUrls.profile);
                }, function (error) {
                    Notification.error(error.data.message);
                });
            }, function (error) {
                Notification.error(error.data.message);
            });
        }
    };
});
