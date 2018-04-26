app.constant('APP_URLS', {
    index: domain + '',
    profile: domain + 'me/',
    signup: domain + 'signup/',
    signin: domain + 'signin/',
    resetPassword: domain + 'password/reset/',
    resetPasswordConfirm: domain + 'password/reset/confirm/',
    profileActivate: domain + 'me/activate/'
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

app.constant('NOTIFICATION_TYPES', {
    NOTICE: 'notice',
    INFO: 'info',
    SUCCESS: 'success',
    ERROR: 'error'
});
