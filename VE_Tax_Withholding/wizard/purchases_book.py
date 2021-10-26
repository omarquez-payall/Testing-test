# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchasesBookWizard( models.TransientModel):
    _name = 'tax.purchases_book_wizard'
    _description = 'Book of every purchase bill entry by period'
    
    name = fields.Char(string='Title', required=True)
    
    description = fields.Text(string='Description')
    
    date_from = fields.Date(string='Fecha desde')
    
    date_to = fields.Date(string='Fecha hasta')
    
    related_invoices = fields.One2many(string='Facturas', comodel_name='tax.purchases_book.lines_wizard', inverse_name='related_book', store = True)


    @api.onchange('date_from','date_to')
    def _compute_invoices(self):
        book_lines = []
        invoices = self.env['account.move'].search([('move_type','=','out_invoice'),('invoice_date','>=',self.date_from),('invoice_date','<=',self.date_to)])
        self.clear_related_invoices()
        for invoice in invoices:
            book_lines.append((0,0,{'name':invoice.name, 'control_number':invoice.control_number, 'total_amount':invoice.amount_total, 'period':invoice.invoice_date}) )
        self.related_invoices = book_lines
        
        
        
    def clear_related_invoices(self):
        for invoice in self.related_invoices:
            invoice.unlink()

    def action_print_report(self):
        data = {'name':self.name, 'date_from':self.date_from, 'date_to':self.date_to, 'related_invoices': self.related_invoices.ids}
        return self.env.ref('VE_Tax_Withholding.action_report_tax_book_report').report_action(self, data)
        