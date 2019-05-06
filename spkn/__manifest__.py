# -*- coding: utf-8 -*-
{
    'name': "spkn",

    'summary': """
        1. Penambahan field spesifikasi buku di modul product.template""",

    'description': """
        Add On untuk PT Sarana Panca Karya Nusa""",

    'author': "Jaya Martha",
    'website': "http://jayamartha.blogspot.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'SPKN',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr', 'stock','crm'],

    # always loaded,
    'data': [
        # 'security/ir.model.access.csv',
        'views/spesifikasi_buku.xml',
        'views/prospek.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}