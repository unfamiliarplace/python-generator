# create JS variable
names = [
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

values = {name: False for name in names}

# Requirement checkers

def on(feature_name: str) -> bool:
    return values.get(feature_name, False())

def none(*_) -> bool:
    return True

def any(*feature_names: str) -> bool:
    for feature_name in feature_names:
        if values.get(feature_name, False):
            return True
    else:
        return False

def all(*feature_names: str) -> bool:
    for feature_name in feature_names:
        if not values.get(feature_name, False):
            return False
    else:
        return True
