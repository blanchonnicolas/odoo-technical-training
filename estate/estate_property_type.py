# -*- coding: utf-8 -*-
from odoo import fields, models #Inherit from global "models" library from odoo

#Here, class EstateProperty is created directly in main folder. 
# However, it is recommended to use folder tree arborescence to ease navigation (and inheritance)

class EstatePropertyType(models.Model):
    _name = "estate.property.type" # Dot characters are replaced by Underscore when table is created by ORM
    _description = "Property Type Table listing Estate category, for example house or apartment"
    _order = "sequence, name" #Sort the entries following sequence (most used) name (alphabetically)

    # -----------Chapitre 12: Inline views - Display the list of properties linked to a property type    
    property_ids = fields.One2many("estate.property", "property_type_id", string="List of properties")

    name = fields.Char('Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order property type Most used comes first")
