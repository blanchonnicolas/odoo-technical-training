# -*- coding: utf-8 -*-
from odoo import fields, models #Inherit from global "models" library from odoo
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
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
        required=True,
        copy=False,
        default='new')