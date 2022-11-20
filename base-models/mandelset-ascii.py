# -*- coding: utf-8 -*-

### =======================================================================
### TITLE       : MANDELBROT SET - ASCII EXIBITION
### AUTOR       : MARCUS FARIA
### DATE        : 15.11.2022
###
### DESCRIPTION :
###     Model 1, display of mandelbrot set with ascii table
###
### FOLLOW ME:
###     GITHUB (curr-account) --> https://github.com/mfaria-tech
###     GITHUB (old-account) --> https://github.com/Marcus-Faria
###     LINKEDIN --> https://www.linkedin.com/in/marcus-v-faria-4a2117213/
### =======================================================================


## ========================================================================
##  To decide whether some complex number, c , belongs to the
##  Mandelbrot set, plug that number into the formula:
##
##      zn = z(n-1)^2 +c
##
def formula(c, n_iterations):
    # The first element, z0, is always equal to zero.
    z = 0


    # Generate the first "n" iterations to validate
    # if the sequence belongs to the set
    for _ in range(n_iterations):
        #print(f"z[{_}] = {z}")
        z = z ** 2 + c

    # By definition, considering that the sequence will
    # be greater than four interactions, if the last value
    # of "z" for the iteration is greater than 2, it does
    # not belong to the mandelbrot set.
    return abs(2) <= 2



def c_matrix(xi, yi, xf, yf, d):
    # 'y' axis: referring to the set of imaginary numbers
    # 'x' axis: referring to the set of real numbers
    sx = int((xf - xi) * d) # Total Sample 'x'
    sy = int((yf - yi) * d) # Total Sample 'y'


    matrix = []

    for i in range(sx):
        x = xi + (i * (xf - xi) / (sx - 1))
        
        for j in range(sy):
            # Next Samples
            y = yi + (j * (yf - yi) / (sy - 1))

            matrix.append(x + y*1j)
    
    #print(matrix)
    return matrix



def gen_mandelset():
    density = 100

    c = c_matrix(-2, .5, -1.5, 1.5, density)

    # for i in c:
    #     belongs = formula(c, n_iterations=20)

    #     # Draw Mandelbrot set ASCII
    #     if belongs == True:
    #         print("Ж", end='')
    #     else:
    #         print(".", end='')

    return True


gen_mandelset()
