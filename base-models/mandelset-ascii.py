# -*- coding: utf-8 -*-

### =======================================================================
### TITLE       : MANDELBROT SET - ASCII EXIBITION
### AUTOR       : MARCUS FARIA
### DATE        : 20.11.2022
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
##  PSEUDOCODE - ESCAPE TIME ALGORITHM
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


## ========================================================================
##  To decide whether some complex number, c , belongs to the
##  Mandelbrot set, plug that number into the formula:
##
##      zn = z(n-1)^2 +c
##
mang = lambda a, b: a*a + b*b

#def mandset():
