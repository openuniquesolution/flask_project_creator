import re

def render(template, values):
    # %% <value name>%%
    pattern = re.compile(r'%%.*%%')
    matches = pattern.finditer(template)
    for match in matches:
       print (match) 

    