import copy


class Matrix:
    """ Matrix class with various methods useful for linear algebra
    Methods include:
        printMatrix
        printRow
        printCol
        getRow    : params(rownumber) : returns(array)
        getCol    : params(colnumber) : returns(array)
        linComb   : params(vector)    : returns(array)  <- Linear combination
        swapCol   : params(colA, colB)
        swapRow   : params(rowA, rowB)
        mMultedBy : params(Matrix)    : returns(Matrix)  <- matrix multiplied by
        transpose :                   : returns(Matrix)
        ref       :                   : returns(Matrix)  <- row echelon form
        rref      :                   : returns(Matrix)  <- reduced row echelon

        """

    def __init__(self, matrix=[]):
        self.matrix = matrix
        self.numRows = len(self.matrix)
        self.numVars = len(self.matrix[0])
        self.maxLengthString = self.calcMaxDig()

    def dotProduct(self, v1, v2):
        """internal convenience method for dot product"""
        if(len(v1) != len(v2)):
            print("can't dot product, vectors don't match")
            return
        output = 0
        for i in range(len(v1)):
            output += v1[i]*v2[i]
        return(output)

    def calcMaxDig(self):
        """internal convenience method to help format printing.
        calculated max width of column"""
        curMax = 0
        for i in range(self.numRows):
            self.matrix[i] = [float(x) for x in self.matrix[i]]
            slrow = [len(str(round(x, 3))) for x in self.matrix[i]]
            rowMax = max(slrow)
            curMax = (curMax if curMax > rowMax else rowMax)
        return(curMax)

    def printMatrix(self):
        self.maxLengthString = self.calcMaxDig()
        print("")
        for i in range(self.numRows):
            printrow = "|"
            for j in range(self.numVars):
                printrow += " {:^{width}} ".format(round(self.matrix[i][j], 3),
                                                   width=self.maxLengthString)
            printrow += "|"
            print(printrow)
        print("")

    def printRow(self, rowNum):
        print("")
        printRow = "|"
        for j in range(self.numVars):
            printRow += " {:^{width}} ".format(self.matrix[rowNum][j],
                                               width=self.maxLengthString)
        printRow += "|"
        print(printRow)

    def printCol(self, colNum):
        for i in range(self.numVars):
            print("| {:^{width}} |".format(self.matrix[i][colNum],
                                           width=self.maxLengthString))

    def getColumn(self, colNum):
        column = []
        for i in range(self.numRows):
            column.append(self.matrix[i][colNum])
        return(column)

    def getRow(self, rowNum):
        return(self.matrix[rowNum])

    def linComb(self, vector):
        if(len(vector) != self.numVars):
            print("vector doesn't match number of columns in Matrix")
            return
        output = []
        for row in self.matrix:
            outRow = 0
            for index, value in enumerate(vector):
                outRow += value * row[index]
            output.append(outRow)
        return(output)

    def matMultedBy(self, matrixB):
        if(self.numVars != matrixB.numRows):
            print("these vectors cannot be multiplied")
            return
        prodNumRows = self.numRows
        prodNumVars = matrixB.numVars
        output = []
        for i in range(prodNumRows):
            row = []
            for j in range(prodNumVars):
                row.append(self.dotProduct(self.getRow(i),
                                           matrixB.getColumn(j)))
            output.append(row)
        return(Matrix(output))

    def swapCols(self, a, b):
        for row in self.matrix:
            row[a], row[b] = row[b], row[a]

    def swapRows(self, a, b):
        self.matrix[a], self.matrix[b] = self.matrix[b], self.matrix[a]

    def transpose(self):
        output = []
        for n in range(self.numVars):
            col = self.getColumn(n)
            output.append(col)
        return(Matrix(output))

    def ref(self):
        cx = 0
        cy = 0
        output = copy.deepcopy(self)
        for n in range(output.numRows - 1):
            cy = n
            while(output.matrix[cy][cx] == 0):
                cy += 1
                if(cy >= output.numRows):
                    cy = n
                    cx += 1
                    if(cx >= output.numVars):
                        return(output)
                if(output.matrix[cy][cx] != 0):
                    output.swapRows(n, cy)
                    cy = n
            pivot = output.matrix[cy][cx]
            for step in range(cy + 1, output.numRows):
                subpivot = output.matrix[step][cx]
                operator = -(subpivot/pivot)
                for i in range(cx, output.numVars):
                    output.matrix[step][i] += (operator * output.matrix[cy][i])
            cx += 1
            if(cx >= output.numVars):
                return(output)
        return(output)

    def rref(self):
        output = self.ref()
        cx = 0
        cy = 0
        for index, row in enumerate(output.matrix):
            cy = index
            while(output.matrix[cy][cx] == 0.0):
                cx += 1
                if(cx >= output.numVars):
                    return(output)
            pivot = output.matrix[cy][cx]
            newrow = [i/pivot for i in row]
            output.matrix[index] = newrow
            output.printMatrix()
        for r in range(self.numRows - 1, 0, -1):
            cx = 0
            cy = r
            if(cx < output.numVars):
                while(output.matrix[cy][cx] == 0.0):
                    cx += 1
            if(cx >= output.numVars):
                break
            for s in range(cy - 1, -1, -1):
                operator = -(output.matrix[s][cx])
                newrow = [x + (operator * output.matrix[cy][ind])
                          for ind, x in
                          enumerate(output.matrix[s])]
                output.matrix[s] = newrow
                output.printMatrix()
        return(output)
