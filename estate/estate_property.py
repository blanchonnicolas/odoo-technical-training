# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions #Inherit from global "models" library from odoo
# api package used for computational functions
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


#Here, class EstateProperty is created directly in main folder. 
# However, it is recommended to use folder tree arborescence to ease navigation (and inheritance)

class EstateProperty(models.Model):
    _name = "estate.property" # Dot characters are replaced by Underscore when table is created by ORM
    _description = "Property Table associated to Estate application"

    #With no specification, the table "estate_property" is created with following fields : 
        # id (Id) :    The unique identifier for a record of the model.
        # create_date (Datetime) :    Creation date of the record.
        # create_uid (Many2one) :    User who created the record.
        # write_date (Datetime) :    Last modification date of the record.
        # write_uid (Many2one) :    User who last modified the record.

    # This can be verified using shell command : \d estate_property
    #We will specify specific fields on top of existing ones, according to Chapter 4 (Boolean, Float, Char, Text, Date, Selection)
    
    name = fields.Char('Name', required=True, translate=True)
    description = fields.Text('Description', required=False, translate=True)
    postcode = fields.Char('PostCode', required=False, translate=False)
    date_availability = fields.Date('Date Availability', required=False, copy=False, default=lambda self: fields.Date.today() + relativedelta(months=+3))
    expected_price = fields.Float('Expected price', required=True, translate=False)
    selling_price = fields.Float('Selling price', required=False, translate=False, readonly=True, copy=False)
    bedrooms = fields.Integer('Number of bedrooms', default=2, required=False)
    living_area = fields.Integer('Living Area surface (sqm)', default=50, required=False)
    facades = fields.Integer('Number of facades', default=2, required=False)
    garage = fields.Boolean('Garage', default=False)
    garden = fields.Boolean('Garden', default=False)
    garden_area = fields.Integer('Garden Area surface (sqm)', required=False)
    garden_orientation = fields.Selection(
        string='Facing orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Garden orientation is used to define facing properties")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        required=True,
        copy=False,
        default='new')

    # -------------------------------------------------------------------------
    # RELATION BETWEEN MODELS
    # -------------------------------------------------------------------------
    property_type_id = fields.Many2one("estate.property.type", string="Property Types")
    salesperson_id = fields.Many2one('res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', index=True, copy=False)

    tag_ids = fields.Many2many("estate.property.tag", string="Property Tags")

    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offer Ids") #Asking the offer model, to fetch all property_id in offer_ids field. This offer_ids field will then be used in estate_property_views, using tree
    
    # -------------------------------------------------------------------------
    # COMPUTE METHODS
    # -------------------------------------------------------------------------

    total_area = fields.Integer(string='Total Area surface (sqm)', 
        compute='_compute_total_area',
        help="Computed field from Garden + Living areas")
    
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    
    best_offer = fields.Float(string='Maximum Price offer',
        compute='_compute_max_price')
    
    @api.depends('offer_ids.price')
    def _compute_max_price(self):
        for record in self:
            if record.offer_ids:
                record.best_offer = max(record.offer_ids.mapped('price'))
            else:
                record.best_offer = 0

    # -------------------------------------------------------------------------
    # DELETE METHOD THAT REJECT DELETING WHEN STATE IS NOT ...
    # -------------------------------------------------------------------------
    @api.ondelete(at_uninstall=False)
    def _unlink_except_state_is_new_or_cancelled(self):
        for record in self:
            if record.state not in ['new','cancelled']:
                raise UserError("Can't delete if state is not New or Cancelled !")

    # -------------------------------------------------------------------------
    # ACTION METHODS THAT ENSURE THAT canceled property cannot be set as sold, and a sold property cannot be canceled ...
    # -------------------------------------------------------------------------
    def action_sold(self):
        if "offer_accepted" in self.mapped("state"):
            raise UserError("Canceled properties cannot be sold.")
        return True

    def action_cancel(self):
        if "sold" in self.mapped("state"):
            raise UserError("Sold properties cannot be canceled.")
        return True




