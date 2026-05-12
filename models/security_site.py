from odoo import models, fields

class SecurityClientSite(models.Model):
    _name = 'security.client.site'
    _description = 'Client Site'

    name = fields.Char(required=True)
    partner_id = fields.Many2one('res.partner', string='Client')
    address = fields.Char()
    risk_level = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], default='medium')

    instructions = fields.Text()
    post_ids = fields.One2many('security.guard.post', 'site_id')

class SecurityGuardPost(models.Model):
    _name = 'security.guard.post'
    _description = 'Guard Post'

    name = fields.Char(required=True)
    site_id = fields.Many2one('security.client.site')
    guards_required = fields.Integer(default=1)
    special_instructions = fields.Text()
    is_critical = fields.Boolean()
