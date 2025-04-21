***
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
***


Attempt 1 
class Solution(object):
    def isAnagram(self, s, t):
        hashS = {}
        hashT = {}

        for letter in s:
            if letter not in hashS:
                hashS[letter] = 1
            else:
                hashS[letter] += 1

        for letter in t:
            if letter not in hashT:
                hashT[letter] = 1
            else:
                hashT[letter] += 1
        
        return hashS == hashT