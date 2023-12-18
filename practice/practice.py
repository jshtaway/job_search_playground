import random
import numpy as np
import re
import string

def random_list(length, sorted = False):
    l = [random.randint(1,100) for i in range (length)]
    if sorted:
        l.sort()
    return l

class MaximizeWater:
    """
    INTERVIEW QUESTION
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.
    """
    number_of_tests = 100

    def incriment_by(self, i, j, array):
        """
        Given an array of integers and two indices i and j, this function returns a tuple (iinc, jinc) where:
        - iinc is 1 if array[i] >= array[j], otherwise 0
        - jinc is 0 if array[j-1] >= array[i+1], otherwise -1
        
        If array[i] == array[j] and array[i+1] == array[j-1], the function recursively calls itself
        with i+1 and j-1 until the values are different.
        """
        if i >= j-1:
            # area will be zero, and it doesnt matter which value is incrimented
            return (1,0)
        if array[i] < array[j]:
            (i, j) = (1, 0)
        elif array[i] > array[j]:
            (i, j) = (0, -1)
        # TODO: turns out if the values are the same it doesnt matter!
        else: # values are equal
            if array[i + 1] > array[j - 1]:
                (i, j) = (1, 0)
            elif array[i + 1] < array[j - 1]:
                (i, j) = (0, -1)
            # TODO: turns out if the values are the same it doesnt matter!
            else: # values are equal
                i, j = self.incriment_by(i + i, j - 1, array)
        return i, j
            
    def find_max_area(self):
        array = [random.randint(1,9) for i in range(10)]
        area = lambda i, j : min(array[i], array[j])*abs(i-j)

        max_area = 0; winning_numbers = []
        for i,ival in enumerate(array):
            for j,jval in enumerate(array[i+1:]):
                max_area = max(max_area, area(i,(j+i+1)))
        indices = []
        for i,ival in enumerate(array):
            for j,jval in enumerate(array[i+1:]):
                if (curr_area := area(i,(j+i+1))) == max_area:
                    print(curr_area)
                    indices.append((i,j+i+1))
        for i,j in indices:
            assert(min(array[i], array[j])*abs(j-i) == max_area)

        print(array)

        # another approach
        i = 0; j = len(array)-1; nmax_area = 0
        while i < j :
            nmax_area = max(area(i,j), nmax_area)
            iinc, jinc = self.incriment_by(i,j, array)
            i += iinc
            j += jinc

        assert(max_area == nmax_area)

    def find_n_max_areas(self):
        for i in range(self.number_of_tests):
            self.find_max_area()

class MoveStuff:
    """
    You are given N blocks and the ith block is at position A[i]
. Your task is to move every block to one single position. For that you can perform any of the two moves any number of times(possibly zero) on any block:
1. Move the ith block by 2 units to the left or to the right with a cost of 0.
2. Move the ith block by 1 unit to the left or to the right with a cost of 1.

It is possible that there is more than one block at the same position initially.

Input format
The first line contains an integer T, denoting the number of test cases.
For each test case, The first line contains one integer N.
The second line contains N space-separated integers.

Output format
For each test case print on a new line, print the minimum cost to move all the blocks to the same position(any position).

Constraints
1 <= T <= 10

1 <= N <= 10^5

1 <= A[i] <= 10^5

Time Limit
1 second

Example
Input
2
6
1 3 3 6 4 8
5
9 2 1 7 8

Output
3
2
    """
    n = 100000000
    T = 1000
    # [1] # 0
    # [1, 2] #1
    # [1, 2, 3] #2
    # [1, 2, 3, 4] #2
    # [1, 2, 3, 4, 5] #2
    # [1, 2, 3, 4, 5, 6] #3
    # [1, 2, 3, 4, 5, 6, 7] #4
    # [1, 2, 3, 4, 5, 6, 7, 8] #4
    # [1, 2, 3, 4, 5, 6, 7, 8, 9] #4
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #5

    def calculate_stuf(self):
        center = self.n/2 if self.n % 2 == 0 else (self.n/2 + .5)
        even = lambda i: bool(i%2 == 0)
        odd = lambda i: bool(i%2 == 1)
        xor = lambda i, j: 1 if (even(i) and not even(j)) or (even(j) and not even(i)) else 0
        return (
            sum([xor(i, center) for i in range(1, int(center))]) +
            sum([xor(i, center) for i in range(int(center + 1), self.n+1)])
        )

    def calculate_stuff2(self):
        #another way 
        center = self.n/2 if self.n % 2 == 0 else (self.n/2 + .5)
        even = lambda i: bool(i%2 == 0)
        odd = lambda i: bool(i%2 == 1)
        xor = lambda i, j: 1 if (even(i) and not even(j)) or (even(j) and not even(i)) else 0

        evens = self.n / 2 if even(self.n) else self.n/2-.5
        odds = self.n / 2 + .5 if not even(self.n) else self.n / 2
        if odd(self.n):
            return odds if even(center) else evens
        if even(self.n):
            return evens

    def test_calculate_stuff(self):
        for i in range(self.T):
            self.n = i# random.randint(1,10)
            assert(self.calculate_stuf() == self.calculate_stuff2())

