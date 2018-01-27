app.service('Session', function () {
  this.create = function (sessionId, userToken, userRole) {
    this.id = sessionId;
    this.userToken = userToken;
    this.userRole = userRole;
  };
  this.destroy = function () {
    this.id = null;
    this.userToken = null;
    this.userRole = null;
  };
})