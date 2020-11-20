
def bracket_validator(input_str):
  open_list = ["[","{","("] 
  close_list = ["]","}",")"] 
  stack = []

  for i in input_str:
    if(i in open_list):
      stack.append(i)
    
    if(i in close_list):
      pos = close_list.index(i)
      if(len(stack) > 0 and (open_list[pos] == stack[len(stack)-1])):
        stack.pop()
      else:
        return "Not nested properly"
  
  if(len(stack) == 0):
    return "Nested properly"
  else:
    return "Not nested properly"


if(__name__ == "__main__"):
  print(bracket_validator(input_str=r"((()"))
  pass