class MergeSort:
    def mergeSort(self, myList):
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]
            # Recursive call on each half
            self.mergeSort(left)
            self.mergeSort(right)
            # Two iterators for traversing the two halves
            i = 0
            j = 0
            # Iterator for the main list
            k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    # The value from the left half has been used
                    myList[k] = left[i]
                    # Move the iterator forward
                    i += 1
                else:
                    myList[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k]=right[j]
                j += 1
                k += 1
        return myList

    def test_merge_sort(self):
        for i in range(10):
            womp = random_list(10)
            print(f"unsorted: {womp}")
            sorter = MergeSort()
            print(f"sorted: {sorter.mergeSort(womp)}")

class MediamOfTwoLists:
    def find_median(self, nums1, nums2):
        my_lists = {False : nums1, True : nums2}
        my_pointers = {False: -1, True: -1}
        curr_list = bool(np.argmin([
            my_lists[False][my_pointers[False] +1],
            my_lists[True][my_pointers[True] +1]
        ]))
        my_pointers[curr_list] += 1
        total_len = len(nums1)+len(nums2)
        median_location = total_len // 2
        for i in range(0, median_location-1):
            curr_list, my_pointers = self.calculate_next_number(my_lists, my_pointers, curr_list)
            print(my_lists[curr_list][my_pointers[curr_list]])
        if median_location-1 == 0:
            curr_list, my_pointers = self.calculate_next_number(my_lists, my_pointers, curr_list)
        if total_len % 2 == 1:
            median = my_lists[curr_list][my_pointers[curr_list]]
        else:
            n1 = my_lists[curr_list][my_pointers[curr_list]]
            curr_list, my_pointers = self.calculate_next_number(my_lists, my_pointers, curr_list)
            n2 = my_lists[curr_list][my_pointers[curr_list]]
            median = (n1+n2)/2
        return median
                
    def calculate_next_number(self, my_lists, my_pointers, curr_list):
        # if the next index in the current list is lower than
        # the next index in the other list, move the pointer up in the
        # current list and keep the current list the same
        if (
            len(my_lists[curr_list]) > my_pointers[curr_list] + 1
            and len(my_lists[not curr_list]) > my_pointers[not curr_list] + 1 
        ):
            if (
                my_lists[curr_list][my_pointers[curr_list] + 1]
                < my_lists[not curr_list][my_pointers[not curr_list] +1]
            ):
                my_pointers[curr_list] += 1
            # if the next index in the other list is lower than the next
            # index in the current list, make the current list the other
            # list and increase the index
            elif (
                my_lists[not curr_list][my_pointers[not curr_list] +1]
                < my_lists[curr_list][my_pointers[curr_list] + 1]
            ):
                curr_list = not curr_list
                my_pointers[curr_list] += 1
        # the left overs, one of the lists are not interable
        # its reached the end
        elif len(my_lists[curr_list]) > my_pointers[curr_list] + 1 :
            my_pointers[curr_list] += 1
        elif len(my_lists[not curr_list]) > my_pointers[not curr_list] + 1 :
            curr_list = not curr_list
            my_pointers[curr_list] += 1
        return curr_list, my_pointers

    def test_find_median(self):
        for i in range(10):
            nums1 = random_list(random.randint(1,8), sorted = True)
            nums2 = random_list(random.randint(1,8), sorted = True)

            print(f"nums1: {nums1}\nnums2: {nums2}")
            print(f"median: {self.find_median(nums1, nums2)}")

