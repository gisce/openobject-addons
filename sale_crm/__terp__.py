{
    "name" : "Sale CRM Stuff",
    "version" : "1.0",
    "author" : "Tiny",
    "website" : "http://tinyerp.com/module_sale.html",
    "depends" : ["sale", "crm", "product", "account"],
    "category" : "Generic Modules/Sales & Purchases",
    "description": """
    This module adds a shortcut on one or several cases in the CRM.
    This shortcut allows you to generate a sale order based the selected case.
    If different cases are open (a list), it generates one sale order by
    case.
    The case is then closed and linked to the generated sale order.

    It also add a shortcut on one or several partners.
    This shorcut allows you to generate a CRM case for the partners.
    """,
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : ["sale_crm_wizard.xml"],
    "active": False,
    "installable": True
}
