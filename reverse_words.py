
def reverse_words(input_list):
  reverse_list = []
  start = 0
  end = 0
  temp = ""

  for i in range(0, len(input_list), 1):
    check = input_list[i]
    if(input_list[i] == " "):
      end = i
      temp = "".join(input_list[start:end])
      reverse_list.append(temp)
      start = end
      end = 0
      temp = ""
  
  return reverse_list[::-1]


if(__name__ == "__main__"):
  input_list = [
    "c", "a", "k", "e", " ",
    "p", "o", "u", "n", "d", " ",
    "s","t","e","a","l"," "
  ]
  print(input_list)
  print("".join(reverse_words(input_list)))
  pass