class CreateTheLargestSquare:
    """Given two sticks, cut them into four sticks in order to create the largest possible shape."""

    def cut_two_sticks(self, stick_lengths):
        if len(stick_lengths) < 4:
            i = np.argmax(stick_lengths)
            stick_lengths = stick_lengths[:i] + [stick_lengths[i]/2]*2 + stick_lengths[i+1:]
        if len(stick_lengths) < 4:
            return self.cut_two_sticks(stick_lengths)
        else:
            print(stick_lengths)
            return stick_lengths


    def test_cut_two_sticks(self):
        for i in range(10):
            stick_lengths = random_list(2)
            print(stick_lengths)
            self.cut_two_sticks(stick_lengths)

class CreateRegex:
    """
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).

    

    Example 1:

    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    Example 2:

    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    Example 3:

    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".
    

    Constraints:

    1 <= s.length <= 20
    1 <= p.length <= 20
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
    """
    def matches(self, s, p, pi = 0, si = 0):
        # -- weird cases ---
        if pi == 0 and p[pi] == "*":
            return False
        # --- --- --- --- --
        try:
            if s[si] == p[pi] or p[pi] == '.':
                si += 1; pi += 1
            elif p[pi] == "*":
                if (s[si] == p[pi-1] or p[pi-1] == '.'):
                    while si < len(s) and (s[si] == p[pi-1] or p[pi-1] == '.'):
                        si+=1
                        if pi+1 == len(p) or self.matches(s, p, pi+1, si):
                            return True
                pi += 1
            else:
                return False
            if si < len(s) and pi < len(p):
                return self.matches(s, p, si, pi)
            elif si == len(s) and pi == len(p):
                return True
            else:
                return False
        except:
            return False

    def matches_chatGPT(self, s, p):
        # Create a 2D DP table initialized to False
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # Empty pattern matches empty string
        dp[0][0] = True
        # Handle patterns with '*'
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        # Populate the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        return dp[len(s)][len(p)]
    
    def test_matches(self):
        test_count = 100000
        sp = [("aa", "aa"), ("aa", "a."), ("aa", "a"), ("aaaa", "aa.*"), ("aa", "a*")]
        sp = [
            (
                "".join([random.choice(string.ascii_lowercase) for i in range(random.randint(1,4))]),
                "".join([random.choice(string.ascii_lowercase + "." + "*") for i in range(random.randint(1,4))]),
            )
            for i in range(test_count)
        ]
        clean_sp = [i for i in sp if not i[1].startswith("*") and not "**" in i[1]]
        inaccurate_count = 0
        for i, (s, p) in enumerate(clean_sp):
            try:
                assert(p.startswith("*") or self.matches_chatGPT(s, p) == bool(re.search(fr"^{p}$", s)))
            except:
                inaccurate_count += 1
        print(f"accuracy of method: {(test_count - inaccurate_count)/test_count*100}%")
# medianer = MediamOfTwoLists()
# medianer.test_find_median()

# cutter = CreateTheLargestSquare()
# print(cutter.test_cut_two_sticks())

matcher = CreateRegex()
matcher.test_matches()

