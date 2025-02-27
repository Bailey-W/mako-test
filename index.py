from mako.template import Template
from mako.lookup import TemplateLookup

# Create a TemplateLookup object with the directory containing your templates
lookup = TemplateLookup(directories=['.'])  # Assuming the templates are in the current directory

# Load the main template using the lookup
main_template = Template(filename='main_template.mako', lookup=lookup)

# Render the main template
output = main_template.render()
print(output)