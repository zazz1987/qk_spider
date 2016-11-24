# -*- coding: utf-8 -*-

from unittest import TestCase
from app import create_app
import json
from app.enterprise.qk_models import *


def convert_obj(obj, *complex_name):
    convert = {}
    for name, value in obj.__dict__.items():
        if value is None:
            continue
        if name[0] is not '_' and name is not 'person_id' \
                and name is not 'bank_id' and name is not 'id':
            convert[name] = value
    for item in complex_name:
        complex_classes = getattr(obj, item)
        complex_list = []
        for temp in complex_classes:
            if item is 'bank_card':
                complex_list.append(convert_obj(temp, 'records'))
            else:
                complex_list.append(convert_obj(temp))
        convert[item] = complex_list
    return convert


class TestPyTransform(TestCase):
    def setUp(self):
        self.app = create_app('development')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def test_query(self):
        company = '北京利祥制药有限公司'
        test_data = """
        {
 "msg": "ok",
 "rsize": 3,
 "total": 3,
 "results": [
  {
   "bbd_xgxx_id": "00105c1df4c29e8d5b6fab60bec788d1",
   "bbd_dotime": "2015-03-27",
   "bbd_uptime": 1547398309,
   "company_key": "北京利祥制药有限公司",
   "company_name": "北京利祥制药有限公司",
   "location": "北京市顺义区林河工业开发区顺康路64号",
   "legalize_scope": "冻干粉针剂",
   "issue_date": "2009-03-12",
   "valid_period": "2014-03-11",
   "certificate_no": "K4845",
   "remark": null,
   "bbd_url": "",
   "province": "北京",
   "legalize_version": "按1998年修订药品GMP认证",
   "continue_legalize_scope": null,
   "continue_date": null,
   "validdate": null,
   "bbd_source": "",
   "bbd_type": "qyxx_gmpauth_prod_cert",
   "create_time": ""
  },
  {
   "bbd_xgxx_id": "9001c7f5a1f37f143463e78d1dde80fc",
   "bbd_dotime": "2015-03-13",
   "bbd_uptime": 1547398292,
   "company_key": "北京利祥制药有限公司",
   "company_name": "北京利祥制药有限公司",
   "location": null,
   "legalize_scope": "原料药(磷酸肌酸钠、泛酸钠)",
   "issue_date": "2005-09-14",
   "valid_period": "2010-09-13",
   "certificate_no": "京G0161",
   "remark": null,
   "bbd_url": "",
   "province": "北京",
   "legalize_version": "按1998年修订药品GMP认证",
   "continue_legalize_scope": null,
   "continue_date": null,
   "validdate": null,
   "bbd_source": "",
   "bbd_type": "qyxx_gmpauth_prod_cert",
   "create_time": ""
  },
  {
   "bbd_xgxx_id": "160a9076805e2b8a61fee390c11c0174",
   "bbd_dotime": "2015-03-12",
   "bbd_uptime": 1547398292,
   "company_key": "北京利祥制药有限公司",
   "company_name": "北京利祥制药有限公司",
   "location": "北京市顺义区林河工业开发区顺康路64号",
   "legalize_scope": "粉针剂(头孢菌素类)",
   "issue_date": "2005-06-20",
   "valid_period": "2010-06-19",
   "certificate_no": "G3409",
   "remark": null,
   "bbd_url": "",
   "province": "北京市",
   "legalize_version": "按1998年修订药品GMP认证",
   "continue_legalize_scope": null,
   "continue_date": null,
   "validdate": null,
   "bbd_source": "",
   "bbd_type": "qyxx_gmpauth_prod_cert",
   "create_time": ""
  }
 ],
 "err_code": 0
}
    """
        unit = find_company(company, db.session)
        result_dict = json.loads(test_data)
        save_obj(QkGmpAuth, unit, result_dict, db.session)
