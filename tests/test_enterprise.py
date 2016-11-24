# -*- coding: utf-8 -*-
from unittest import TestCase

from app import create_app, db
from app.models import Role


class TestEnterprist(TestCase):

    def setup(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()

    def search(self):
        pass
