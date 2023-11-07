# -*- coding: utf-8 -*-
from odoo import fields, models #Inherit from global "models" library from odoo

#Here, class EstateProperty is created directly in main folder. 
# However, it is recommended to use folder tree arborescence to ease navigation (and inheritance)

class EstatePropertyType(models.Model):
    _name = "estate.property.type" # Dot characters are replaced by Underscore when table is created by ORM
    _description = "Property Type Table listing Estate category, for example house or appartment"
    
    name = fields.Char('Name', required=True, translate=True)
