def lesser_of_two_evens(a,b):

  def is_even(num):
    return num % 2 == 0

  if a < b:
    if is_even(a):
      return a
    else:
      return b
  else:
    if is_even(b):
      return b
    else:
      return a


def animal_crackers(text):
  words = text.split(" ")
  return words[0].lower()[0] == words[1][0].lower()


def makes_twenty(n1, n2):
  return n1 == 20 or n2 == 20 or n1+n2 == 20


def old_macdonald(name):
  string = ""
  for index, char in enumerate(name):
    if index == 0 or index == 3:
      string += char.upper()
    else:
      string += char
  return string


def master_yoda(sentence):
  words = sentence.split(" ")
  words.reverse()
  return " ".join(words)


def almost_there(n):
  if 100 - n <= 10 or n - 100 <= 10:
    return True
  elif 200 - n <= 10 or n - 200 <= 10:
    return True
  else:
    return False


def has_33(nums):
  for index, num in enumerate(nums):
    if num == 3 and index != len(nums)-1:
      if nums[index+1] == 3:
        return True
  return False

def paper_doll(text):
  result = ""
  for char in text:
    result += char*3
  return result


def blackjack(a,b,c):
  cards = [a,b,c]
  total = sum(cards)
  if (total <= 21):
    return total
  else:
    for card in cards:
      if total > 21 and card == 11:
        total -= 10
        if total <= 21:
          return total

    return "BUST"


def summer_69(arr):
  sum = 0
  ignore = False

  for num in arr:
    if num == 6:
      ignore = True
      continue

    if num == 9:
      ignore = False;
      continue

    if ignore:
      continue

    sum += num

  return sum


def spy_game(nums):
  first = second = third = None
  for num in nums:
    if (num == 0 or num == 7):
      if (first == None):
        first = num
      elif (second == None):
        second = num
      elif (third == None):
        third = num
  return [first, second, third] == [0,0,7]


def count_primes(nums):

  primes = []

  if nums <= 1:
    return 0;

  def is_prime(value):
    for num in range(2, value):
      if value % num == 0:
        return False
    return True

  for num in range(2, nums):
    if is_prime(num):
      primes.append(num)

  return len(primes)
