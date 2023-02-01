from utils import *


class Simplex:
    def __init__(self, A, B, C):
        self.unbounded = False
        self.rows = len(A)
        self.cols = len(A[0])
        self.a = A
        self.b = B
        self.c = C

    def printMatrix2D(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.a[i][j], end=" ")
            print()

    def getColByIndex(self, index):
        col = []
        for i in range(self.rows):
            col.append(self.a[i][index])
        return col

    def getRowByIndex(self, index):
        row = []
        for i in range(self.cols):
            row.append(self.a[index][i])
        return row

    def calBasicColumn(self):
        basicIndexCol = [None for i in range(self.cols)]
        for i in range(self.cols):
            col = self.getColByIndex(i)
            indexIdentity = isIdentityCol(col)
            if indexIdentity >= 0:
                basicIndexCol[indexIdentity] = i
        basicCol = []
        for i in basicIndexCol:
            if i is not None:
                basicCol.append(self.c[i])
        return basicCol

    def calextremeRow(self, basicCol):
        extremeSol = []
        for i in range(self.cols):
            extremeValue = 0
            col = self.getColByIndex(i)
            for j in range(self.rows):
                extremeValue += col[j] * basicCol[j]
            extremeValue -= self.c[i]
            extremeSol.append(extremeValue)
        return extremeSol

    def optimized(self, extremeRow):
        isOptimized = True
        for i in extremeRow:
            if i > 0:
                return False
        return isOptimized

    def getPivotRow(self, pivotCol):
        ratioLst = [-1 for i in range(self.rows)]  # -1 is not invalid
        for i in range(self.rows):
            if pivotCol[i] > 0:
                ratioLst[i] = self.b[i] / pivotCol[i]
        pivotElement = ratioLst.index(min(filter(lambda x: x > 0, ratioLst)))
        return [self.getRowByIndex(pivotElement), pivotElement]

    def getPivotCol(self, extremeRow):
        # Get value max of extreme column
        maxValue = max(extremeRow)
        countMax = extremeRow.count(maxValue)
        if countMax == 1:
            colIndex = extremeRow.index(maxValue)
            col = self.getColByIndex(colIndex)
            if isUnboundedCol(col):
                self.unbounded = True
                return None
            else:
                return [col, colIndex]
        else:
            countMaxList = [idx for idx, value in enumerate(
                extremeRow) if value == maxValue]
            for idx, value in enumerate(countMaxList):
                col = self.getColByIndex(value)
                if isUnboundedCol(col):
                    if idx < len(countMaxList) - 1:
                        continue
                    else:
                        self.unbounded = True
                        return None
                else:
                    return [col, value]

    def calOptimalValue(self, basicCol):
        optimalValue = 0
        for i in range(self.rows):
            optimalValue += basicCol[i] * self.b[i]
        return optimalValue

    def genOptimalSol(self):
        optimalSol = [0 for i in range(self.cols)]
        for i in range(self.cols):
            _col = self.getColByIndex(i)
            idxIdentity = isIdentityCol(_col)
            if idxIdentity >= 0:
                optimalSol[i] = self.b[idxIdentity]
        return optimalSol

    def calSimplexAlgo(self):
        # Finding the basic variable -> basic column
        basicCol = self.calBasicColumn()
        extremeRow = self.calextremeRow(basicCol)
    
        if self.optimized(extremeRow):
            print("Optimal solution: ", self.genOptimalSol())
            print("Optimal Value", self.calOptimalValue(basicCol))
            return True
        # Get pivot column
        [pivotCol, pivotColIndex] = self.getPivotCol(extremeRow)
        if pivotCol is None and self.unbounded:
            print("Unbounded")
            return True
        [pivotRow, pivotRowIndex] = self.getPivotRow(pivotCol)
        pivotValue = self.a[pivotRowIndex][pivotColIndex]
        normalizePivotRow = [i / pivotValue for i in pivotRow]
        self.b[pivotRowIndex] /= pivotValue
        for i in range(self.rows):
            if i != pivotRowIndex:
                for j in range(self.cols):
                    self.a[i][j] -= (pivotCol[i] * normalizePivotRow[j])
        for i in range(self.rows):
            if i != pivotRowIndex:
                self.b[i] -= (pivotCol[i] * self.b[pivotRowIndex])
        for i in range(self.cols):
            self.a[pivotRowIndex][i] = normalizePivotRow[i]
        self.printMatrix2D()
        print("Extreme Row:", extremeRow)
        print("Extreme Solution:", self.b)
        print()
        return False

    def simplex(self):
        try:
            result = False
            while result is False:
                result = self.calSimplexAlgo()
        except:
            print("Unbounded")
