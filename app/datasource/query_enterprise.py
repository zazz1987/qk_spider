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

        result = {}
        #其他
        if index == 7:
            #行政处罚
            result['bbd_ent_admin_pena'] = BBD.query_ent_admin_pena(company=key, **kwargs)
            #招聘数据
            result['bbd_recruit'] = BBD.query_recruit(company=key, **kwargs)
            #招中标信息
            result['bbd_bidwinner'] = BBD.query_bidwinner(company=key, **kwargs)
            #境外投资
            result['bbd_overseasinv'] = BBD.query_overseasinv(company=key, **kwargs)
        return json.dumps(result)
