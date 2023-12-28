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
    other_benefits = fields.Html('Other Benefits')
    passport_number = fields.Char('Passport Number')
    pp_expiry = fields.Date('Passport Expiry')
    nationality = fields.Char('Nationality')
    xpat_position = fields.Char('Xpat Position')
    remuneration = fields.Char('Remuneration')
    working_hours = fields.Char('Working Hours')
    mobile_number = fields.Char('Mobile Number')
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
    is_married = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                 default='no', string="Is Married")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                                  default='male', string="Gender")
    visa_type = fields.Selection([('work', 'Work Visa'), ('business', 'Business Visa'), ('special','Special Visa')],
                              default='work', string="Visa Type")
    wp_number = fields.Char('Work Permit Number')
    wp_expiry = fields.Date('WP Expiry Date')
    slot_expiry = fields.Date('Slot Expiry Date')
    card_expiry = fields.Date('Card Expiry Date')
    insurance_expiry = fields.Date('Insurance Expiry Date')

class SetCustomerHeaderFooter(models.Model):
    """"""
    _inherit = "res.partner"

    customer_header = fields.Image("Header")
    customer_footer = fields.Image("Footer")
    customer_seal = fields.Image("Customer Seal")
    customer_sign = fields.Image("Customer Sign")
    customer_header_width = fields.Char("Header Width", default="1000")
    customer_header_height = fields.Char("Header height", default="100")
    customer_footer_width = fields.Char("Footer Width", default="1000")
    customer_footer_height = fields.Char("Footer height", default="75")
