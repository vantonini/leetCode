class Solution:
  def roman_to_decimal(roman_num):
      roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
      decimal_num = 0
      prev_num = 0
      for char in roman_num[::-1]:
          curr_num = roman_dict[char]
          if curr_num < prev_num:
              decimal_num -= curr_num
          else:
              decimal_num += curr_num
          prev_num = curr_num
      return decimal_num