from odoo import models, fields

class TariffGrid(models.Model):
    _name = 'tariff.grid'
    _description = 'Tariff Grid'
    
    colis_type = fields.Selection([('envelope', 'Envelope'), ('material', 'Material')], string='Colis Type', required=True)
    weight = fields.Float('Weight', required=True)
    zone_id = fields.Many2one('tariff.zone', string='Zone', required=True)
    amount = fields.Float('Amount', required=True)
    client_ids = fields.Many2many('res.partner', string='Clients')
