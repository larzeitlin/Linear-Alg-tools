# Linear-Alg-tools


Matrix class with various methods useful for studying linear algebra. Of course there are more optimal libs out there, this is just me learning by doing...

  ## Methods include:
  
  | method      | parameters           | returns | note                 |
  |-------------|----------------------|---------|----------------------|
  | printMatrix |                      |         | pretty print         |
  | printRow    |                      |         | pretty print         |
  | printCol    |                      |         | pretty print         |
  | getRow      | row(int)             | array   | 0-indexed            |
  | getCol      | col(int)             | array   | 0-indexed            |
  | getVal      | col, row(int, int)   | float   | 0-indexed            |
  | deleteCol   | col(int)             |         | 0-indexed            |
  | deleteRow   | row(int)             |         | 0-indexed            |
  | linComb     | vector  (array)      | array   | Linear combination   |
  | swapCol     | colA, colB(int, int) |         | 0-indexed            |
  | swapRow     | rowA, rowB(int, int) |         | 0-indexed            |
  | mMultedBy   | Matrix               | Matrix  | matrix multiplied by |
  | transpose   |                      | Matrix  |                      |
  | ref         |                      | Matrix  | row echelon form     |
  | rref        |                      | Matrix  | reduced row echelon  |
  | nulspace    |                      | Matrix  | null space basis     |
  | colspace    |                      | Matrix  | column space basis   |
  | rowspace    |                      | Matrix  | row space basis      |
  | leftnul     |                      | Matrix  | leftnull space basis |
  | getRank     | Matrix               | int     | rank of matrix       |


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
