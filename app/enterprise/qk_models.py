# -*- coding: utf-8 -*-


from app import db
from app.util.logger import logger
from sqlalchemy.exc import StatementError


def find_company(name, db_session):
    """
    :param
    db_session:
    :param
    name:
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


def save_obj(class_name, company, result_dict, db_session):
    """

    :param
    class_name:
    :param
    company:
    :param
    result_dict:
    :param
    db_session:
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


# 公司名称字典
class QkCompany(db.Model):
    __tablename__ = 'qk_company'
    # 公司名称
    name = db.Column(db.Text, primary_key=True)
    # GMP认证数据
    qk_gmp_auth = db.relationship('QkGmpAuth', backref='qk_company')
    # 企业工商数据备案信息
    qk_qyxx_baxx = db.relationship('QkQyxxBaxx', backref='qk_company')
    # 企业采矿权许可数据
    qk_licence_mining = db.relationship('QkLicenceMining', backref='qk_company')
    # 分支机构数据
    qk_qyxx_fzjg_extend = db.relationship('QkQyxxFzjgExtend', backref='qk_company')
    # 企业工程监理资质数据
    qk_qyxx_gcjljz =  db.relationship('QkQyxxGcjljz', backref='qk_company')
    # 企业工业产品生产许可数据
    qk_licence_ind_pro = db.relationship('QkLicenceIndPro', backref='qk_company')
    # 企业工商股东数据
    qk_qyxx_gdxx = db.relationship('QkQyxxGdxx', backref='qk_company')
    # 化妆品生产许可数据
    qk_qua_cos_pro = db.relationship('QkQuaCosPro', backref='qk_company')
    # 企业计算机软件著作权数据
    qk_ent_softw_copyr = db.relationship('QkEntSoftwCopyr', backref='qk_company')
    # 企业建筑施工许可数据
    qk_licence_bui_cons = db.relationship('QkLicenceBuiCons', backref='qk_company')
    # 经营异常
    qk_qyxg_jyyc = db.relationship('QkQyxgJyyc', backref='qk_company')
    # 境外投资数据
    qk_overseasinv = db.relationship('QkOverseasinv', backref='qk_company')
    # 企业农药生产企业资质数据
    qk_qua_pes_pro = db.relationship('QkQuaPesPro', backref='qk_company')
    # 企业工商数据
    qk_qyxx_jbxx_his = db.relationship('QkQyxxJbxxHis', backref='qk_company')
    # 企业商标数据
    qk_ent_trademark = db.relationship('QkEntTrademark', backref='qk_company')
    # 企业诉讼数据-裁判文书
    qk_zgcpwsw = db.relationship('QkZgcpwsw', backref='qk_company')
    # 企业变更信息
    qk_qyxx_bgxx = db.relationship('QkQyxxBgxx', backref='qk_company')
    # 企业招标信息
    qk_bidinviting = db.relationship('QkBidinviting',backref='qk_company')
    # 企业中标信息
    qk_bidwinner = db.relationship('QkBidwinner',backref='qk_company')
    # 食品生产许可
    qk_licence_food_pro = db.relationship('QkLicenseFoodPro',backref='qk_company')
    # 双软认证数据
    qk_cert_soft_ent_pro = db.relationship('QkCertSoftEntPro',backref='qk_company')
    # 探矿权许可数据
    qk_licence_pros = db.relationship('QkLicencePros',backref='qk_company')
    # 通信建设资质
    qk_qua_comm_cons = db.relationship('QkQuaCommCons',backref='qk_company')
    # 信息系统工程监理资
    qk_qua_itsys_sup = db.relationship('QkQuaItsysSup',backref='qk_company')
    # 药品经营许可数据
    qk_licence_medi_oper = db.relationship('QkLicenceMediOper',backref='qk_company')
    # 药品生产许可数据
    qk_licence_medi_pro = db.relationship('QkLicenceMediPro', backref='qk_company')
    # 域名备案
    qk_domain_name_website_Info = db.relationship('QkDomainNameWebsiteInfo', backref='qk_company')
    # 招聘信息
    qk_recruit = db.relationship('QkRecruit', backref='qk_company')
    # 专利数据
    qk_patent = db.relationship('QkPatent', backref='qk_company')
    # 作品著作权
    qk_ent_copyrights = db.relationship('QkEntCopyrights', backref='qk_company')


