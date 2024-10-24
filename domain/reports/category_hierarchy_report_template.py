from odoo import models, fields, api

class AbstractCategoryHierarchy(models.AbstractModel):
    _name = 'abstract.category.hierarchy'
    _description = 'Abstract Model for Category Hierarchy Reporting'
    _abstract = True

    def get_child_categories(self, category_id):
        """
        Get all child categories of the given category.
        """
        domain = [('id', 'child_of', category_id)]
        return self.env['product.category'].search(domain)

    def get_parent_categories(self, category_id):
        """
        Get all parent categories of the given category.
        """
        domain = [('id', 'parent_of', category_id)]
        return self.env['product.category'].search(domain)

    def generate_category_hierarchy_report(self, product):
        """
        This method will be used to generate a report for parent and child categories.
        """
        print(product,".........................product\n\n")
        print(self,".........................self\n\n")
        
        parent_categories = self.get_parent_categories(product.categ_id.id)
        child_categories = self.get_child_categories(product.categ_id.id)
        print("........parent_categories.......parent_categories...parent_categories",parent_categories)
        print("........child_categories.......child_categories...child_categories",child_categories)
        return {
            'product': product,
            'parent_categories': parent_categories,
            'child_categories': child_categories,
        }
