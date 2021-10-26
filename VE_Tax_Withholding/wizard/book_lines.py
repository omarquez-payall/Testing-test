# -*- coding: utf-8 -*-

from odoo import models, fields, api
class BookLinesWizard( models.TransientModel):
    _name = 'tax.purchases_book.lines_wizard'
    _description = 'Lines of purchases bill entry by period'

    related_book = fields.Many2one(comodel_name = 'tax.purchases_book_wizard')
    name = fields.Char(string = 'No de Documento')
    control_number = fields.Char(string = 'Numero de Control', default = '0')
    tax_amount = fields.Float(string='Porcentaje de impuesto', default = '0')
    untaxed_amount = fields.Float(string='Base Imponible', default = '0')
    total_amount = fields.Float(string='Importe de factura', default = '0')
    period = fields.Text(string='Periodo', default = '0')