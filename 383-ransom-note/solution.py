class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # convert magazine to a list of characters
        mag_list = list(magazine)
        # iterate over the characters in the ransom note
        for char in ransomNote:
            # if the character is not in the magazine, return False
            if char not in mag_list:
                return False
            # otherwise, remove the character from the magazine list
            mag_list.remove(char)
        # if we get here, the ransom note can be constructed
        return True