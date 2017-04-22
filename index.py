#Python 3.0
import re
import os
import collections
import time
import numpy as np
from scipy.linalg import eig

class pagerank:

    def pagerank(self, input_file, teleportation_rate = 0.15):
    #function to implement pagerank algorithm
    #input_file - input file that follows the format provided in the assignment description
        file = open(input_file, "r")
        fileContents = file.read().split("\n")
        file.close()

        # Get # of pages / links
        numbPages = int(fileContents[0].replace(" ",""))
        numbLinks = int(fileContents[1].replace(" ",""))

        # Create empty adjacency matrix
        matrix = [[0 for x in range(numbPages)] for y in range(numbPages)]

        # Read links to matrix
        for x in fileContents[2:]:
            y = x.split()
            if len(y) == 2:
                source = int(y[0])
                dest = int(y[1])

                matrix[source][dest] += 1

        # Matrix -> probability matrix
        for i in range(0,len(matrix)):
            row_total = float(sum(matrix[i]))

        # Modifying matrix to
        for i in range(0,len(matrix)):
            row_total = sum(matrix[i])
            #if row_total == 0:
            #    for j in range(0,len(matrix[i])):
            #        matrix[i][j] = (1 - teleportation_rate)*(1.0/float(numbPages)) + teleportation_rate/float(numbPages)
            #else:
            for j in range(0,len(matrix[0])):
                matrix[i][j] = (1.0 - teleportation_rate)*float(matrix[i][j]/row_total) + teleportation_rate/float(numbPages)

        # Get initial matrix P
        P = np.full((numbPages, 1), 1.0/float(numbPages))
        P = np.matrix(P)

        # Get left hand eigenvector of transition probability matrix as A
        w, vl, vr = eig(np.matrix(matrix), left=True)
        A = vl

        A = np.matrix(matrix).transpose()

        i = 0
        while i < 100:
            P = A*P
            i+=1

        # Sort the final result by page rank and get top ten results
        final = list(zip(list(map(lambda x: round(x[0],3), P.tolist())),range(0,numbPages)))
        final.sort(reverse=True, key=lambda x: x[0])
        final = final[:10]


        for i,x in enumerate(final):
            print(str(i)+".","Doc Number", x[1]," -  Rank:", x[0], "")






pr = pagerank()
pr.pagerank("test3.txt")
