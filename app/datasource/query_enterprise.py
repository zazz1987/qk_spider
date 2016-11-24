# -*- coding: utf-8 -*-
from queue import Queue

from app.datasource.bbd.bbd import BBD


class QueryEnterprise():
    data_source = [BBD]
    data_queue = Queue()

    @classmethod
    def query(cls, *args, **kwargs):
        key = kwargs.get('key')
        index = kwargs.get('index')
        page_size = kwargs.get('page_size')
        # BBD.query(enterprise_name=key, page_size=page_size)


    @classmethod
    def company_list(cls, query, page_size=None):
        result = BBD.query_companysearch2(query=query, page_size=page_size)
        return result.text
