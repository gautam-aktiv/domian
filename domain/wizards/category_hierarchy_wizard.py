from odoo import models, fields, api

class CategoryHierarchyWizard(models.TransientModel):
    _name = 'category.hierarchy.wizard'
    _description = 'Wizard to Display Category Hierarchy and Generate Report'

    product_id = fields.Many2one('product.template', string='Product')
    parent_categories = fields.Many2many(
        'product.category',
        'category_hierarchy_parent_rel',  
        'wizard_id',
        'category_id',
        string='Parent Categories'
    )
    child_categories = fields.Many2many(
        'product.category',
        'category_hierarchy_child_rel',
        'wizard_id',
        'category_id',
        string='Child Categories'
    )

    @api.model
    def default_get(self, fields_list):
        """
        Populate the wizard with parent and child categories based on the selected product.
        """
        res = super(CategoryHierarchyWizard, self).default_get(fields_list)
        active_id = self.env.context.get('active_id')
        if active_id:
            product = self.env['product.template'].browse(active_id)

            # Get parent and child categories
            parent_categories = self.env['product.category'].search([('id', 'parent_of', product.categ_id.id)])
            child_categories = self.env['product.category'].search([('id', 'child_of', product.categ_id.id)])

            # Set the values for the wizard fields
            res.update({
                'product_id': product.id,
                'parent_categories': [(6, 0, parent_categories.ids)],
                'child_categories': [(6, 0, child_categories.ids)],
            })
        return res

    def action_generate_report(self):
        """
        Generate the report and close the wizard when the button is clicked.
        """
        return self.env.ref('domain.action_report_category_hierarchy').report_action(self.product_id)
