(function ($) {
    'use strict';

    var input = $('.validate-input .input100');

    $('.input100').each(function () {
        $(this).on('blur', function () {
            if ($(this).val().trim() !== '') {
                $(this).addClass('has-val');
            } else {
                $(this).removeClass('has-val');
            }
        });

        $(this).on('change', function () {
            if ($(this).val() !== null) {
                $(this).addClass('has-val');
                $('select').niceSelect('update');
            } else {
                $(this).removeClass('has-val');
                $('select').niceSelect('update');
            }
        })
    });

    $('.validate-form').on('submit', function () {
        var check = true;

        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) === false) {
                showValidate(input[i]);
                check = false;
            }
        }

        return check;
    });

    $('.validate-form .input100').each(function () {
        $(this).focus(function () {
            hideValidate(this);
        });
    });

    function validate(input) {
        if ($(input).attr('type') === 'email' || $(input).attr('name') === 'email') {
            if ($(input).val().match(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/) == null) {
                return false;
            }
        } else {
            if ($(input).val().trim() === '') {
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
})(jQuery);

$(document).ready(function () {
    'use strict';

    $('select').niceSelect();

    $('.avatar-frame').hover(function () {
        $('.remove-avatar').fadeToggle(500);
    });

    $('.animsition').animsition({
        inClass: 'zoom-in-sm',
        outClass: 'zoom-out-sm',
        timeout: true,
        timeoutCountdown: 500
    });
});
