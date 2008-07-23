##############################################################################
#
# Copyright (c) 2004 TINY SPRL. (http://tiny.be) All Rights Reserved.
#                    Fabien Pinckaers <fp@tiny.Be>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

import wizard
import netsvc
import netsvc
import osv
import time
import pooler

pay_form = '''<?xml version="1.0"?>
<form string="Check payment for buyer">
</form>'''
pay_fields = {
}


pay_form1 = '''<?xml version="1.0"?>
<form string="Check payment for seller">
</form>'''
pay_fields1 = {
}
def _payer(self, cr, uid, data, context):
    pool = pooler.get_pool(cr.dbname)
    pool.get('auction.lots').write(cr,uid,data['ids'],{'is_ok':True, 'state':'paid'})
    return {}


def _payer_sel(self, cr, uid, data, context):
    pool = pooler.get_pool(cr.dbname)
    pool.get('auction.lots').write(cr,uid,data['ids'],{'paid_vnd':True})
    return {}


class wiz_auc_pay(wizard.interface):
    states = {
        'init': {
            'actions': [],
            'result': {'type': 'form', 'arch':pay_form, 'fields': pay_fields, 'state':[('end','Cancel'),('pay','Pay')]}
        },
        'pay': {
        'actions': [_payer],
        'result': {'type': 'state', 'state':'end'}
        }}
wiz_auc_pay('auction.payer')


class wiz_auc_pay_sel(wizard.interface):
    states = {
        'init': {
            'actions': [],
            'result': {'type': 'form', 'arch':pay_form1, 'fields': pay_fields1, 'state':[('end','Cancel'),('pay2','Pay')]}
        },
        'pay2': {
        'actions': [_payer_sel],
        'result': {'type': 'state', 'state':'end'}
        }}
wiz_auc_pay_sel('auction.payer.sel')

