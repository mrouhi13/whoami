'use strict';
var app = angular.module('profile', ['ngFileUpload']);

app.constant("APP_CONFIG", {
    appVrsion: '0.0.1',
    appProducer: 'Majid Rouhi Kh.',
    apiUrl: "http://127.0.0.1:8000/api/v1/"
});