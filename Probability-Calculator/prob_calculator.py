import copy
import random
from collections import Counter

class Hat:
  contents = []
  
  def __init__(self, **balls):
    self.contents = []
    for color in balls:
      for _ in range(balls[color]):
        self.contents.append(color)

  def draw(self,quantity):
    if quantity > len(self.contents):
      return self.contents
    result = random.sample(self.contents,quantity)
    for item in result:
      self.contents.remove(item)
    return result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  ans = 0
  for i in range(num_experiments):
    hat_for_this_experiment = copy.deepcopy(hat)
    sample = Counter(hat_for_this_experiment.draw(num_balls_drawn))
    successful_experiment = True
    for color in expected_balls:
      if color not in sample or sample[color] < expected_balls[color]:
        successful_experiment = False
        break
    ans += successful_experiment
  return ans/num_experiments
