from odoo import models, fields, api

class QuoteLine(models.Model):
    _name = 'quote.line'
    _description = 'Quote Line'
    
    quote_id = fields.Many2one('quote', string='Quote', required=True)
    colis_id = fields.Many2one('colis', string='Colis', required=True)
    price = fields.Float('Price', compute='_compute_price', store=True)

    @api.depends('colis_id')
    def _compute_price(self):
        for line in self:
            line.price = line.colis_id.get_tariff()

class Quote(models.Model):
    _name = 'quote'
    _description = 'Quote'
    
    name = fields.Char('Quote Name', required=True)
    client_id = fields.Many2one('res.partner', string='Client', required=True)
    line_ids = fields.One2many('quote.line', 'quote_id', string='Quote Lines')
