# -*- coding: utf-8 -*-

from odoo import models

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
        
    def action_child_of(self):
        domain = [('id', 'child_of', self.categ_id.id)]
        child = self.env['product.category'].search(domain)
        for category in child:
            print(f"\n\n\ncategory id: {category.id} ==> category name: {category.name} \n\n\n")

    def action_Parent_of(self):
        domain = [('id', 'parent_of', self.categ_id.id)]
        parent_categories = self.env['product.category'].search(domain)
        print(parent_categories,".....parent_categories")    
        for category in parent_categories:
            print(f"\n\n\ncategory id: {category.id} ==> category name: {category.name} \n\n\n")
            child = self.env['product.category'].search([
                ('id', 'child_of', category.id)
                ])
            
    def action_open_category_hierarchy_wizard(self):
        """
        Open the wizard to display parent and child categories of the current product's category.
        """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Category Hierarchy',
            'res_model': 'category.hierarchy.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_id': self.id},
        }