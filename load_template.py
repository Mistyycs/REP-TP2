from jinja2 import Template

template_content = open('property.py.jinja').read()
template = Template(template_content)

factors = {
    "operation1" : "(x+y) + z",
    "operation2" : "x+ (y+z)",
    "repetitions" : 1000,
}

generated_code = template.render(factors)

with open('generated_property_check.py','w') as f:
    f.write(generated_code)

print("Generated code has been written to 'generated_property_check.py'.")