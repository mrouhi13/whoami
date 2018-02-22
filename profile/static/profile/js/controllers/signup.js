app.controller('signupCtrl', function ($scope, $http, $timeout, Auth, Cookie) {
    $scope.message = '';
    $scope.credentials = {
        email: '',
        confirmEmail: '',
        password: ''
    };

    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            window.location.replace('/profile');
        }
    };

    $scope.signup = function (credentials) {
        if (credentials.email != credentials.confirmEmail) {
            $('.alert-card-content').children('p').removeClass('green');
            $('.alert-card-content').children('p').addClass('red');

            $scope.message = 'ایمیل و تکرار ایمیل یکسان نیست.';

            $('.alert-card').fadeToggle('slow');
            $('.login100-form-title').hide();

            $timeout(function () {
                $('.alert-card').hide();
                $('.login100-form-title').fadeToggle(1500);
            }, 2000);
        } else {
            Auth.signup(credentials)
                .then(function (response) {
                    $('.alert-card-content').children('p').removeClass('red');
                    $('.alert-card-content').children('p').addClass('green');

                    $scope.message = response.data.message;

                    $('.alert-card').fadeToggle('slow');
                    $('.login100-form-title').hide();

                    $timeout(function () {
                        $('.alert-card').hide();
                        $('.login100-form-title').fadeToggle(10000);
                    }, 2000);
                }, function (error) {
                    $('.alert-card-content').children('p').removeClass('green');
                    $('.alert-card-content').children('p').addClass('red');

                    $scope.message = error.data.message;

                    $('.alert-card').fadeToggle('slow');
                    $('.login100-form-title').hide();

                    $timeout(function () {
                        $('.alert-card').hide();
                        $('.login100-form-title').fadeToggle(1500);
                    }, 2000);
                });
        }
    };
});
