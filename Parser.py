def generate_AST(string):
  number_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-']
  ind = 1 
  arr_to_return = []
  while ind < len(string):
    char = string[ind] 
    if char == "(":
      open_cnt = 1 
      closed_cnt = 0
      sub_str = "("
      for c in string[ind + 1:]: 
        if c == "(": open_cnt += 1
        if c == ")": closed_cnt += 1
        sub_str += c 
        if open_cnt == closed_cnt: break
      arr_to_return.append(generate_AST(sub_str)) 
      ind += len(sub_str)
    elif char == " " or char == ")":
      ind += 1
    else:
      stop_ind = string.find(" ", ind)
      if stop_ind == -1:
        stop_ind = string.find(")", ind) 
      s = string[ind:stop_ind]
      if all(x in number_symbols for x in list(s)):
        if s.find('-', 1) == -1:
          num = float(s)
          arr_to_return.append(num)
      else:
        arr_to_return.append(s)
      ind = stop_ind + 1 
  return arr_to_return


if __name__ == "__main__":
    ip = "(first (list -1.5 (+ 2 3) 9))" # lisp
    print("Input(LISP):", ip)
    print("Output (AST):", generate_AST(ip))
