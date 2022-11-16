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
    return abs(z) <= 2



def c_matrix(x0, y0, x, y):
    return


def get_members(c, n_iterations):
    mask = formula(c, n_iterations)
    return c[mask]


members = get_members(-1, n_iterations=10)
print(members)
print(formula(-1, n_iterations=10))

#"Ж"
