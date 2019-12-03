from odoo import models, fields

class Job(models.Model):
    _inherit = "hr.job"
    
    reporting_manager = fields.Many2one('hr.employee', 'Reporting Manager')
    assign_location = fields.Char('Assignment Location')
    years_experience = fields.Char('Years of Experience')
    edu_qualification = fields.Char('Educational Qualification')
    languages = fields.Char(string='Languages')
    it_skills = fields.Many2many('it.skills', sting="IT Skills")
    nationalities = fields.Char('Nationality')
    visa_status = fields.Selection([
        ('transferable_iqama', 'Transferable Iqama'),
        ('saudi_national', 'Saudi National'),
        ('any_status', 'Any Visa Status '),
    ], string="Visa Status")


class ITSkills(models.Model):
    _name = 'it.skills'
    
    name = fields.Char('name')