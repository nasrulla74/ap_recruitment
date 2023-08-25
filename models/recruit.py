# -*- coding: utf-8 -*-
from odoo import fields, models


class XpatWorkTypes(models.Model):
    _name = "xpat.worktypes"
    _description = "Xpat work types"

    name = fields.Char(string="Xpat Work Type", required=True)


class XpatWorkSites(models.Model):
    _name = "xpat.worktsites"
    _description = "Xpat work sites"

    name = fields.Char(string="Xpat Work Site", required=True)
    address = fields.Text('Work Site Address')


class InheritPartner(models.Model):
    _inherit = 'hr.applicant'

    permanent_address = fields.Text('Permanent Address')
    current_address = fields.Text('Current Address')
    other_benefits = fields.Text('Other Benefits')
    passport_number = fields.Char('Passport Number')
    nationality = fields.Char('Nationality')
    xpat_position = fields.Char('Xpat Position')
    remuneration = fields.Char('Remuneration')
    working_hours = fields.Char('Working Hours')
    salary_payment = fields.Char('Salary Payment')
    emergency_contact_name = fields.Char('Emergency Contact Name')
    emergency_contact_number = fields.Char('Emergency Contact Number')
    sponsor_name = fields.Char('Sponsor Name')
    sponsor_position = fields.Char('Sponsor Position')
    birth_date = fields.Date('Date of Birth')
    contract_start = fields.Date('Contract Start')
    contract_end = fields.Date('Contract End')
    apply_date = fields.Date('Apply Date')
    work_type_id = fields.Many2one('xpat.worktypes', string="Work Type")
    work_site_id = fields.Many2one('xpat.worktsites', string="Work Site")
    contract_status_id = fields.Many2one('hr.contract.type', string="Contract Status")


class SetCustomerHeaderFooter(models.Model):
    """"""
    _inherit = "res.partner"

    customer_header = fields.Image("Header")
    customer_footer = fields.Image("Footer")
    customer_seal = fields.Image("Customer Seal")
    customer_header_width = fields.Char("Header Width", default="1000")
    customer_header_height = fields.Char("Header height", default="100")
    customer_footer_width = fields.Char("Footer Width", default="1000")
    customer_footer_height = fields.Char("Footer height", default="75")
