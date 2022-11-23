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
##  PSEUDOCODE
##
##  For each pixel (Px, Py) on the screen, do:
##  {
##      x0 = scaled x coordinate of pixel (scaled to lie in the Mandelbrot X scale (-2.5, 1))
##      y0 = scaled y coordinate of pixel (scaled to lie in the Mandelbrot Y scale (-1, 1))
##      x = 0.0
##      y = 0.0
##      iteration = 0
##      max_iteration = 1000
##      while ( x*x + y*y < 2*2  AND  iteration < max_iteration )
##      {
##          xtemp = x*x - y*y + x0
##          y = 2*x*y + y0
##          x = xtemp
##          iteration = iteration + 1
##      }
##      color = palette[iteration]
##      plot(Px, Py, color)
##  }



## ========================================================================
##  To decide whether some complex number, c , belongs to the
##  Mandelbrot set, plug that number into the formula:
##
##      zn = z(n-1)^2 +c
##
def formula( x, y, n_iterations ):
    # The first element, z0, is always equal to zero.
    z = 0

    # Generate the first "n" iterations to validate
    # if the sequence belongs to the set
    interation = 0

    while interation < n_iterations:
        # Relating the pseudocode to c, z and Pc:
        #   z = x + iy
        #   z^2 = x^2 + 2ixy - y^2
        #   c = x0 + iy0
        #
        # pseudocode in the computation of x and y
        #   x = Re(z^2 + c) = x^2 - y^2 + x0
        #   y = Im(z^2 + c) = 2xy + y0
        z = x**2 + y**2

        # By definition, considering that the sequence will
        # be greater than four interactions, if the last value
        # of "z" for the iteration is greater than 2, it does
        # not belong to the mandelbrot set.
        if abs( z ) >= 2 * 2:
            return 0
        
        interation += 1
    
    return 1



def c_matrix(x0, xf, y0, yf, step=0.1, iterations=223):
    # 'y' axis: referring to the set of imaginary numbers
    # 'x' axis: referring to the set of real numbers

    matrix = []

    x = .0
    y = .0

    for i in range( abs( int( ( xf - x0 ) / step ) ) ):
        x = x**2 - y**2 + ( x0  + i * step ) ## current position, set 'x' number
        
        column = []
        for j in range( abs( int( ( yf - y0 ) / step ) ) ): 
            y = 2 * x * y + ( y0  + i * step ) ## current position, set 'y'' number
            print(x)
            print(y)

            # store if the complex number participates in the set
            column.append( formula( x, y, iterations ) )
        
        matrix.append( column )
    
    return matrix



def gen_mandelset():

    c = c_matrix( -2, .5, -1.5, 1.5 )

    # for i in c:
    #     belongs = formula(c, n_iterations=20)

    #     # Draw Mandelbrot set ASCII
    #     if belongs == True:
    #         print("Ж", end='')
    #     else:
    #         print(".", end='')

    return True


gen_mandelset()

