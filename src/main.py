from feature import Feature
from python_generator import PythonGenerator as PG

feature_names = [
    "symbols",
    "math",
    "strings",
    "containers",
    "boolean",
    "variables",
    "arrays",
    "maps",
    "control",
    "imports",
    "functions"
  ]

enabled = ['symbols', 'math', 'strings']

features = {}

for name in feature_names:
    feature = Feature(name)
    feature.disable(True)
    feature.value(name in enabled)

    features[name] = feature

prompt = PG.generate(features)
print(prompt)