import os, json
ZIISH_CONFIG = os.path.dirname(os.path.realpath(__file__))
(ZIISH_ROOT, config) = os.path.split(ZIISH_CONFIG)
ZIISH_PARAMETERS = os.path.join(ZIISH_CONFIG, 'parameters.json')
# ZIISH_ROOT = os.environ["ZIISH_ROOT"]
ZIISH_TEMPLATE = os.path.join(ZIISH_ROOT, 'Templates')

# os.chdir(root)
PARAMETERS = json.load(file(ZIISH_PARAMETERS))