# 企业GMP认证数据
class QkGmpAuth(db.Model):
    __tablename__ = 'qk_gmp_auth'
    qk_id = db.Column(db.INTEGER, primary_key=True)
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


# 企业工商数据备案信息
class QkQyxxBaxx(db.Model):
    __tablename__ = 'qk_qyxx_baxx'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    salary = db.Column(db.Text)
    idtype = db.Column(db.Text)
    name = db.Column(db.Text)
    no = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    resume = db.Column(db.Text)
    bbd_qyxx_id = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    asstarting = db.Column(db.Text)
    sex = db.Column(db.Text)
    idno = db.Column(db.Text)
    name_id = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    position = db.Column(db.Text)
    type = db.Column(db.Text)
    id = db.Column(db.Text)


# 企业采矿权许可数据
class QkLicenceMining(db.Model):
    __tablename__ = 'qk_licence_mining'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    _id = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    company_key = db.Column(db.Text)
    issue_org = db.Column(db.Text)
    mining_mineral = db.Column(db.Text)
    validdate = db.Column(db.Text)
    valid_from = db.Column(db.Text)
    validto = db.Column(db.Text)
    certificate_no = db.Column(db.Text)
    area = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    project_type = db.Column(db.Text)
    issue_date = db.Column(db.Text)
    mine_name = db.Column(db.Text)
    mining_method = db.Column(db.Text)
    design_scale = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


# 分支机构数据
class QkQyxxFzjgExtend(db.Model):
    __tablename__ = 'qk_qyxx_fzjg_extend'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.Text)
    regorg = db.Column(db.Text)
    frname = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    no = db.Column(db.Text)
    bbd_qyxx_id = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    esdate = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    regno = db.Column(db.Text)
    address = db.Column(db.Text)
    enterprise_status = db.Column(db.Text)
    regno_or_creditcode = db.Column(db.Text)


# 企业工程监理资质数据
class QkQyxxGcjljz(db.Model):
    __tablename__ = 'qk_qyxx_gcjljz'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    issue_date = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    no = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    validdate = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    business_scope = db.Column(db.Text)
    certificate_no = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    bbd_type = db.Column(db.Text)
    id = db.Column(db.Text)
    location = db.Column(db.Text)


# 企业工业产品生产许可数据
class QkLicenceIndPro(db.Model):
    __tablename__ = 'qk_licence_ind_pro'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    _id = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    product_name = db.Column(db.Text)
    company_name = db.Column(db.Text, db.Foreignkey('qk_company.name'))
    issue_date = db.Column(db.Text)
    validdate = db.Column(db.Text)
    certificate_no = db.Column(db.Text)
    location = db.Column(db.Text)
    attachment = db.Column(db.Text)
    specification = db.Column(db.Text)
    instruction = db.Column(db.Text)
    bbd_qyxx_company_id = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    bbd_qyxx_branch_id = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


# 企业工商股东数据
class QkQyxxGdxx(db.Model):
    __tablename__ = 'qk_qyxx_gdxx'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    idtype = db.Column(db.Text)
    shareholder_type = db.Column(db.Text)
    invest_amount = db.Column(db.Text)
    no = db.Column(db.Text)
    shareholder_name = db.Column(db.Text)
    bbd_qyxx_id = db.Column(db.Text)
    paid_contribution = db.Column(db.Text)
    shareholder_id = db.Column(db.Text)
    invest_name = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    idno = db.Column(db.Text)
    invest_ratio = db.Column(db.Text)
    create_time = db.Column(db.Text)
    company_name = db.Column(db.Text, db.Foreignkey('qk_company.name'))
    subscribed_capital = db.Column(db.Text)
    name_compid = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    id = db.Column(db.Text)
    shareholder_detail = db.Column(db.Text)


# 化妆品生产许可数据
class QkQuaCosPro(db.Model):
    __tablename__ = 'qk_qua_cos_pro'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    bbd_dotime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    company_key = db.Column(db.Text)
    company_name = db.Column(db.Text, db.Foreignkey('qk_company.name'))
    location = db.Column(db.Text)
    produce_address = db.Column(db.Text)
    issue_date = db.Column(db.Text)
    validdate = db.Column(db.Text)
    certificate_no = db.Column(db.Text)
    details = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    province = db.Column(db.Text)
    product_name = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    bbd_qyxx_company_id = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_qyxx_branch_id = db.Column(db.Text)
    bbd_source = db.Column(db.Text)

