app.controller('passwordResetCtrl', function ($scope, $timeout, Auth, Validator, APP_URLS, MESSAGES) {
    $scope.message = '...';
    $scope.credentials = {
        email: ''
    };

    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            window.location.replace(APP_URLS.profile);
        }
    };

    $scope.passwordReset = function (credentials) {
        $('.alert-card-content').children('p').removeClass('green').addClass('red');

        if (credentials.email.length === 0 || typeof credentials.email === 'undefined') {
            $scope.message = MESSAGES.EMAIL_IS_BLANK;
        } else if (!Validator.emailValidation(credentials.email)) {
            $scope.message = MESSAGES.EMAIL_VALIDATION_ERROR;
        } else {
            Auth.passwordReset(credentials)
                .then(function (response) {
                    $('.alert-card-content').children('p').removeClass('red').addClass('green');

                    $scope.message = response.data.message;
                }, function (error) {
                    $scope.message = error.data.message;
                });
        }

        $('.alert-card').fadeToggle('slow');
        $('.login100-form-title').hide();

        $timeout(function () {
            $('.alert-card').hide();
            $('.login100-form-title').fadeToggle(1500);
        }, 2000);
    };
});
