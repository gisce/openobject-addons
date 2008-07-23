# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2005-2006 TINY SPRL. (http://tiny.be) All Rights Reserved.
#
# $Id: allowances.py 4656 2006-11-24 09:58:42Z ced $
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

from mx import DateTime
import time

from osv import fields, osv

class payroll_setup_elements(osv.osv):
    _name = "payroll.setup.elements"
    _description = "Elements"
    _columns = {
            'name' : fields.char('Element Type', size=32, required=True),
            'category' : fields.selection([('payelements','PAY ELEMENT'),('deductions','DEDUCTION'),('reimbursements','REIMBURSEMENTS')], 'Category'),
        }
    _defaults = {
            #'attendance' : lambda *a: True,
        }
    _order = 'name desc'
    
payroll_setup_elements()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

