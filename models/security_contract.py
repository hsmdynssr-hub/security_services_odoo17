from odoo import models, fields

class SecurityContract(models.Model):
    _name = 'security.contract'
    _description = 'Security Contract'
    _rec_name = 'contract_no'

    contract_no = fields.Char(required=True)
    partner_id = fields.Many2one('res.partner', string='Client', required=True)
    start_date = fields.Date()
    end_date = fields.Date()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('closed', 'Closed'),
    ], default='draft')

    monthly_amount = fields.Float()
    operations_manager_id = fields.Many2one('hr.employee')
    sales_person_id = fields.Many2one('res.users')

    line_ids = fields.One2many('security.contract.line', 'contract_id')

class SecurityContractLine(models.Model):
    _name = 'security.contract.line'
    _description = 'Security Contract Line'

    contract_id = fields.Many2one('security.contract')
    site_id = fields.Many2one('security.client.site')
    service_type = fields.Selection([
        ('fixed', 'Fixed Guarding'),
        ('patrol', 'Patrol'),
        ('vip', 'VIP'),
    ])
    guards_count = fields.Integer()
    shifts_count = fields.Integer()
    unit_price = fields.Float()
    monthly_price = fields.Float()
