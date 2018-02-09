app.controller('signupCtrl', function ($scope, $http, Auth, APP_CONFIG) {
    $scope.init = function () {
        if (Auth.isAuthenticate()) {
            window.location.replace("/profile");
        }
    };

    $scope.register = function (data) {
        if (data.email != data.confirmEmail) {
            console.log('email err');
        } else {
            var content = {
                "email": data.email,
                "password": data.password
            }

            $http.post(APP_CONFIG.api + "signup/", content)
                .then(function (response) {
                    if (response.status == 200) {
                        Auth.setUser(response.data.token);
                        window.location.replace("/profile");
                    }
                    console.log(response);
                }, function (err) {
                    console.log(err);
                });
        }
    };
});
