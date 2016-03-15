#!/usr/bin/python

"""
using: ./hampath.py input_file

input file - connection matrix for a graph
numbers with ; as separator

ex.

0;1;2
1;0;3
2;3;0
"""

import sys

#Initial node for search \ start element in result chain.
start = 0;

def deep (path):
	for i in range(0, len(matrix[0])):	# len(matrix[0]) - number of iterations
		if matrix[path[-1]][i] != 0:	# path[-1] - last element in chain
			if i not in path:
				newPath = list(path)	# a = b not equal a = copy(b) >_<
				newPath.append(i)

				if len(newPath) == len(matrix[0]):
					if matrix[newPath[0]][newPath[-1]] != 0:
						print newPath
						return 1

				fin = deep ( newPath )
				if fin == 1:			# exit if path found
					return 1

	return 0


f = open (sys.argv[1])
matrix = [ map(int,line.split(';')) for line in f ]


while True:
	my_path = [ start ]
	res = deep( my_path )
	if res == 0 and len(matrix[0]) > start + 1:
		start += 1
	else:
		break