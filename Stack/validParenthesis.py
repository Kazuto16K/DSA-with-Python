class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map_dict = {
            '}':'{',']':'[',')':'('
        }
        stack = Stack()
        for el in s:
            if el == '{' or el == '[' or el == "(":
                stack.push(el)
            else:
                top = stack.peek()
                if top == map_dict[el]:
                    stack.pop()
                else:
                    stack.push(el)
        return stack.size() == 0
    
obj = Solution()
print(obj.isValid("()[]{}"))