# Linear-Alg-tools


   Matrix class with various methods useful for linear algebra

  ## Methods include:

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
	   nulspace  :                   : returns(Matrix)  <- Null-space basis



 ## features:

obvious assignment from python built-in arrays:


```python
a = Matrix([[1, 3, 0, 2, -1], [0, 0, -1, 4, -3], [0, 0, 0, 0, 0]])
```


pretty printing with evenly spaced columns. for example:


```python
a.printMatrix()
```


```
| 1.0   3.0   0.0   2.0   -1.0 |
| 0.0   0.0   1.0   4.0   -3.0 |
| 0.0   0.0   0.0   0.0   0.0  |
```


easly chain methods:


```python
a.transpose().printMatrix()
```


```
| 1.0   0.0   0.0  |
| 3.0   0.0   0.0  |
| 0.0   -1.0  0.0  |
| 2.0   4.0   0.0  |
| -1.0  -3.0  0.0  |
```


 ## To Do:
- column space
- row space
- left null
- ax = b
- cython optimise
- verbose methods
	
