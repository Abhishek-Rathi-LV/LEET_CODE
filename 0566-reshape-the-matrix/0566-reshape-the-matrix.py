import numpy as np

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
            
        return np.array(mat).reshape(r, c).tolist()
