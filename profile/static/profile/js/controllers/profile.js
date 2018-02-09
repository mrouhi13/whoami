app.controller('profileCtrl', function ($scope, $http, $timeout, Auth, Cookie, Upload) {
    $scope.init = function () {
        if (!Auth.isAuthenticated()) {
            window.location.replace('/signin');
        }
    };

    $scope.uploadFiles = function (file, errFiles) {
        if (typeof errFiles[0] !== 'undefined') {
            if (errFiles[0].$error === 'pattern') {
                $scope.UploadeImageError = 'فایل ارسال شده مورد قبول نیست';
                $scope.ImageUpladeErrorShow = true;
            }
            else if (errFiles[0].$error === 'maxSize') {
                $scope.UploadeImageError = 'حجم فایل ارسال شده بیش از حد مجاز است.';
                $scope.ImageUpladeErrorShow = true;
            }
        } else {
            if (file !== null) {
                Upload.base64DataUrl(file).then(function (urls) {
                    $scope.file = urls;

                    $timeout(function () {
                        $('.avatar-frame').css('display', 'block');
                        $('.avatar-frame').css('width', $('.file-view').width() + 16);
                    }, 50);
                });
            }
        }
    };

    $scope.RemoveImage = function () {
        $('.avatar-frame').css('display', 'none');

        $scope.file = null;
    };

    $scope.signout = function () {
        Auth.signout()
            .then(function () {
                Cookie.remove('token');

                window.location.replace('/signin');
            }, function (error) {
                $scope.error = error.data.message;
                $scope.showCard = true;
            });
    }
});