# 企业计算机软件著作权数据
class QkEntSoftwCopyr(db.Model):
    __tablename__ = 'qk_ent_softw_copyr'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    data_source = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    key = db.Column(db.Text)
    rawdata = db.Column(db.Text)
    retain1 = db.Column(db.Text)
    retain2 = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    uuid = db.Column(db.Text)
    bbd_version = db.Column(db.Text)
    class_code = db.Column(db.Text)
    version_num = db.Column(db.Text)
    regnum = db.Column(db.Text)
    regdate = db.Column(db.Text)
    copyright_nationality = db.Column(db.Text)
    soft_short = db.Column(db.Text)
    copyright_owner = db.Column(db.Text, db.Foreignkey('qk_company.name'))
    soft_full_name = db.Column(db.Text)
    soft_short = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    date_first_publication = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_qyxx_company_id = db.Column(db.Text)
    bbd_qyxx_branch_id = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


# 企业建筑施工许可数据
class QkLicenceBuiCons(db.Model):
    __tablename__ = 'qk_licence_bui_cons'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    no = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    company_name = db.Column(db.Text, db.Foreignkey('qk_company.name'))
    location = db.Column(db.Text)
    certificate_no = db.Column(db.Text)
    business_scope = db.Column(db.Text)
    bbd_qyxx_company_id = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    bbd_qyxx_branch_id = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


# 经营异常
class QkQyxgJyyc(db.Model):
    __tablename__ = 'qk_qyxg_jyyc'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    bbd_xgxx_id = db.Column(db.Text)
    remove_busexcep_list = db.Column(db.Text)
    annual_report = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    notice_type = db.Column(db.Text)
    decision_org = db.Column(db.Text)
    bbd_source = db.Column(db.Text)
    create_time = db.Column(db.Text)
    id = db.Column(db.Text)
    regno_or_creditcode = db.Column(db.Text)
    busexcep_list = db.Column(db.Text)
    title = db.Column(db.Text)
    remove_date = db.Column(db.Text)
    rank_date = db.Column(db.Text)
    company_name = db.Column(db.Text, db.Foreignkey('qk_company.name'))
    bbd_type = db.Column(db.Text)
    status = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    rank_busexcep_date = db.Column(db.Text)
    punish_orgout = db.Column(db.Text)
    punish_org = db.Column(db.Text)
    no = db.Column(db.Text)
    case_type = db.Column(db.Text)
    table_name = db.Column(db.Text)
    decide_docno = db.Column(db.Text)
    bbd_url = db.Column(db.Text)


# 境外投资数据
class QkOverseasinv(db.Model):
    __tablename__ = 'qk_overseasinv'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    operate_scope = db.Column(db.Text)
    certificate_num = db.Column(db.Text)
    foreign_invest_enterprises = db.Column(db.Text)
    approval_date = db.Column(db.Text)
    province = db.Column(db.Text)
    domestic_invest_subject = db.Column(db.Text, db.Foreignkey('qk_company.name'))
    bbd_url = db.Column(db.Text)
    country_region = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    certificate_no = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    create_time = db.Column(db.Text)


# 企业农药生产企业资质数据
class QkQuaPesPro(db.Model):
    __tablename__ = 'qk_qua_pes_pro'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    no = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    company_key = db.Column(db.Text)
    company_name = db.Column(db.Text, db.Foreignkey('qk_company.name'))
    reg_address = db.Column(db.Text)
    produce_address = db.Column(db.Text)
    type = db.Column(db.Text)
    validdate = db.Column(db.Text)
    valid_from = db.Column(db.Text)
    validto = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    province = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    bbd_qyxx_company_id = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_qyxx_branch_id = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


