# -*- coding: utf-8 -*-
# © 2016 Cristian Salamea <cristian.salamea@ayni.com.ec>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Impresion de Cheques para Ecuador',
    'version': '17.0.0.1.0',
    'author': ' O.C.A., Leonardo Gómez',
    'category': 'Accounting',
    'complexity': 'normal',
    'website': '',
    'license': 'AGPL-3',
    'data': [
        'views/report_check_pacifico.xml',
        'views/report_check_pichincha.xml',
        'views/report_check_guayaquil.xml',
        'views/reports.xml',
        'views/account_view.xml'
    ],
    'depends': [
        'account_check_printing',
    ]
}
