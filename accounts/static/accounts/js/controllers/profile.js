app.controller('profileCtrl', function ($scope, $timeout, Auth, Profile, Cookie, Upload, APP_URLS, MESSAGES) {
        $scope.message = '...';
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
                window.location.replace(APP_URLS.signin);
            }

            $scope.getProfile();
        };

        $scope.uploadFile = function (file, errFiles) {
            $('.alert-card-content').children('p').removeClass('green').addClass('red');

            if (typeof errFiles[0] !== 'undefined') {
                if (errFiles[0].$error === 'pattern') {
                    $scope.message = MESSAGES.UPLOAD_FILE_ERROR;
                } else if (errFiles[0].$error === 'maxSize') {
                    $scope.message = MESSAGES.FILE_SIZE_ERROR;
                }

                $('.alert-card').fadeToggle('slow');
                $('.login100-form-title').hide();

                $timeout(function () {
                    $('.alert-card').hide();
                    $('.login100-form-title').fadeToggle(1500);
                }, 2000);
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
            $('.alert-card-content').children('p').removeClass('green').addClass('red');

            Profile.get()
                .then(function (response) {
                    $('.alert-card-content').children('p').removeClass('red').addClass('green');

                    $scope.message = response.data.message;
                    $scope.credentials = response.data.content;
                }, function (error) {
                    $scope.message = error.data.message;

                    $('.alert-card').fadeToggle('slow');
                    $('.login100-form-title').hide();

                    $timeout(function () {
                        $('.alert-card').hide();
                        $('.login100-form-title').fadeToggle(1500);
                    }, 2000);
                });
        };

        $scope.updateProfile = function (credentials) {
            $('.alert-card-content').children('p').removeClass('green').addClass('red');

            if ($('select, ul').dropdown('value') !== '?') {
                $scope.credentials.gender = $('select, ul').dropdown('value').split(':')[1];
            }
            console.log($scope.credentials);
            Profile.update(credentials)
                .then(function (response) {
                    $('.alert-card-content').children('p').removeClass('red').addClass('green');

                    $scope.message = response.data.message;
                }, function (error) {
                    $scope.message = error.data.message;
                });

            $('.alert-card').fadeToggle('slow');
            $('.login100-form-title').hide();

            $timeout(function () {
                $('.alert-card').hide();
                $('.login100-form-title').fadeToggle(1500);
            }, 2000);
        };

        $scope.signout = function () {
            Auth.signout()
                .then(function () {
                    Cookie.remove('token');

                    window.location.replace(APP_URLS.signin);
                }, function (error) {
                    $scope.error = error.data.message;
                    $scope.showCard = true;
                });
        }
    }
);