# 企业工商数据
class QkQyxxJbxxHis(db.Model):
    """
    数据在jbxx內
    """
    __tablename__ = 'qk_qyxx_jbxx_his'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    operating_period = db.Column(db.Text)
    regno = db.Column(db.Text)
    company_regorg = db.Column(db.Text)
    investcap_amount = db.Column(db.Text)
    ipo_company = db.Column(db.Text)
    company_type = db.Column(db.Text)
    approval_date = db.Column(db.Text)
    create_time = db.Column(db.Text)
    esdate = db.Column(db.Text)
    realcap_amount = db.Column(db.Text)
    credit_code = db.Column(db.Text)
    regcap = db.Column(db.Text)
    id = db.Column(db.Text)
    enterprise_status = db.Column(db.Text)
    invest_cap = db.Column(db.Text)
    openfrom = db.Column(db.Text)
    regorg = db.Column(db.Text)
    frname = db.Column(db.Text)
    regcapcur = db.Column(db.Text)
    parent_firm = db.Column(db.Text)
    bbd_qyxx_id = db.Column(db.Text)
    company_county = db.Column(db.Text)
    operate_scope = db.Column(db.Text)
    regcap_currency = db.Column(db.Text)
    company_name = db.Column(db.Text, db.Foreignkey('qk_company.name'))
    bbd_type = db.Column(db.Text)
    company_industry = db.Column(db.Text)
    regno_or_creditcode = db.Column(db.Text)
    type = db.Column(db.Text)
    revoke_date = db.Column(db.Text)
    investcap_currency = db.Column(db.Text)
    form = db.Column(db.Text)
    bbd_history_name = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    cancel_date = db.Column(db.Text)
    regcap_amount = db.Column(db.Text)
    address = db.Column(db.Text)
    opento = db.Column(db.Text)
    company_enterprise_status = db.Column(db.Text)
    company_province = db.Column(db.Text)
    company_currency = db.Column(db.Text)
    realcap_currency = db.Column(db.Text)
    realcap = db.Column(db.Text)
    frname_id = db.Column(db.Text)
    frname_compid = db.Column(db.Text)
    company_companytype = db.Column(db.Text)


# 企业商标数据
class QkEntTrademark(db.Model):
    __tablename__ = 'qk_ent_trademark'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.Text, db.Foreignkey('qk_company.name'))
    product_list = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    similar_groups = db.Column(db.Text)
    brand_image = db.Column(db.Text)
    class_no = db.Column(db.Text)
    application_no = db.Column(db.Text)
    shangbiao = db.Column(db.Text)
    bbd_version = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    brand_name = db.Column(db.Text)
    commodity = db.Column(db.Text)
    applicant_name = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    no = db.Column(db.Text)
    class_brand = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


# 企业诉讼数据-裁判文书
class QkZgcpwsw(db.Model):
    __tablename__ = 'qk_zgcpwsw'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.Text, db.Foreignkey('qk_company.name'))
    title = db.Column(db.Text)
    casecode = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    action_cause = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    case_type = db.Column(db.Text)
    caseout_come = db.Column(db.Text)
    sentence_date = db.Column(db.Text)
    trial_court = db.Column(db.Text)
    court_litigant = db.Column(db.Text)
    pro_litigant = db.Column(db.Text)
    def_litigant = db.Column(db.Text)
    data_source = db.Column(db.Text)
    pro_other_related = db.Column(db.Text)
    def_other_related = db.Column(db.Text)
    litigant_type = db.Column(db.Text)
    _id = db.Column(db.Text)
    historycase = db.Column(db.Text)
    litigant = db.Column(db.Text)
    rawdata = db.Column(db.Text)
    rel_doc = db.Column(db.Text)
    rel_doc_url = db.Column(db.Text)
    doc_type = db.Column(db.Text)
    ju_proc = db.Column(db.Text)
    applicable_law = db.Column(db.Text)
    update = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    create_time = db.Column(db.Text)
    court_acceptance_fee = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)


# 企业变更信息
class QkQyxxBgxx(db.Model):
    __tablename__ = 'qk_qyxx_bgxx'
    qk_id = db.Column(db.INTEGER, primary_key=True)
    change_count = db.Column(db.Text)
    content_before_change = db.Column(db.Text)
    change_items = db.Column(db.Text)
    bbd_qyxx_id = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    content_after_change = db.Column(db.Text)
    company_name = db.Column(db.Text, db.Foreignkey('qk_company.name'))
    bbd_uptime = db.Column(db.Text)
    change_date = db.Column(db.Text)
    id = db.Column(db.Text)


class QkBidinviting(db.Model):
    """
    企业招标信息
    """
    __tablename__ = 'qkbidinviting'
    qk_id = db.Column(db.Integer, primary_key=True)
    bbd_dotime = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    main = db.Column(db.Text)
    title = db.Column(db.Text)
    project_name = db.Column(db.Text)
    project_number = db.Column(db.Text)
    city = db.Column(db.Text)
    industry = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    source_funds = db.Column(db.Text)
    pubdate = db.Column(db.Text)
    invite_starttime = db.Column(db.Text)
    invite_deadline = db.Column(db.Text)
    bid_opentime = db.Column(db.Text)
    data_sources = db.Column(db.Text)
    company_name_invite = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    telephone = db.Column(db.Text)
    email = db.Column(db.Text)
    fax = db.Column(db.Text)
    agency_name = db.Column(db.Text)
    agency_telephone = db.Column(db.Text)
    agency_email = db.Column(db.Text)
    agency_fax = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    bidwinning_pubdat = db.Column(db.Text)
    company_name_win = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


