# -*- coding: utf-8 -*-

{
    'name': 'VE - Tax Withholding',
    
    'summary': """
        This is a module in which you can perform tax withholdings, generate the sales and purchase ledger required by Venezuelan law. 
    """,
    
    'description': """
        This is a module in which you can perform tax withholdings, generate the sales and purchase ledger required by Venezuelan law. 
    """,
    
    'author': 'Payall',
    
    'website': 'https://payall.com.ve/',
    
    'category': 'Accounting',
    
    'version': '1.0.0',
    
    'depends': ['account_accountant','sale_management'],
    
    'data': [
        "security/tax_withholding_security.xml",
        "security/ir.model.access.csv",
        "data/withholding_subjects_data.xml",
        "report/tax_withholding_report.xml",
        "report/tax_book_report.xml",
        "wizard/purchases_book_views.xml",
        "views/tax_withholding_subject_view.xml",
        "views/tax_withholding_views.xml",
        "views/tax_withholding_menuitems.xml",
        "views/account_move_inherit_view.xml",
        
       
    ],
    
    'demo': [
        "data/withholding_subjects_demo.xml"
    ],
}