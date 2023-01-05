import math

class Category:
  name = ""
  ledger = []
  balance = 0
  spent = 0
  
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.balance = 0
    self.spent = 0
    
  def get_balance (self):
    return self.balance
  
  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    return False

  def deposit(self,amount,description=""):
    self.ledger.append( {"amount": amount, "description": description} )
    self.balance += amount

  def withdraw(self,amount,description="",spending=True):
    if not self.check_funds(amount):
      return False
    self.ledger.append( {"amount": -amount, "description": description} )
    self.balance -= amount
    if spending:
      self.spent += amount
    return True

  def transfer(self,amount,target_category):
    if not self.check_funds(amount):
      return False
    self.withdraw(amount,"Transfer to " + target_category.name,False)
    target_category.deposit(amount, "Transfer from " + self.name)
    return True

  def __str__(self):
    name_len = len(self.name)
    number_of_stars = (30 - name_len)//2
    first_line = ["*"] * number_of_stars + list(self.name) + ["*"] * number_of_stars
    if len(first_line) == 29:
      first_line.append("*")
    ans = [ "".join(first_line) ]
    
    for amount_description in self.ledger:
      amount = amount_description["amount"]
      description = amount_description["description"]
      line_first_part = description.ljust(23)[:23]
      line_second_part = '{0:.2f}'.format(amount)
      ans.append (line_first_part + line_second_part.rjust(7)[-7:])

    ans.append ("Total: " + '{0:.2f}'.format(self.balance))
    return "\n".join(ans)

def create_spend_chart(categories):
  total_spent = sum( cat.spent for cat in categories )
  ans = [list("Percentage spent by category")]
  for i in reversed(range(0,110,10)):
    ans.append( list(str(i).rjust(3)) + ["|", " "] )
  
  middle_line = [" "] * 4 + ["-"] * (len(categories) * 3 + 1)
  ans.append(middle_line)
  
  max_len_of_names = max( len(cat.name) for cat in categories )
  for i in range(max_len_of_names):
    ans.append([" "] * 5)
  for cat in categories:
    # make bars going up
    number_of_o_in_bar = math.floor(cat.spent*10/total_spent)+1
    for i in range(number_of_o_in_bar):
      ans[11-i] += ["o", " ", " "]
    for i in range(number_of_o_in_bar,11):
      ans[11-i] += [" "] * 3
    # make numbers going down
    for index,letter in enumerate(list(cat.name)):
      ans[13+index] += [letter] + ([" "] * 2)
    for i in range(len(cat.name),max_len_of_names):
      ans[13+i] += [" "] * 3

  for i in range(len(ans)):
    ans[i] = "".join(ans[i])
  return "\n".join(ans)