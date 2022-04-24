class Node:
  def __init__(self, children, max):
    self.children = [max] * children
    self.children[-1] += 1
    self.size = children
    self.max = max

  def getNextNumber(self):
    i = self.size - 1
    while self.children[i] == 1:
      self.children[i] = self.max
      i -= 1
      if i == -1:
        return None
        
    self.children[i] -= 1
    return self.children


def getCombs(n, m, D, comparisonAlgo):
  # n is the number of dice
  # m is the number of dice kept with advantage
  # D is the dN, or the type of dice that it is
  # n >= m
  combs = {}
  total = 0
  totalNum = 0
  node = Node(n, D)
  while True:
    nextNum = node.getNextNumber()
    if nextNum == None:
      break
    adNum = nextNum[::]
    set = m
    while set < n:
      adNum = comparisonAlgo(adNum)
      set += 1
    summed = sum(adNum)
    totalNum += summed
    if sum(adNum) in combs.keys():
      combs[sum(adNum)] += 1
    else:
      combs[sum(adNum)] = 1
    total +=1

  print(combs, total, totalNum / total)


def removeSmallest(li):
  li = li[::]
  # removes the smallest number from a list.
  num = (0, li[0])
  for i in range(1, len(li)):
    if num[1] > li[i]:
      num = (i, li[i])
  li.pop(num[0])
  return li

def removeBiggest(li):
  li = li[::]
  # removes the smallest number from a list.
  num = (0, li[0])
  for i in range(1, len(li)):
    if num[1] < li[i]:
      num = (i, li[i])
  li.pop(num[0])
  return li

getCombs(4, 3, 6, removeSmallest)