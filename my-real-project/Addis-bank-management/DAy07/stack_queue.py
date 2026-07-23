from collections import deque

# STACK

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):

        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):

        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

# QUEUE

class Queue:

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):

        if self.is_empty():
            return None

        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

# Balanced Brackets

def balanced_brackets(text):

    stack = Stack()

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in text:

        if ch in "([{":
            stack.push(ch)

        elif ch in ")]}":

            if stack.is_empty():
                return False

            if stack.pop() != pairs[ch]:
                return False

    return stack.is_empty()


print(balanced_brackets("()"))
print(balanced_brackets("{[()]}"))
print(balanced_brackets("{[(])}"))
print(balanced_brackets("(()"))

# Maximum Sliding Window Sum

def max_sliding_window_sum(nums, k):

    q = Queue()

    window_sum = 0
    max_sum = float("-inf")

    for num in nums:

        q.enqueue(num)
        window_sum += num

        if len(q.items) > k:
            window_sum -= q.dequeue()

        if len(q.items) == k:
            max_sum = max(max_sum, window_sum)

    return max_sum


print(max_sliding_window_sum([2,1,5,1,3,2],3))
print(max_sliding_window_sum([1,2,3,4],2))
print(max_sliding_window_sum([5,5,5],2))