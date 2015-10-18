import jinja2
import os, sys, json
import includes
from Parser import faroo_latest_trends as faroo
from ImageProcessing import extract_front_page_images
try:
    template_file = sys.argv[1]

except Exception, e:
    template_file = "body.html"
os.chdir(includes.ZIISH_ROOT)
faroo_data = faroo.get_faroo_data(100)
front_page_post = extract_front_page_images.extract_front_page_images(faroo_data)
templateLoader = jinja2.FileSystemLoader( searchpath = includes.ZIISH_TEMPLATE)
templateEnv = jinja2.Environment( loader=templateLoader )
template = templateEnv.get_template(template_file)
output = template.render(parameters = includes.PARAMETERS, faroo_data = faroo_data, front_page_post = front_page_post)
print output.encode('utf-8')