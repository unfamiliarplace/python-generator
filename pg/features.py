# Data

names = [    

      # line types
      "comments",
      "statements",
      "expressions",
      "decorators",
      "symbol_practice",
      "real_world",

      # components
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
    ]

values = {}

# Utilities

def reset_features(polarity: bool=False) -> None:
    for name in names:
        values[name] = polarity

def update_features(current_features: dict[str, bool]={}) -> None:
    if current_features:
        reset_features()
        current_features = dict(current_features) # Transcrypt bs
        for (key, value) in current_features.items():
            values[key] = value

# Requirement checkers

def on(feature_name: str) -> bool:
    return values.get(feature_name, False)

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

# Initialize

reset_features(False)
