from rest_framework import generics
from rest_framework.response import Response
# 重写查询返回格式
class ReListView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        # 重写response 返回信息
        response = {'retcode': 200, 'msg': '查询成功'}

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # 将原来的结果放进response字典
        response['retlist'] = serializer.data
        return Response(response)