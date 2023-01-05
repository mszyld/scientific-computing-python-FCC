import re

def arithmetic_arranger(problems, compute = False):

  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:
    if problem.find('/') != -1 or problem.find('*') != -1:
      return "Error: Operator must be '+' or '-'."
  for problem in problems:
    if re.search("[^\s0-9+-]", problem):
      return "Error: Numbers must only contain digits."
  for problem in problems:
    problem_as_list = problem.split()
    if len(problem_as_list[0]) > 4 or len(problem_as_list[-1]) > 4:
      return "Error: Numbers cannot be more than four digits."

  if compute:
    LINES = 4
  else:
    LINES = 3  
  arranged_problems = [[] for _ in range(LINES)]
  
  for index,problem in enumerate(problems):
    problem_as_list = problem.split()
    first_number = problem_as_list[0]
    operator = problem_as_list[1]
    second_number = problem_as_list[2]
    total_len = max(len(first_number),len(second_number)) + 2
    
    before_first_number = [" "] * (total_len - len(first_number))
    arranged_problems[0].append("".join(before_first_number + [first_number]))
    before_second_number = [operator] + [" "] * (total_len - len(second_number) - 1)
    arranged_problems[1].append("".join(before_second_number + [second_number]))
    arranged_problems[2].append("".join(["-"] * total_len))
    
    if compute:
      result = int(first_number)
      if operator == "+":
        result += int(second_number)
      if operator == "-":
        result -= int(second_number)
      result = str(result)
      before_result = [" "] * (total_len - len(result))
      arranged_problems[3].append("".join(before_result + [result]))
    
  for i in range(LINES):
    arranged_problems[i] = "    ".join(arranged_problems[i])
  return "\n".join(arranged_problems)
