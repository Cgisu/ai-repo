"""Adevent 2023 Day 1: Trebuchet?"""

from enum import Enum
import sys

class Digits(Enum):
  one = 1
  two = 2
  three = 3
  four = 4
  five = 5
  six = 6
  seven = 7
  eight = 8
  nine = 9

RAW = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

RAW_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

def parse(raw: str) -> list[str]:
  """Convert raw string to list of strings."""
  return raw.split('\n')

def digit_index(line: str) -> int:
  """Return digit index"""
  for c in line:
    if c.isdigit():
      return line.index(c)
  return 0

def has_digit_str(line: str) -> bool:
  """Check line has string digit"""
  flag = False
  for digit in Digits:
    if digit.name in line:
      flag = True
      break
  return flag

def digits_str_index(line: str) -> tuple[tuple[int, Digits], tuple[int, Digits]]:
  """Finds the index of numbers in text format"""
  first_digit_str_index = sys.maxsize
  last_digit_str_index = -1 * sys.maxsize
  
  for digit in Digits:
    if digit.name in line:
      if line.index(digit.name) < first_digit_str_index:
        first_digit_str_index = line.index(digit.name)
        first_digit_str = digit

      if line.rindex(digit.name) > last_digit_str_index:
        last_digit_str_index =  line.rindex(digit.name)
        last_digit_str = digit
  
  return (first_digit_str_index, first_digit_str), (0 - (len(line) - last_digit_str_index ), last_digit_str)

def calibration_value(amended_line: str)-> int:
  """Calibration value"""
  if not amended_line.isalpha():
    first_digit_index = digit_index(amended_line)
    first_digit = int(amended_line[first_digit_index])
    last_digit_index = -1 * digit_index(amended_line[::-1]) - 1
    last_digit = int(amended_line[last_digit_index])

    if (has_digit_str(amended_line)):
      first_digit_str, last_digit_str =  digits_str_index(amended_line)
      if first_digit_str[0] < first_digit_index:
        first_digit = first_digit_str[1].value
      if last_digit_str[0] > last_digit_index:
        last_digit = last_digit_str[1].value

    return int(str(first_digit) + str(last_digit))
    
  else:
    if has_digit_str(amended_line):
      first_digit_str, last_digit_str =  digits_str_index(amended_line)
      return int(str(first_digit_str[1].value) + str(last_digit_str[1].value))

  return 0

# part1
total = 0
for line in parse(RAW):
  total += calibration_value(line)

print(total)

# part2
total = 0
for line in parse(RAW_2):
  total += calibration_value(line)
  
print(total)

# output
total = 0
with open('day01.txt') as f:
  amended_document = parse(f.read())
  for amended_line in amended_document:
    total += calibration_value(amended_line)

print(total)
