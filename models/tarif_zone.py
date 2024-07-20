# -*- coding: utf-8 -*-

from odoo import models, fields

class TariffZone(models.Model):
    _name = 'tariff.zone'
    _description = 'Tariff Zone'
    
    name = fields.Char('Zone Name', required=True)
    country_ids = fields.Many2many('res.country', string='Countries')

