# -*- coding: utf-8 -*-
import json

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
        BBD.query(enterprise_name=key, page_size=page_size)

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

    @classmethod
    def query_basic(cls, *args, **kwargs):
        enterprise_name = kwargs.get('enterprise_name')
        result = BBD.query_qyxx_jbxx(company=enterprise_name)
        return result

    @classmethod
    def query_related_party(cls, *args, **kwargs):
        enterprise_name = kwargs.get('enterprise_name')
        result = BBD.query_rel(company=enterprise_name)
        return result

    @classmethod
    def query_qualifiction(cls, *args, **kwargs):
        #TODO: 未完成
        enterprise_name = kwargs.get('enterprise_name')
        r1 = BBD.query_licence_pros(company=enterprise_name)
        r2 = BBD.query_qua_comm_cons(company=enterprise_name)
        r3 = BBD.query_licence_bui_cons(company=enterprise_name)
        r4 = BBD.query_qyxx_gcjljz(company=enterprise_name)
        r5 = BBD.query_qua_itsys_sup(company=enterprise_name)
        r6 = BBD.query_cert_soft_ent_pro(company=enterprise_name)
        r7 = BBD.query_licence_ind_pro(company=enterprise_name)
        r8 = BBD.query_qua_pes_pro(company=enterprise_name)
        r9 = BBD.query_licence_food_pro(company=enterprise_name)
        r10 = BBD.query_licence_medi_pro(company=enterprise_name)
        r11 = BBD.query_licence_medi_oper(company=enterprise_name)
        r12 = BBD.query_qua_cos_pro(company=enterprise_name)
        r13 = BBD.query_gmp_auth(company=enterprise_name)
        r = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13]
        d = {}
        for item in r:
            d.update(r)


    @classmethod
    def company_list(cls, query, page_size=None):
        result = BBD.query_companysearch2(query=query, page_size=page_size)
        return result
