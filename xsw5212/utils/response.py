from rest_framework.views import Response


class APIResponse(Response):
    def __init__(self, data_status, data_msg, data_res=None, status=None, headers=None, **kwargs):
        data = {
            'status': data_status,
            'msg': data_msg
        },
        if data_res:
            data_msg['data_res'] = data_res
        super().__init__(data=data, status=status, headers=headers, **kwargs)