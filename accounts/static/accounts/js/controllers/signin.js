app.controller('signinCtrl', function ($scope, $http, $timeout, Auth, Cookie) {
    $scope.message = '';
    $scope.rememberMe = false;
    $scope.credentials = {
        email: '',
        password: ''
    };

    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            window.location.replace('/profile');
        }
    };

    $scope.signin = function (credentials) {
        Auth.signin(credentials)
            .then(function (response) {
                $('.alert-card-content').children('p').removeClass('red');
                $('.alert-card-content').children('p').addClass('green');

                var days = 0;
                if ($scope.rememberMe) {
                    days = 60;
                }

                Cookie.set('auth-token=', response.data.content.token, days);

                window.location.replace('/accounts');
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
    };
});
