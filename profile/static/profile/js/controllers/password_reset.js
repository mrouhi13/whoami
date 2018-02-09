app.controller('passwordResetCtrl', function ($scope, $rootScope, $http, $timeout, Auth) {
    $scope.message = '';
    $scope.credentials = {
        email: ''
    };

    $scope.init = function () {
        if (Auth.isAuthenticated($rootScope.token)) {
            // window.location.replace("/profile");
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
    };
});