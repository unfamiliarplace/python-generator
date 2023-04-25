from pg import pygen
import features

if __name__ == '__main__':
  off = ['maps', 'functions', 'classes', 'files', 'containers']

  current_features = {}
  for name in features.values:
      current_features[name] = name not in off

  line = pygen.generate(current_features)
  print(line)
