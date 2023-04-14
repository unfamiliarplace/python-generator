from feature import Feature
import pg

feature_names = [
    "variables",
    "math",
    "strings",
    "booleans",
    "containers",
    "control",
    "indexing",
    "maps",
    "imports",
    "functions",
    "methods",

    # line types
    "comments",
    "statements",
    "expressions",
    "decorators",
    "symbol_practice",
    "real_world"
  ]

disabled = ['maps', 'functions',
    
    # testing real world
    "comments",
    "statements",
    "expressions",
    "decorators",
    "symbol_practice",
]

features = {}

for name in feature_names:
    feature = Feature(name)
    feature.disable(name not in disabled)
    feature.value(name not in disabled)

    features[name] = feature

pg.PythonGenerator().set_features(features)
line = pg.Line()
render = str(line)
print(render)