class QkBidwinner(db.Model):
    """
    企业中标信息
    """
    __tablename__ = 'qk_bidwinner'
    qk_id = db.Column(db.Integer, primary_key=True)
    bbd_version = db.Column(db.Text)
    company_name_invite = db.Column(db.Text)
    telephone = db.Column(db.Text)
    email = db.Column(db.Text)
    fax = db.Column(db.Text)
    agency_name = db.Column(db.Text)
    agency_telephone = db.Column(db.Text)
    agency_email = db.Column(db.Text)
    agency_fax = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    bidwinning_pubdate = db.Column(db.Text)
    company_name_win = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    data_sources = db.Column(db.Text)
    bid_opentime = db.Column(db.Text)
    invite_deadline = db.Column(db.Text)
    uptime = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    main = db.Column(db.Text)
    title = db.Column(db.Text)
    project_name = db.Column(db.Text)
    project_number = db.Column(db.Text)
    city = db.Column(db.Text)
    industry = db.Column(db.Text)
    source_funds = db.Column(db.Text)
    pubdate = db.Column(db.Text)
    invite_starttime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


class QkLicenceFoodPro(db.Model):
    """
    食品生产许可
    """
    __tablename__ = 'qk_licence_food_pro'
    qk_id = db.Column(db.Integer, primary_key=True)
    bbd_dotime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    company_key = db.Column(db.Text)
    product_name = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    location = db.Column(db.Text)
    issue_unit = db.Column(db.Text)
    issue_date = db.Column(db.Text)
    test_mode = db.Column(db.Text)
    produce_address = db.Column(db.Text)
    validdate = db.Column(db.Text)
    certificate_no = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    bbd_qyxx_company_id = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_qyxx_branch_id = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


class QkCertSoftEntPro(db.Model):
    """
    双软认证
    """
    __tablename__ = 'qk_cert_soft_ent_pro'
    qk_id = db.Column(db.Integer, primary_key=True)
    no = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    original_company_name = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    original_frname = db.Column(db.Text)
    frname = db.Column(db.Text)
    original_product_name = db.Column(db.Text)
    product_name = db.Column(db.Text)
    certificate_num = db.Column(db.Text)
    regdate = db.Column(db.Text)
    publish_date = db.Column(db.Text)
    issue_date = db.Column(db.Text)
    type = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    current_city = db.Column(db.Text)
    bbd_qyxx_company_id = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_qyxx_branch_id = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


class QkLicencePros(db.Model):
    """
    探矿权许可
    """
    __tablename__ = 'qk_licence_pros'
    qk_id = db.Column(db.Integer, primary_key=True)
    bbd_uptime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    company_key = db.Column(db.Text)
    issue_org = db.Column(db.Text)
    explore_mineral = db.Column(db.Text)
    validdate = db.Column(db.Text)
    valid_from = db.Column(db.Text)
    validto = db.Column(db.Text)
    certificate_no = db.Column(db.Text)
    area = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    project_type = db.Column(db.Text)
    issue_date = db.Column(db.Text)
    project_name = db.Column(db.Text)
    location = db.Column(db.Text)
    extreme_coordinate = db.Column(db.Text)
    explore_unit = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    bbd_qyxx_company_id = db.Column(db.Text)
    bbd_qyxx_branch_id = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


class QkQuaCommCons(db.Model):
    """
    通信建设资质
    """
    __tablename__ = 'qk_qua_comm_cons'
    qk_id = db.Column(db.Integer, primary_key=True)
    bbd_xgxx_id = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    company_key = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    certificate_no = db.Column(db.Text)
    issue_date = db.Column(db.Text)
    validdate = db.Column(db.Text)
    issue_org = db.Column(db.Text)
    qualification_type = db.Column(db.Text)
    qualification_level = db.Column(db.Text)
    punishment_info = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


