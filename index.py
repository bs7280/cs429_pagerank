#Python 3.0
import re
import os
import collections
import time
#import other modules as needed

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

        print("Raw Probability Matrix")
        print(matrix)

        # Modifying matrix to
        for i in range(0,len(matrix)):
            row_total = sum(matrix[i])
            if row_total == 0:
                for j in range(0,len(matrix[i])):
                    matrix[i][j] = 1.0/float(numbPages)
            else:
                for j in range(0,len(matrix[0])):
                    matrix[i][j] = (1 - teleportation_rate)*float(matrix[i][j]/row_total) + teleportation_rate/float(numbPages)

        # Testing
        for i in range(0,len(matrix)):
            #print(matrix[i])
            assert(abs(sum(matrix[i]) - 1) < 0.001)


        print(matrix)




pr = pagerank()
pr.pagerank("test1.txt")
