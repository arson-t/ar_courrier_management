# -*- coding: utf-8 -*-
{
    'name': "ar_courrier_management",
    'summary': """
                """,
    'description': """
    """,
    'author': "Fano",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'web', 'mail', 'hr'],

    'data': [
        'security/ir.model.access.csv',
        'views/courier_arrived_view.xml',
        'views/courrier_depart_view.xml',
        'views/enregistrement_os_view.xml',
        'views/enregistrement_decision_view.xml',
        'views/enregistrement_marche.xml',
        'views/enregistrement_convention.xml'
    ],

}
