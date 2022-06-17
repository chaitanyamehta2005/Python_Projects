"""
Question:
A bigram or digram is a sequence of two adjacent elements from a string of tokens, which are typically letters, syllables, or words. A bigram is an n-gram for n=2. The frequency distribution of every bigram in a string is commonly used for simple statistical analysis of text in many applications, including in computational linguistics, cryptography, speech recognition, and so on.
Original list:
['Sum all the items in a list', 'Find the second smallest number in a list']
Bigram sequence of the said list:
[('Sum', 'all'), ('all', 'the'), ('the', 'items'), ('items', 'in'), ('in', 'a'), ('a', 'list'), ('Find', 'the'), ('the', 'second'), ('second', 'smallest'), ('smallest', 'number'), ('number', 'in'), ('in', 'a'), ('a', 'list')]
"""


Orig_list = ['Sum all the items in a list']
print(list(*Orig_list))
