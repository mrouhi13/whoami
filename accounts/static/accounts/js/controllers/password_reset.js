app.controller('passwordResetCtrl', function ($scope, $http, $timeout, Auth, Cookie) {
    $scope.message = '';
    $scope.credentials = {
        email: ''
    };

    $scope.init = function () {
        if (Auth.isAuthenticated()) {
            window.location.replace('/accounts');
        }
    };

    $scope.passwordReset = function (credentials) {
        Auth.passwordReset(credentials)
            .then(function (response) {
                $('.alert-card-content').children('p').removeClass('red');
                $('.alert-card-content').children('p').addClass('green');

                $scope.message = response.data.message;

                $('.alert-card').fadeToggle('slow');
                $('.login100-form-title').hide();

                $timeout(function () {
                    $('.alert-card').hide();
                    $('.login100-form-title').fadeToggle(1500);
                }, 10000);
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
