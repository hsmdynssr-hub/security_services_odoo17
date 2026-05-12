from odoo import models, fields

class SecurityRoster(models.Model):
    _name = 'security.roster'
    _description = 'Security Roster'

    name = fields.Char()
    site_id = fields.Many2one('security.client.site')
    date = fields.Date()
    supervisor_id = fields.Many2one('hr.employee')
    state = fields.Selection([
        ('planned', 'Planned'),
        ('started', 'Started'),
        ('completed', 'Completed'),
    ], default='planned')

class SecurityAttendance(models.Model):
    _name = 'security.attendance'
    _description = 'Security Attendance'

    employee_id = fields.Many2one('hr.employee', required=True)
    site_id = fields.Many2one('security.client.site')
    check_in = fields.Datetime()
    check_out = fields.Datetime()
    delay_minutes = fields.Integer()
    status = fields.Selection([
        ('present', 'Present'),
        ('late', 'Late'),
        ('absent', 'Absent'),
    ], default='present')

class SecurityIncident(models.Model):
    _name = 'security.incident'
    _description = 'Security Incident'

    name = fields.Char(string='Incident No')
    site_id = fields.Many2one('security.client.site')
    employee_id = fields.Many2one('hr.employee')
    incident_type = fields.Selection([
        ('theft', 'Theft'),
        ('complaint', 'Complaint'),
        ('damage', 'Damage'),
    ])
    severity = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ])
    description = fields.Text()
    action_taken = fields.Text()
    state = fields.Selection([
        ('reported', 'Reported'),
        ('investigation', 'Under Investigation'),
        ('closed', 'Closed'),
    ], default='reported')
