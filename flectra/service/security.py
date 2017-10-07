# -*- coding: utf-8 -*-
# Part of Flectra. See LICENSE file for full copyright and licensing details.

import flectra
import flectra.exceptions

def login(db, login, password):
    res_users = flectra.registry(db)['res.users']
    return res_users._login(db, login, password)

def check(db, uid, passwd):
    res_users = flectra.registry(db)['res.users']
    return res_users.check(db, uid, passwd)
