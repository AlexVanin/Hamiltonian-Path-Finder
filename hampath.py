#!/usr/bin/python

import sys

start = 0;			#Initial node for search \ start element in result chain.

def deep (path):
	for i in range(0, len(matrix[0])):								# len(matrix[0]) - number of iterations
		if matrix[path[-1]][i] != 0:								# path[-1] - last element in chain
			if i not in path:										# if element not in chain already and has a connection w\ prev. node -- connect
				newPath = list(path)								# a = b not equal a = copy(b) >_<
				newPath.append(i)

				if len(newPath) == len(matrix[0]):					#
					if matrix[newPath[0]][newPath[-1]] != 0:		# check connection for first and last nodes
						print newPath
						return 1

				fin = deep ( newPath )
				if fin == 1:										# exit if path found
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