class QkQuaItsysSup(db.Model):
    """
    信息系统工程监理资质
    """
    __tablename__ = 'qk_qua_itsys_sup'
    qk_id = db.Column(db.Integer, primary_key=True)
    no = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    company_key = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    qualification_level = db.Column(db.Text)
    location = db.Column(db.Text)
    certificate_no = db.Column(db.Text)
    approval_date = db.Column(db.Text)
    fristissue_date = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


class QkLicenceMediOper(db.Model):
    """
    药品经营许可
    """
    __tablename__ = 'qk_licence_medi_oper'
    qk_id = db.Column(db.Integer, primary_key=True)
    bbd_dotime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    company_key = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    frname = db.Column(db.Text)
    reg_address = db.Column(db.Text)
    business_scope = db.Column(db.Text)
    warehouse_address = db.Column(db.Text)
    operate_mode = db.Column(db.Text)
    principal = db.Column(db.Text)
    quality_principal = db.Column(db.Text)
    issue_date = db.Column(db.Text)
    validdate = db.Column(db.Text)
    certificate_no = db.Column(db.Text)
    issueunit = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    remark = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


class QkLicenceMediPro(db.Model):
    """
    药品生产许可
    """
    __tablename__ = 'qk_licence_medi_pro'
    qk_id = db.Column(db.Integer, primary_key=True)
    bbd_dotime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    company_key = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    frname = db.Column(db.Text)
    reg_address = db.Column(db.Text)
    produce_scope = db.Column(db.Text)
    produce_address = db.Column(db.Text)
    company_type = db.Column(db.Text)
    principal = db.Column(db.Text)
    issue_date = db.Column(db.Text)
    validdate = db.Column(db.Text)
    certificate_no = db.Column(db.Text)
    remark = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    province = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    code = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


class QkDomainNameWebsiteInfo(db.Model):
    """
    域名备案数据信息
    """
    __tablename__ = 'qk_domain_name_website_info'
    qk_id = db.Column(db.Integer, primary_key=True)
    bbd_dotime = db.Column(db.Text)
    bbd_source = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    record_license = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    site_certificate_no = db.Column(db.Text)
    domain_name = db.Column(db.Text)
    organizer_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    homepage_url = db.Column(db.Text)
    website_name = db.Column(db.Text)
    create_time = db.Column(db.Text)
    chief_website_name = db.Column(db.Text)
    approval_time = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    id = db.Column(db.Text)
    website_exam_item = db.Column(db.Text)
    organizer_nature = db.Column(db.Text)


class QkRecruit(db.Model):
    """
    招牌信息
    """
    __tablename__ = 'qk_recruit'
    qk_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    job_title = db.Column(db.Text)
    location = db.Column(db.Text)
    desc = db.Column(db.Text)
    recruit_numbers = db.Column(db.Text)
    pubdate = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    job_descriptions = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    benefits = db.Column(db.Text)
    salary = db.Column(db.Text)
    service_year = db.Column(db.Text)
    website_address = db.Column(db.Text)
    jobfair_location = db.Column(db.Text)
    jobfair_time = db.Column(db.Text)
    language_required = db.Column(db.Text)
    job_nature = db.Column(db.Text)
    job_functions = db.Column(db.Text)
    education_required = db.Column(db.Text)
    enscale = db.Column(db.Text)
    agerequired = db.Column(db.Text)
    postcode = db.Column(db.Text)
    e_mail = db.Column(db.Text)
    contact_information = db.Column(db.Text)
    company_introduction = db.Column(db.Text)
    industry = db.Column(db.Text)
    company_nature = db.Column(db.Text)
    en_scale = db.Column(db.Text)
    majors_required = db.Column(db.Text)
    department = db.Column(db.Text)
    underling_numbers = db.Column(db.Text)
    view_rate = db.Column(db.Text)
    sex_required = db.Column(db.Text)
    bbd_recruit_num = db.Column(db.Text)
    bbd_industry = db.Column(db.Text)
    responserate = db.Column(db.Text)
    bbd_salary = db.Column(db.Text)
    salary_system = db.Column(db.Text)
    reportto = db.Column(db.Text)
    validdate = db.Column(db.Text)
    delivery_time = db.Column(db.Text)
    page_content = db.Column(db.Text)
    source = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)
    pubdate_doublet = db.Column(db.Text)
    create_time = db.Column(db.Text)


