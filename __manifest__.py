# -*- coding: utf-8 -*-
{
    'name': "Limawira Purchase Order",
    'summary': '',
    'author': '',
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base', 'purchase'],
    'data': [
        # PURCHASE ORDER
        'report/lww_po_report.xml',
        'views/lww_po_template.xml',
        'views/bs_po_template.xml',
        'views/spartadua_po_template.xml',
        'views/pratama_po_template.xml',
        'views/imadea_p_template.xml',
        # FORM VIEW
        'views/purchase_order_view.xml',
    ],
    'installable': True,
    'application': False,
}

