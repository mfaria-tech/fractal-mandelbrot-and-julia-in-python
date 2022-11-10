# -*- coding: utf-8 -*-

### ===============================================
### TITLE       : MANDELBROT SET
### AUTOR       : MARCUS FARIA
### DATE        : 03.11.2022
###
### ===============================================


import numpy as np
#import matplotlib as plt


class MandelbrotSet:
    def __init__(self, max_iterations: int):
        """
        A loader-like context manager
        
        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.max_iterations: int

    def stability(self, c: complex) -> float:
        return self.escape_count(c) / self.max_iterations
    
    def escape_count(self, c: complex) -> int:
        z = 0

        for i in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > 2:
                return i
        
        return self.max_iterations
