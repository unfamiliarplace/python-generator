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

# Stupid prenames to avoid circular dependencies failing

class Mixin_Generatable: pass
class Mixin_Renderable: pass
class Mixin_Renderable_Operation: pass

class Sequence: pass
class Formula_Node: pass
class Formula_Requirement: pass
class Formula_Pattern: pass

from formula.pg_sequence import Sequence
from formula.pg_formula_node import Formula_Node
from formula.pg_formula_requirement import Formula_Requirement
from formula.pg_formula_pattern import Formula_Pattern

from mixins.pg_mixin_generatable import Mixin_Generatable
from mixins.pg_mixin_renderable import Mixin_Renderable
from mixins.pg_mixin_renderable_operation import Mixin_Renderable_Operation

FP = Formula_Pattern
FN = Formula_Node
FR = Formula_Requirement

class Boolean: pass
class Container: pass
class Float: pass
class Integer: pass
class Number: pass
class String: pass
class Variable: pass
class Function_Call: pass
class Expression: pass

class Control: pass
class Function_Definition: pass
class Function_Lambda: pass
class Import: pass
class Statement: pass

class Assignment: pass
class Decorator: pass
class Real_World: pass
class Symbol_Practice: pass
class Line: pass

from expressions.pg_boolean import Boolean
from expressions.pg_container import Container
from expressions.pg_float import Float
from expressions.pg_integer import Integer
from expressions.pg_number import Number
from expressions.pg_string import String
from expressions.pg_variable import Variable
from expressions.pg_function_call import Function_Call
from expressions.pg_expression import Expression

from statements.pg_control import Control
from statements.pg_function_definition import Function_Definition
from statements.pg_function_lambda import Function_Lambda
from statements.pg_import import Import
from statements.pg_statement import Statement

from lines.pg_assignment import Assignment
from lines.pg_decorator import Decorator
from lines.pg_real_world import Real_World
from lines.pg_symbol_practice import Symbol_Practice
from lines.pg_line import Line
