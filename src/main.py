from feature import Feature
from pg import PythonGenerator as PG
from components.pg_line import PG_Line

feature_names = [
    "symbols",
    "math",
    "strings",
    "containers",
    "boolean",
    "variables",
    "arrays",
    "maps",
    "controls",
    "imports",
    "functions"
  ]

enabled = ['symbols', 'math', 'strings', 'controls']

features = {}

for name in feature_names:
    feature = Feature(name)
    feature.disable(True)
    feature.value(name in enabled)

    features[name] = feature

pg = PG(features)
prompt = PG_Line(pg)
render = str(prompt)
print(render)
