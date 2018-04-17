app.controller('profileCtrl', function ($scope, $rootScope, $timeout, Auth, Profile, Cookie, Upload, Notification) {
        $scope.credentials = {
            firstName: '',
            lastName: '',
            mobile: '',
            gender: '',
            bio: '',
            avatar: ''
        };

        $scope.genders = [
            {id: 'f', text: 'زن'},
            {id: 'm', text: 'مرد'},
            {id: 'n', text: 'دیگر'}
        ];

        $scope.init = function () {
            if (!Auth.isAuthenticated()) {
                window.location.replace($rootScope.appUrls.signin);
            }

            $scope.getProfile();
        };

        $scope.uploadFile = function (file, errFiles) {
            if (typeof errFiles[0] !== 'undefined') {
                if (errFiles[0].$error === 'pattern') {
                    Notification.error($rootScope.messages.UPLOAD_FILE_ERROR);
                } else if (errFiles[0].$error === 'maxSize') {
                    Notification.error($rootScope.messages.FILE_SIZE_ERROR);
                }
            } else {
                if (file !== null) {
                    Upload.base64DataUrl(file).then(function (urls) {
                        $scope.file = urls;

                        $timeout(function () {
                            $('.avatar-frame').css('display', 'block').css('width', $('.file-view').width() + 16);
                        }, 50);
                    });
                }
            }
        };

        $scope.removeImage = function () {
            $('.avatar-frame').css('display', 'none');

            $scope.file = null;
        };

        $scope.getProfile = function () {
            Profile.get()
                .then(function (response) {
                    $scope.credentials = response.data.content; // TODO: check has value when data loaded.
                }, function (error) {
                    Notification.error(error.data.message);
                });
        };

        $scope.updateProfile = function (credentials) {
            Profile.update(credentials)
                .then(function (response) {
                    Notification.success(response.data.message);
                }, function (error) {
                    Notification.error(error.data.message);
                });
        };

        $scope.signout = function () {
            Auth.signout()
                .then(function () {
                    Cookie.remove('token');

                    window.location.replace($rootScope.appUrls.signin);
                }, function (error) {
                    Notification.error(error.data.message);
                });
        }
    }
);
