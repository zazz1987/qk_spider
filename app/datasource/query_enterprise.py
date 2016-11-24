# -*- coding: utf-8 -*-
from queue import Queue

from app.datasource.bbd.bbd import BBD


def QueryEnterprise():
    data_source = [BBD]
    data_queue = Queue()

    def query(cls, *args, **kwargs):
        key = kwargs.get['key']
        index = kwargs.get['index']
        BBD.query(enterprise_name=key)
