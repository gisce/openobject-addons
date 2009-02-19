# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2008 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name":"Indian Accounting",
    "version":"1.0",
    "author":"Tiny",
    "category":"Profile",
    "depends":[
        "account_base",
<<<<<<< TREE
        "account_india_ledger",
<<<<<<< TREE
        "account_indian_report",
        "account_voucher"
=======
=======
        #"account_india_ledger",
>>>>>>> MERGE-SOURCE
        "account_invoice",
        "account_voucher",
        "account_india",
        "account_report_india",
<<<<<<< TREE
        "account_stock",
        "sale_numbers",
        "purchase_number",
        "l10n_chart_in", 
>>>>>>> MERGE-SOURCE
=======
        #"account_stock",
        #"sale_numbers",
        #"purchase_number",
        #important for the indian accounting but do not load with account module
        "l10n_chart_in",
>>>>>>> MERGE-SOURCE
    ],
    "demo_xml":[],
    "update_xml":[],
    "active":False,
    "installable":True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

