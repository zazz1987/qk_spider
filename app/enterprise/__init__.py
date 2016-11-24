from flask import Blueprint

enterprise = Blueprint('enterprise', __name__)

from . import views, views2, views3, errors
from ..models import Permission


@enterprise.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
