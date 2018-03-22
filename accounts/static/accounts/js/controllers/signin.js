app.controller('signinCtrl', function ($scope, $timeout, Auth, Cookie, Validator, APP_URLS, MESSAGES) {
    $scope.message = '...';
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
        $('.alert-card-content').children('p').removeClass('green').addClass('red');

        if (credentials.email.length === 0 || typeof credentials.email === 'undefined') {
            $scope.message = MESSAGES.EMAIL_IS_BLANK;
        } else if (!Validator.emailValidation(credentials.email)) {
            $scope.message = MESSAGES.EMAIL_VALIDATION_ERROR;
        } else if (credentials.password.length === 0 || typeof credentials.password === 'undefined') {
            $scope.message = MESSAGES.PASSWORD_IS_BLANK;
        } else {
            Auth.signin(credentials)
                .then(function (response) {
                    $('.alert-card-content').children('p').removeClass('red').addClass('green');

                    var days = 0;
                    if ($scope.rememberMe) {
                        days = 60;
                    }

                    Cookie.set('token=', response.data.content.token, days);

                    window.location.replace(APP_URLS.profile);
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
