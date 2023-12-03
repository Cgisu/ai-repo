"""Advent 2023 Day 2: Cube Conundrum"""

import re
import sys
import math

RAW = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

cube_configs = {
  'red': 12,
  'green': 13,
  'blue': 14
}

def parse(raw: str) -> list[str]:
  """Convert raw string to list of strings."""
  return raw.split('\n')

def get_id(line: str) -> str:
  """Get the game id"""
  return line.split(':')[0].split(' ')[-1]

def list_of_infos (line: str) -> list[list[str]]:
  """Returns games' list as a list of strings"""
  raw_infos = line.split(':')[1].split(';')
  pattern = r'\d+ \w+' # 'value color' string match
  infos_list = [re.findall(pattern, info) for info in raw_infos]

  return infos_list

def min_possible_power(line: str) -> int:
  """ Returns min possible"""
  infos_list = list_of_infos(line)
  cube_colors = { k: -1 * sys.maxsize for k, v in cube_configs.items()} # max int

  for infos in infos_list:
    for info in infos:
      value, color = info.split(' ')
      if cube_colors[color] < int(value):
        cube_colors[color] = int(value) # update each color fewest value that make the game possible

  return math.prod(cube_colors.values())

def is_impossible(line: str) -> bool:
  """Check if it would be impossible"""
  infos_list = list_of_infos(line)

  for infos in infos_list:
    for info in infos:
      value, color = info.split(' ')
      if cube_configs[color] < int(value):
        return True
  
  return False

if __name__ == '__main__':
  # test input
  total = sum([int(get_id(line)) 
              for line in parse(RAW) 
              if not is_impossible(line)])

  print(total)
  
  # input file
  with open('./advent2023/day02/day02.txt') as f:
    games = f.read()
    total_ids = sum([int(get_id(line)) 
                for line in parse(games) 
                if not is_impossible(line)])
    
    total_power = sum([ min_possible_power(line)
                for line in parse(games)])

  print('total_id:', total_ids)
  print('total_power:', total_power)