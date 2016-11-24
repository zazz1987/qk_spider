# -*- coding: utf-8 -*-


from app import db
from app.util.logger import logger
from sqlalchemy.exc import StatementError


def find_company(name, db_session):
    """
    :param db_session:
    :param name:
    :return:


    """
    company = db_session.query(QkCompany).filter_by(name=name).first()
    if company is None:
        company = QkCompany(name=name)
        try:
            db_session.add(company)
            db_session.commit()
        except StatementError as e:
            logger.error(e)
    return company


def update_obj(class_name, company, result_dict, db_session):
    """

    :param cls:
    :param company:
    :param result_dict:
    :return:
    """
    for item in result_dict['results']:
        obj = class_name(qk_company=company)
        for name, value in item.items():
            if hasattr(obj, name):
                setattr(obj, name, value)
        try:
            db_session.add(obj)
            db_session.commit()
        except StatementError as e:
            logger.error(e)


class QkCompany(db.Model):
    __tablename__ = 'qk_company'
    # 公司名称
    name = db.Column(db.Text, primary_key=True)
    # GMP认证数据
    qk_gmp_auth = db.relationship('QkGmpAuth', backref='qk_company')


class QkGmpAuth(db.Model):
    __tablename__ = 'qk_gmp_auth'
    qk_id = db.Column(db.Integer, primary_key=True)
    bbd_xgxx_id = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    company_key = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    location = db.Column(db.Text)
    legalize_scope = db.Column(db.Text)
    issue_date = db.Column(db.Text)
    valid_period = db.Column(db.Text)
    certificate_no = db.Column(db.Text)
    remark = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    province = db.Column(db.Text)
    legalize_version = db.Column(db.Text)
    continue_legalize_scope = db.Column(db.Text)
    continue_date = db.Column(db.Text)
    validdate = db.Column(db.Text)
    bbd_source = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    create_time = db.Column(db.Text)
