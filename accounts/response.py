from rest_framework.response import Response


def response(content=None, status=None, message=None, headers=None):
    return Response({'status': status, 'message': message, 'content': content},
                    status=status, headers=headers)
