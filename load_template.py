from jinja2 import Template

template_content = open('property_template.py.jinja').read()
template = Template(template_content)

factor_combinations = [
    {"operation1" : "(x + y) + z", "operation2" : "x + (y + z)", "repetitions" : 1000, "operation_gen_alea" : "random.random()"},
    {"operation1" : "(x + y) + z", "operation2" : "x + (y + z)", "repetitions" : 10000, "operation_gen_alea" : "numpy.random.rand()"},
    {"operation1" : "x + y", "operation2" : "y + x", "repetitions" : 10000, "operation_gen_alea" : "random.random()"},
    {"operation1" : "x * y", "operation2" : "y * x", "repetitions" : 10000, "operation_gen_alea" : "random.random()"},
    {"operation1" : "x * y", "operation2" : "y * x", "repetitions" : 10000, "operation_gen_alea" : "numpy.random.rand()"},
]

for factors in factor_combinations:
    generated_code = template.render(factors)
    with open('generated_property_check.py','w') as f:
        f.write(generated_code)
    print(f"Running check for factors: {factors}")
    exec(generated_code)