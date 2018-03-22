/**
 * @author Majid Rouhi Kh. <mrouhi13@icloud.com>
 * @version 0.0.2
 * @date Dec 2017
 */

'use strict';
var app = angular.module('profile', ['ngFileUpload']);
var domain = 'http://127.0.0.1:8000/';
var accountsApiBaseUrl = 'accounts/v1/';

app.constant('APP_URLS', {
    index: domain + '',
    profile: domain + 'me/',
    signup: domain + 'signup/',
    signin: domain + 'signin/',
    resetPassword: domain + 'password/reset/',
    resetPasswordConfirm: domain + 'password/reset/confirm/'
});

app.constant('API_URLS', {
    profile: domain + accountsApiBaseUrl + 'me/',
    account: domain + accountsApiBaseUrl + 'account/',
    createUser: domain + accountsApiBaseUrl + 'users/create/',
    deleteUser: domain + accountsApiBaseUrl + 'users/delete/',
    activateUser: domain + accountsApiBaseUrl + 'users/activate/',
    setEmail: domain + accountsApiBaseUrl + 'email/',
    setPassword: domain + accountsApiBaseUrl + 'password/',
    resetPassword: domain + accountsApiBaseUrl + 'password/reset/',
    resetPasswordConfirm: domain + accountsApiBaseUrl + 'password/reset/confirm/',
    createToken: domain + accountsApiBaseUrl + 'token/create/',
    destroyToken: domain + accountsApiBaseUrl + 'token/destroy/'
});
