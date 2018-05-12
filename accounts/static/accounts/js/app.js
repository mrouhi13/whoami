/**
 * @author Majid Rouhi Kh. <mrouhi13@icloud.com>
 * @version 0.0.2
 * @date Dec 2017
 */

'use strict';
var app = angular.module('accounts', ['ngFileUpload']);
var domain = 'http://127.0.0.1:8000/';
var accountsApiBaseUrl = 'accounts/v1/';

angular.module('accounts')
    .run(function ($rootScope, APP_URLS, API_URLS, MESSAGES, NOTIFICATION_TYPES) {
        $rootScope.appUrls = APP_URLS;
        $rootScope.apiUrls = API_URLS;
        $rootScope.messages = MESSAGES;
        $rootScope.notificationType = NOTIFICATION_TYPES;
    });
