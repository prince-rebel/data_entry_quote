from odoo import models, fields, api
from odoo.exceptions import UserError

class Colis(models.Model):
    _name = 'colis'
    _description = 'Colis'
    
    name = fields.Char('Name', required=True)
    colis_type = fields.Selection([('envelope', 'Envelope'), ('material', 'Material')], string='Colis Type', required=True)
    weight = fields.Float('Weight', required=True)
    destination_country_id = fields.Many2one('res.country', string='Destination Country', required=True)
    client_id = fields.Many2one('res.partner', string='Client', required=True)

    def get_tariff(self):
        zone = self.env['tariff.zone'].search([('country_ids', 'in', [self.destination_country_id.id])], limit=1)
        if not zone:
            raise UserError('No tariff zone found for the destination country.')

        grid = self.env['tariff.grid'].search([
            ('colis_type', '=', self.colis_type),
            ('weight', '<=', self.weight),
            ('zone_id', '=', zone.id),
            ('client_ids', 'in', [self.client_id.id])
        ], limit=1, order='weight desc')
        
        if not grid:
            raise UserError('No tariff found for the given criteria.')

        return grid.amount
