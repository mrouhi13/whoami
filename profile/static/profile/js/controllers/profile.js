app.controller('profileCtrl', function ($scope, $http, Auth, Upload) {
    $scope.init = function () {
        if (!Auth.isAuthenticated()) {
            window.location.replace("/signin");
        }
    };

    $scope.uploadFiles = function (file, errFiles) {
        if (typeof errFiles[0] !== "undefined") {
            if (errFiles[0].$error === "pattern") {
                $scope.UploadeImageError = "Only image file";
                $scope.ImageUpladeErrorShow = true;
            }
            else if (errFiles[0].$error === "maxSize") {
                $scope.UploadeImageError = "Image file size is too large";
                $scope.ImageUpladeErrorShow = true;
            }
        } else {
            if (file !== null) {
                Upload.base64DataUrl(file).then(function (urls) {
                    $scope.file = urls;

                    setTimeout(function () {
                        $('.avatar-frame').css('display', 'block');
                        $('.avatar-frame').css('width', $('.file-view').width() + 16);
                    }, 50);
                });
            }
        }
    };

    $scope.RemoveImage = function (data, event) {
        $('.avatar-frame').css('display', 'none');

        $scope.file = null;
    };

    $scope.signout = function () {
        Auth.unsetUser();
        window.location.replace("/signin");
    }
});


app.controller('ApplicationCtrl', function ($scope, USER_ROLES, Auth) {
  $scope.currentUser = null;
  $scope.userRoles = USER_ROLES;
  $scope.isAuthorized = Auth.isAuthorized;

  $scope.setCurrentUser = function (user) {
    $scope.currentUser = user;
  };

      $scope.uploadFiles = function (file, errFiles) {
        if (typeof errFiles[0] !== "undefined") {
            if (errFiles[0].$error === "pattern") {
                $scope.UploadeImageError = "Only image file";
                $scope.ImageUpladeErrorShow = true;
            }
            else if (errFiles[0].$error === "maxSize") {
                $scope.UploadeImageError = "Image file size is too large";
                $scope.ImageUpladeErrorShow = true;
            }
        } else {
            if (file !== null) {
                Upload.base64DataUrl(file).then(function (urls) {
                    $scope.file = urls;

                    setTimeout(function () {
                        $('.avatar-frame').css('display', 'block');
                        $('.avatar-frame').css('width', $('.file-view').width() + 16);
                    }, 50);
                });
            }
        }
    };

    $scope.RemoveImage = function (data, event) {
        $('.avatar-frame').css('display', 'none');

        $scope.file = null;
    };

    $scope.signout = function () {
        Auth.unsetUser();
        window.location.replace("/signin");
    }
})