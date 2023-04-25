from lines.pg_line import Line
import features

class PythonGenerator():

    def make_line(current_features: dict[str, bool]={}) -> Line:
        if current_features:
            current_features = dict(current_features) # Transcrypt bs
            for (k, v) in current_features.items():
                features.values[k] = v
        
        return Line()

    def generate(current_features: dict[str, bool]={}) -> str:
        return str(PythonGenerator.make_line(current_features))     

pygen = PythonGenerator
