from bs4 import BeautifulSoup as BS
from minify_html import minify

# Which Parts to get:

html_parts = [
    'navbar-horizontal-1',
    'footer-1'
]


# Get each part and add to css, js file

css = ''
js = ''
for html_part in html_parts:
    html_file = f"html/{html_part}.html"
    with open(html_file, 'r') as file:
        html = file.read()
    soup = BS(html, 'html5lib')
    if soup.find('style'):
        css += str(soup.find('style').contents[0])
    if soup.find('script'):
        js += str(soup.find('script').contents[0])

with open('output/style.css', 'w') as file:
    file.write(minify(css))

with open('output/script.js', 'w') as file:
    file.write(minify(js))