class QkPatent(db.Model):
    """
    企业专利数据
    """
    __tablename__ = 'qk_patent'
    qk_id = db.Column(db.Integer, primary_key=True)
    bbd_qyxx_id = db.Column(db.Text)
    public_code = db.Column(db.Text)
    class_code = db.Column(db.Text)
    inventor = db.Column(db.Text)
    title = db.Column(db.Text)
    application_date = db.Column(db.Text)
    application_code = db.Column(db.Text)
    independent_claim = db.Column(db.Text)
    applicant = db.Column(db.Text)
    address = db.Column(db.Text)
    publidate = db.Column(db.Text)
    main_classcode = db.Column(db.Text)
    patent_type = db.Column(db.Text)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    bbd_dotime = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    bbd_version = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    patent_agency = db.Column(db.Text)
    agent_name = db.Column(db.Text)
    npc_code = db.Column(db.Text)
    law_state = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_xgxx_id = db.Column(db.Text)


class QkEntCopyrights(db.Model):
    """
    企业作品著作权,copyright_owner关联公司名
    """
    __tablename__ = 'qk_ent_copyrights'
    qk_id = db.Column(db.Integer, primary_key=True)
    data_source = db.Column(db.Text)
    bbd_type = db.Column(db.Text)
    bbd_dotime = db.Column(db.Text)
    key = db.Column(db.Text)
    rawdata = db.Column(db.Text)
    retain1 = db.Column(db.Text)
    retain2 = db.Column(db.Text)
    bbd_uptime = db.Column(db.Text)
    bbd_url = db.Column(db.Text)
    uuid = db.Column(db.Text)
    bbd_version = db.Column(db.Text)
    production_name = db.Column(db.Text)
    production_category = db.Column(db.Text)
    creation_completion_date = db.Column(db.Text)
    regnum = db.Column(db.Text)
    regdate = db.Column(db.Text)
    copyright_owner = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    bbd_xgxx_id = db.Column(db.Text)
    date_first_publication = db.Column(db.Text)
    create_time = db.Column(db.Text)
    bbd_source = db.Column(db.Text)


class QkQyxxNb(db.Model):
    """
    企业年报
    """
    __tablename__ = 'qk_qyxx_nb'
    qk_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.Text, db.ForeignKey('qk_company.name'))
    qk_qyxx_nb_jbxx = db.relationship('QkQyxxNbJbxx', backref='qk_qyxx_nb')

class QkQyxxNbJbxx(db.Model):
    """
    企业信息年报数据-基本信息
    """
    __tablename__ = 'qk_qyxx_nb_jbxx'
    qk_id = db.Column(db.Integer, primary_key=True)
    nb_id = db.Column(db.Integer, db.ForeignKey('qk_qyxx_nb.qk_id'))
    regno_or_creditcode = db.Column(db.Text)
    bbd_source= db.Column(db.Text)
    bbd_uptime= db.Column(db.Text)
    bbd_dotime= db.Column(db.Text)
    bbd_html= db.Column(db.Text)
    company_name= db.Column(db.Text)
    bbd_url= db.Column(db.Text)
    year= db.Column(db.Text)
    status= db.Column(db.Text)
    bbd_params= db.Column(db.Text)
    version= db.Column(db.Text)
    bbd_table= db.Column(db.Text)
    _id= db.Column(db.Text)
    bbd_type= db.Column(db.Text)
    type= db.Column(db.Text)
    his_companyname= db.Column(db.Text)
    bbd_seed= db.Column(db.Text)
    rowkey_dict= db.Column(db.Text)
    phone= db.Column(db.Text)
    staff_num= db.Column(db.Text)
    name= db.Column(db.Text)
    postalcode= db.Column(db.Text)
    address= db.Column(db.Text)
    enterprise_status= db.Column(db.Text)
    stock_transfer_flag= db.Column(db.Text)
    regno_creditcode= db.Column(db.Text)
    stock_buy_flag= db.Column(db.Text)
    website_flag= db.Column(db.Text)
    email= db.Column(db.Text)
    external_security_flag= db.Column(db.Text)
    subordinate_relations= db.Column(db.Text)
    frname= db.Column(db.Text)
    money_num= db.Column(db.Text)
    subordinate_name= db.Column(db.Text)
    company_type= db.Column(db.Text)
    admin_license_flag= db.Column(db.Text)
    nbbz= db.Column(db.Text)
    bbd_qyxx__id= db.Column(db.Text)
    bbd_xgxx_id= db.Column(db.Text)
