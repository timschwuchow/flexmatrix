'''
Created on Jun 26, 2016

@author: tim
'''

import numpy as np 
import sympy as sy 

class FlexMatrix:
    '''
    Matrix that contains both numpy and sympy forms 
    '''
    def __init__(self,m=None):
        '''
        Constructor 
        '''
        
        self.orig = m 
        if type(m) is list:
            self.i = len(m)
            self.j = len(m[0])
        else:
            self.i = m.shape[0]
            self.j = m.shape[1]
        self.np = np.matrix(m)
        self.sy = sy.Matrix(m)
        self.li = self.np.tolist() 
    
    def transpose(self):
        '''
        Return transposed flexmatrix 
        '''
        return FlexMatrix(self.np.T)
    def substitute(self,subdict):
        return FlexMatrix(self.sy.subs(subdict))
        