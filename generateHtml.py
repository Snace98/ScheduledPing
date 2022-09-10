from jinja2 import Template

def generateHtml(pingData):
    with open('pingTemplate.html') as f:
        tmpl = Template(f.read());
        htmlRawText = tmpl.render(pingData = pingData)
    
    with open('pingData.html', 'w') as f:
        f.write(htmlRawText)