"""Advent 2023 Day 3: Gear Ratios"""

import re
import math
from dataclasses import dataclass
from typing import NamedTuple, List, Dict

class XY(NamedTuple):
    #store the coordinate of a number
    x: int
    y: int

@dataclass
class Number:
    #store the start, end and value of a number
    start: XY
    end: XY
    value: int

def is_adjacent(symbol_location: XY, number: Number) -> bool:
    """Check if adjucent"""
    
    nx_low, nx_high = number.start.x, number.end.x # number's lower bound and number higher bound along x direction
    ny = number.start.y # number's lower bound and number higher bound along y direction

    x, y = symbol_location

    return nx_low - 1 <= x <= nx_high + 1 and ny - 1 <= y <= ny + 1

@dataclass
class Schematic:
    # store the schmatic
    numbers: List[Number]
    symbols: Dict[XY, str]

    def part_numbers(self) -> List[int]:
        """collect the part numbers in a list"""
        return [number.value for number in self.numbers if self.adjacent_to_symbol(number)]
    
    def adjacent_to_symbol(self, number: Number) -> bool:
       
        return any(
           is_adjacent(symbol_location, number) 
           for symbol_location in self.symbols
        )
    def gear_ratios(self) -> List[int]:
        """return gear ratios"""
        output: List[int] = []
        possible_gears = [loc for loc, symbol in self.symbols.items() if symbol == '*']

        for poss_gear in possible_gears:
            adjacent_numbers_to_poss_gear = [n.value for n in self.numbers if is_adjacent(poss_gear, n)]
            if len(adjacent_numbers_to_poss_gear) == 2:
                output.append(math.prod(adjacent_numbers_to_poss_gear))
        
        return output

def parse(raw: str) -> Schematic:
    lines = raw.splitlines()
    numbers = []
    symbols = {}

    for y, line in enumerate(lines):
        # handle numbers
        for match in re.finditer('\d+', line):
            start = XY(match.start(), y)
            end = XY(match.end() - 1, y)
            numbers.append(Number(start, end, int(match.group())))
        
        # handle symbols
        for x, symbol in enumerate(line):
            if not symbol.isdigit() and symbol != '.':
                symbols[XY(x, y)] = symbol

    return Schematic(numbers, symbols)

if __name__ == '__main__':
    RAW = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    SCHEMATIC = parse(RAW)
    assert sum(SCHEMATIC.part_numbers()) == 4361, 'Not correct'
    assert sum(SCHEMATIC.gear_ratios()) == 467835, 'Not correct'
    
    # read input
    with open('./advent2023/day03/day03.txt') as f:
        schematic = parse(f.read())

    print(sum(schematic.part_numbers()))
    print(sum(schematic.gear_ratios()))