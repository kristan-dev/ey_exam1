import re

def camel_to_snake(input_str):
  name = input_str
  name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
  return name

if(__name__ == "__main__"):
  print(camel_to_snake("ThisIsAwesome"))
  pass