from feature import Feature, Dummy_Feature
from lines.pg_line import Line

class PythonGenerator():

    def generate(self, current_features: dict[str, Feature]={}) -> str:
        if current_features:
            current_features = dict(current_features) # Transcrypt bs
            for (k, v) in current_features.items():
                features[k] = v
        
        return str(Line())
    
    # Requirement checkers

    def on(self, feature_name: str) -> bool:
        return features.get(feature_name, Dummy_Feature()).value()

    def none(self, *features_names: str) -> bool:
        return True

    def any(self, *feature_names: str) -> bool:
        for feature_name in feature_names:
            if features.get(feature_name, Dummy_Feature()).value():
                return True
        else:
            return False

    def all(self, *feature_names: str) -> bool:
        for feature_name in feature_names:
            if not features.get(feature_name, Dummy_Feature()).value():
                return False
        else:
            return True

# create JS variable
features = {
    'real_world': True,
    'expressions': True,
    'math': True
}
pygen = PythonGenerator()
