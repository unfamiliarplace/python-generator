if __name__ == '__main__':

  from feature import Feature
  import pg
  from lines.pg_line import Line

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
      "classes",
      "files",

      # line types
      "comments",
      "statements",
      "expressions",
      "decorators",
      "symbol_practice",
      "real_world"
    ]

  disabled = ['maps', 'functions', 'classes', 'files', 'containers']

  features = {}

  for name in feature_names:
      feature = Feature(name)
      feature.disable(name not in disabled)
      feature.value(name not in disabled)

      features[name] = feature

  pg.features = features
  pg.PythonGenerator().set_features(features)
  line = Line()
  render = str(line)
  print(render)
