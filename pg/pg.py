from feature import Feature
from lines.pg_line import Line

class PythonGenerator():

    # Singleton

    def __new__(cls):        
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def set_features(self, features: dict[str, Feature]):
        self.features = features
        return self

    def generate(self, features: dict[str, Feature]=None) -> str:
        if features is not None:
            self.set_features(features)
        
        return str(Line())
        

    # Requirement checkers

    def on(self, feature_name: str) -> bool:
        return self.features[feature_name].value()

    def none(self, *features_names: str) -> bool:
        return True

    def any(self, *feature_names: str) -> bool:
        for feature_name in feature_names:
            if self.features[feature_name].value():
                return True
        else:
            return False

    def all(self, *feature_names: str) -> bool:
        for feature_name in feature_names:
            if not self.features[feature_name].value():
                return False
        else:
            return True

# create JS variable
pygen = PythonGenerator()
