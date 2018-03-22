app.controller('signupCtrl', function ($scope, $timeout, Auth, Validator, APP_URLS, MESSAGES) {
    $scope.message = '...';
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
        $('.alert-card-content').children('p').removeClass('green').addClass('red');

        if (credentials.email.length === 0 || typeof credentials.email === 'undefined') {
            $scope.message = MESSAGES.EMAIL_IS_BLANK;
        } else if (!Validator.emailValidation(credentials.email)) {
            $scope.message = MESSAGES.EMAIL_VALIDATION_ERROR;
        } else if (credentials.confirmEmail.length === 0 || typeof credentials.confirmEmail === 'undefined') {
            $scope.message = MESSAGES.CONFIRM_EMAIL_IS_BLANK;
        } else if (!Validator.emailValidation(credentials.confirmEmail)) {
            $scope.message = MESSAGES.CONFIRM_EMAIL_VALIDATION_ERROR;
        } else if (credentials.email !== credentials.confirmEmail) {
            $scope.message = MESSAGES.PASSWORD_MISMATCH_ERROR;
        } else if (credentials.password.length === 0 || typeof credentials.password === 'undefined') {
            $scope.message = MESSAGES.PASSWORD_IS_BLANK;
        } else {
            Auth.signup(credentials)
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
