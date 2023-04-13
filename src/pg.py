from feature import Feature
from typing import Self

class PythonGenerator():

    # Singleton

    def __new__(cls) -> Self:        
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def set_features(self: Self, features: dict[str, Feature]) -> Self:
        self.features = features
        return self

    # Requirement checkers

    def on(self: Self, feature_name: str) -> bool:
        return self.features[feature_name].value()

    def none(self: Self, *features_names: str) -> bool:
        return True

    def any(self: Self, *feature_names: str) -> bool:
        for feature_name in feature_names:
            if self.features[feature_name].value():
                return True
        else:
            return False

    def all(self: Self, *feature_names: str) -> bool:
        for feature_name in feature_names:
            if not self.features[feature_name].value():
                return False
        else:
            return True
