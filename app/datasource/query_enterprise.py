# -*- coding: utf-8 -*-
from queue import Queue

from app.datasource.bbd.bbd import BBD


class QueryEnterprise():
    data_source = [BBD]
    data_queue = Queue()

    @classmethod
    def query(cls, *args, **kwargs):
        key = kwargs.get['key']
        index = kwargs.get['index']
        BBD.query(enterprise_name=key)

    @classmethod
    def company_list(cls, query):
        result = BBD.query_companysearch2(query=query)
        return result