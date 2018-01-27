from rest_framework.response import Response


def response(content, status, message=''):
    return Response({'status': status, 'content': content, 'message': message})
