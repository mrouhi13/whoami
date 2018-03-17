from rest_framework import views


def exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = views.exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        if response.data.setdefault('non_field_errors', None) is not None:
            exception_detail = response.data['non_field_errors'][0]
        elif response.data.setdefault('detail', None) is None:
            exception_detail = next(iter(response.data.values()))[0]
            exception_detail = exception_detail.replace(
                'This field', next(iter(response.data.keys())))
        else:
            exception_detail = response.data['detail']

        response.data = {'status': response.status_code,
                         'message': exception_detail, 'content': {}}

    return response
