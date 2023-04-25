from lines.pg_line import Line
import features

class PythonGenerator():

    def make_line(current_features: dict[str, bool]={}) -> Line:
        features.update_features(current_features)        
        return Line()

    def generate(current_features: dict[str, bool]={}) -> str:
        return str(PythonGenerator.make_line(current_features))

pygen = PythonGenerator
