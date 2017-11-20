# Linear-Alg-tools


Matrix class with various methods useful for studying linear algebra

  ## Methods include:
  

 | method       | parameters            | returns          | notes                      |
 |--------------|-----------------------|------------------|----------------------------|
 |  printMatrix |                       |                  |                            |  
 |  printRow    |                       |                  |                            | 
 |  printCol    |                       |                  |                            | 
 |  getRow      | rownumber(int)        |  array           |                            | 
 |  getCol      | colnumber(int)        |  array           |                            | 
 |  getVal      | col, row(int, int)    |  float           |                            | 
 |  deleteCol   | colnumber(int)        |                  |                            | 
 |  deleteRow   | rownumber(int)        |                  |                            | 
 |  linComb     | vector  (array)       |  array           |   Linear combination       |
 |  swapCol     | colA, colB(int, int)  |                  |                            | 
 |  swapRow     | rowA, rowB(int, int)  |                  |                            | 
 |  mMultedBy   | Matrix                |  Matrix          |   matrix multiplied by     | 
 |  transpose   |                       |  Matrix          |                            | 
 |  ref         |                       |  Matrix          |   row echelon form         | 
 |  rref        |                       |  Matrix          |   reduced row echelon      | 
 |  nulspace    |                       |  Matrix          |   null space basis         | 
 |  colspace    |                       |  Matrix          |   column space basis       | 
 |  getRank     | Matrix                |  int             |   rank of matrix           | 


## note:


- All numbering of columns and rows is zero indexed. 
- [0, 0] is top left. 
- Matricies are initiaized row by row with the upper-most row on the left


## features:

#### obvious assignment from python built-in arrays:


```python
a = Matrix([[1, 3, 0, 2, -1], [0, 0, -1, 4, -3], [0, 0, 0, 0, 0]])
```


#### pretty printing with evenly spaced columnse:


```python
a.printMatrix()
```


```
| 1.0   3.0   0.0   2.0   -1.0 |
| 0.0   0.0   1.0   4.0   -3.0 |
| 0.0   0.0   0.0   0.0   0.0  |
```


#### easly chain methods:


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
  
