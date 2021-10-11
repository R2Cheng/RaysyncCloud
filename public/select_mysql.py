#-*- coding:utf-8 -*-
import pymysql
from public.mysql_db import *
from unittest import TestCase
import unittest


class UserLogin(TestCase):
        def test_case001(self):
                id = 10000004
                sql = 'select user_name  from tb_user WHERE id=%d' % id
                db_name = 'rendering_service'
                a = sqlQuery(sql,db_name)
                print(a[0][0])


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UserLogin('test_case001'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
