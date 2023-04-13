from feature import Feature
from pg import PythonGenerator as PG
from components.pg_line import PG_Line

feature_names = [
    "variables",
    "math",
    "strings",
    "booleans",
    "containers",
    "indexing",
    "maps",
    "imports",
    "functions",

    # line types
    "comments",
    "statements",
    "expressions",
    "decorators",
    "symbol_practice",
    "real_world"
  ]

disabled = ['containers', 'arrays', 'maps', 'imports', 'functions']

features = {}

for name in feature_names:
    feature = Feature(name)
    feature.disable(name not in disabled)
    feature.value(name not in disabled)

    features[name] = feature

pg = PG().set_features(features)
line = PG_Line()
render = str(line)
print(render)
