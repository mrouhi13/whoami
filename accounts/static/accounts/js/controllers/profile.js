app.controller('profileCtrl', function ($scope, $rootScope, $timeout, Auth, Profile, Account, Cookie, Upload, Notification) {
        $scope.credentials = {
            firstName: '',
            lastName: '',
            mobile: '',
            gender: '',
            bio: '',
            avatar: ''
        };

        $scope.genders = [
            {id: 'f', text: 'Female'},
            {id: 'm', text: 'Male'},
            {id: 'n', text: 'No-binary'}
        ];

        $scope.init = function () {
            if (Auth.isAuthenticated()) {
                Account.get().then(function (response) {
                    if (!response.data.content.is_active) {
                        window.location.replace($rootScope.appUrls.profileActivate);
                    }
                }, function (error) {
                    if (error.data.status === 401) {
                        $scope.signout();
                    } else {
                        Notification.error(error.data.message);
                    }
                });

                Cookie.set('token=', Cookie.get('token'), sessionStorage.getItem('rememberMe'));
            } else {
                window.location.replace($rootScope.appUrls.signin);
            }

            if (localStorage.getItem('message') !== null) {
                Notification.custom(localStorage.getItem('message'), localStorage.getItem('messageType'));

                localStorage.removeItem('message');
                localStorage.removeItem('messageType');
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
                    var form = new FormData();
                    form.append("image", file);
                    $('.avatar-frame').css('display', 'block');
                    // Upload.base64DataUrl(file).then(function (urls) {
                    //     $scope.file = urls;
                    //
                    //     $('.avatar-frame').css('display', 'block');
                    // });
                }
            }
        };

        $scope.removeImage = function () {
            $('.avatar-frame').css('display', 'none');
            $('#avatar').attr('src', '');

            $scope.file = null;
        };

        $scope.getProfile = function () {
            Profile.get().then(function (response) {
                $scope.credentials = response.data.content;

                $timeout(function () {
                    $('select').niceSelect('update');
                }, 100);
            }, function (error) {
                if (error.data.status === 401) {
                    $scope.signout();
                } else {
                    Notification.error(error.data.message);
                }
            });
        };

        $scope.updateProfile = function (credentials) {
            Profile.update(credentials).then(function () {
                Notification.success($rootScope.messages.PROFILE_UPDATED);
            }, function (error) {
                if (error.data.status === 401) {
                    $scope.signout();
                } else {
                    Notification.error(error.data.message);
                }
            });
        };

        $scope.signout = function () {
            Auth.signout().then(function () {
            }, function (error) {
                localStorage.setItem('message', error.data.message);
                localStorage.setItem('messageType', $rootScope.notificationType.ERROR);
            });

            Cookie.remove('token');

            $timeout(function () {
                window.location.replace($rootScope.appUrls.signin);
            }, 200);
        };
    }
);
