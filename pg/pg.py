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

    def generate(self: Self, features: dict[str, Feature]=None) -> str:
        if features is not None:
            self.set_features(features)
        
        return str(Line())
        

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

# Stupid to avoid import circularity...

from mixins.pg_mixin_renderable import Mixin_Renderable
from mixins.pg_mixin_renderable_operation import Mixin_Renderable_Operation

from formula.pg_sequence import Sequence
from formula.pg_formula_node import Formula_Node, FN
from formula.pg_formula_requirement import Formula_Requirement, FR
from formula.pg_formula_pattern import Formula_Pattern, FP

from mixins.pg_mixin_generatable import Mixin_Generatable

from expressions.pg_boolean import Boolean
from expressions.pg_container import Container
from expressions.pg_float import Float
from expressions.pg_integer import Integer
from expressions.pg_number import Number
from expressions.pg_string import String
from expressions.pg_variable import Variable
from expressions.pg_function_call import Function_Call, Return_Type, RT
from expressions.pg_expression import Expression
from expressions.pg_none import None_Node
from expressions.pg_exception import Exception

from statements.pg_control import Control
from statements.pg_function_definition import Function_Definition
from statements.pg_function_lambda import Function_Lambda
from statements.pg_import import Import
from statements.pg_statement import Statement

from lines.pg_assignment import Assignment
from lines.pg_decorator import Decorator
from lines.pg_real_world import Real_World
from lines.pg_symbol_practice import Symbol_Practice
from lines.pg_comment import Comment
from lines.pg_line import Line

# create JS variable
pygen = PythonGenerator()
