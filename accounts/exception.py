from rest_framework import views


def exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = views.exception_handler(exc, context)
    if response is not None:
        if isinstance(response.data, list):
            exception_detail = response.data[0]
        else:
            if response.data.setdefault('non_field_errors', None) is not None:
                exception_detail = response.data['non_field_errors'][0]
            elif response.data.setdefault('detail', None) is not None:
                exception_detail = response.data['detail']
            else:
                exception_detail = next(iter(response.data.values()))[0]
                field_name = next(
                    iter(response.data.keys())).replace('_', ' ').capitalize()
                exception_detail = exception_detail.replace('This field',
                                                            field_name)

        response.data = {
            'status': response.status_code,
            'message': exception_detail,
            'content': {}
        }

    return response
