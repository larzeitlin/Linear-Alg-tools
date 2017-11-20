import copy


class Matrix:
    """ Matrix class with various methods useful for studying linear algebra
    Methods include:
        printMatrix
        printRow
        printCol
        getRow    : params(rownumber) : returns(array)
        getCol    : params(colnumber) : returns(array)
        getVal    : params(col, row)  : returns(float)
        deleteCol : params(colnumber)
        deleteRow : params(rownumber)
        linComb   : params(vector)    : returns(array)   <- Linear combination
        swapCol   : params(colA, colB)
        swapRow   : params(rowA, rowB)
        mMultedBy : params(Matrix)    : returns(Matrix)  <- matrix multiplied by
        transpose :                   : returns(Matrix)
        ref       :                   : returns(Matrix)  <- row echelon form
        rref      :                   : returns(Matrix)  <- reduced row echelon
        nulspace  :                   : returns(Matrix)  <- null space basis
        colspace  :                   : returns(Matrix)  <- column space basis
        getRank   : params(Matrix)    : returns(int)     <- rank of matrix

        """

    def __init__(self, matrix=[]):
        self.matrix = matrix
        self.numRows = len(self.matrix)
        self.numVars = len(self.matrix[0])
        self.maxLengthString = self.calcMaxDig()

    def dotProduct(self, v1, v2):
        """internal convenience method for dot product"""
        assert (len(v1) == len(v2)), "vectors must be same length"
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

    def deleteCol(self, colNum):
        assert colNum < self.numVars, "out of range"
        assert colNum >= 0, "negative column number"
        for i in self.matrix:
            i.pop(colNum)
        self.numVars = len(self.matrix[0])

    def getRow(self, rowNum):
        return(self.matrix[rowNum])

    def getVal(self, col, row):
        return(self.matrix[row][col])

    def deleteRow(self, rowNum):
        assert rowNum < self.numRows, "out of range"
        assert rowNum >= 0, "negative row number"
        self.matrix.pop(rowNum)
        self.numRows = len(self.matrix)

    def linComb(self, vector):
        assert len(vector) == self.numVars, "dimensions mis-match"
        output = []
        for row in self.matrix:
            outRow = 0
            for index, value in enumerate(vector):
                outRow += value * row[index]
            output.append(outRow)
        return(output)

    def matMultedBy(self, matrixB):
        assert self.numVars == matrixB.numRows, "dimensions mis-match"
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

    def findPivots(self):
        """takes a ref or rref matrix to be useful"""
        pivots = []
        for index, row in enumerate(self.matrix):
            cy = index
            cx = 0
            while(self.matrix[cy][cx] == 0):
                cx += 1
                if(cx >= self.numVars):
                    break
            if(cx >= self.numVars):
                break
            pivots.append([cx, cy])
        return(pivots)

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
                mult = -(subpivot/pivot)
                for i in range(cx, output.numVars):
                    output.matrix[step][i] += (mult * output.matrix[cy][i])
            cx += 1
            if(cx >= output.numVars):
                return(output)
        return(output)

    def getRank(self):
        ref = self.ref()
        return(len(ref.findPivots()))

    def refp1s(self):
        """internal convenience function
        for setting all pivots to 1 for an ref"""
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
        return(output)

    def rref(self):
        output = self.refp1s()
        for r in range(output.numRows - 1, 0, -1):
            cx = 0
            cy = r
            emptyRow = False
            while(output.matrix[cy][cx] == 0.0):
                cx += 1
                if(cx >= output.numVars):
                    emptyRow = True
                    break
            if(not emptyRow):
                for s in range(cy - 1, -1, -1):
                    mult = -(output.matrix[s][cx])
                    newrow = [x + (mult * output.matrix[cy][ind])
                              for ind, x in
                              enumerate(output.matrix[s])]
                    output.matrix[s] = newrow
        return(output)

    def nulspace(self):
        rref = self.rref()
        pivots = rref.findPivots()
        numPivots = len(pivots)
        numFree = rref.numVars - numPivots
        pivCols = [i[0] for i in pivots]
        sequence = []
        freeColVecs = []
        for i in range(rref.numVars):
            if i not in pivCols:
                freeColVecs.append(rref.getColumn(i))
        for i in range(rref.numVars):
            sequence.append('P' if i in pivCols else 0)
        output = []
        for i in range(numFree):
            temp = copy.deepcopy(sequence)
            counter = -1
            for j in range(len(temp)):
                if temp[j] == 0:
                    counter += 1
                    if counter == i:
                        temp[j] = 1
                if temp[j] == 'P':
                    temp[j] = -(freeColVecs[i].pop(0))
            output.append(temp)
        return(Matrix(output).transpose())

    def colspace(self):
        ref = self.ref()
        pivotCols = [n[0] for n in ref.findPivots()]
        output = copy.deepcopy(self)
        for i in range(self.numVars - 1, -1, -1):
            if i not in pivotCols:
                output.deleteCol(i)
        return(output)
    
