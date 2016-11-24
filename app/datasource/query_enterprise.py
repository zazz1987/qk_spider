# -*- coding: utf-8 -*-
import json

from queue import Queue

from app.datasource.bbd.bbd import BBD


def QueryEnterprise():
    data_source = [BBD]
    data_queue = Queue()

    def query(cls, *args, **kwargs):
        key = kwargs.get['key']
        index = kwargs.get['index']
        BBD.query(enterprise_name=key)

        data = dict()
        data['data'] = []
        #其他
        if index == 7:
            #行政处罚
            data['data'].append(BBD.query_ent_admin_pena(company=key, **kwargs))
            #招聘数据
            data['data'].append(BBD.query_recruit(company=key, **kwargs))
            #招中标信息
            data['data'].append(BBD.query_bidwinner(company=key, **kwargs))
            #境外投资
            data['data'].append(BBD.query_overseasinv(company=key, **kwargs))
        return json.dumps(data)
