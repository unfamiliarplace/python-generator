from components.pg_sequence import PG_Sequence
from feature import Feature
from typing import Self

class PythonGenerator():

    def __init__(self: Self, features: dict[str, Feature]) -> None:
        self.features = features

    def on(self: Self, feature_name: str) -> bool:
        return self.features[feature_name].value()
    
    # Requirement checkers

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
