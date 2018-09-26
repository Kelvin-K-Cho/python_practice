import math
import string

def vol(rad):
  return (4/3)*(math.pi)*(rad**3)

def ran_check(num,low,high):
  return low <= num <= high

def up_low(s):
  uppercase_count = 0
  lowercase_count = 0
  for char in s:
    if char.isupper():
      uppercase_count += 1
    elif char.islower():
      lowercase_count += 1

  return f"No. of Upper case characters : {uppercase_count} \nNo. of Lower case characters : {lowercase_count}"

def unique_list(lst):
  unique = [];
  lookup = {};
  for num in lst:
    check = lookup.get(num);
    if check:
      continue;
    else:
      unique.append(num)
      lookup[num] = True
  return unique

def multiply(numbers):
  result = 1;
  for num in numbers:
    result *= num
  return result

def palindrome(s):
  for index, char in enumerate(s):
    if char != s[len(s) - 1 - index]:
      return False
  return True

def ispangram(str1, alphabet=string.ascii_lowercase):
  compare = []
  lookup = {}
  array = str1.split()
  str1 = "".join(array)
  for char in str1:
    check = lookup.get( char.lower() )
    if check:
      continue
    else:
      compare.append( char.lower() )
      lookup[char.lower()] = True

  return len(alphabet) == len(compare)
