app.factory('Notification', function () {
    var myStack = {
        text: null,
        type: null,
        addclass: 'custom',
        icon: false,
        mouse_reset: false,
        buttons: {
            sticker: false,
            closer: false
        },
        animate: {
            animate: true,
            in_class: 'bounceIn',
            out_class: 'bounceOut'
        }
    };

    return {
        notice: function (message) {
            myStack.text = message;

            PNotify.removeAll();

            notice = new PNotify(myStack);
        },
        info: function (message) {
            myStack.text = message;
            myStack.type = 'info';

            PNotify.removeAll();

            notice = new PNotify(myStack);
        },
        success: function (message) {
            myStack.text = message;
            myStack.type = 'success';

            PNotify.removeAll();

            notice = new PNotify(myStack);
        },
        error: function (message) {
            myStack.text = message;
            myStack.type = 'error';

            PNotify.removeAll();

            notice = new PNotify(myStack);
        },
        custom: function (message, type) {
            myStack.text = message;
            myStack.type = type;

            PNotify.removeAll();

            notice = new PNotify(myStack);
        }
    }
});
