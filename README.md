<!--
    TITLE       : README.md
    AUTOR       : MARCUS FARIA
    DATE        : 03.10.2022
 -->

**Desenhando Conjunto de Mandelbrot em Python**
===

<div align="center">

![Fractal Mandelbrot Set, low density][img-fractal-low-density]

</div><br />

## **Algoritmo Base Simples**

<br /><div align="center">

O algoritmo mais simples para gerar uma representação do _conjunto de Mandelbrot_ é conhecido como algoritmo de "tempo de fuga" (Escape Time). 

</div><br />

Para o _Escape Time Algorthm_, montado em `base-models/mandelset-ascii.py`, um cálculo repetido é executado para cada ponto _X_, _Y_ na área de plotagem e, com base no resultado destes pontos, um identificador é adicionado a este ponto. O resultado de cada iteração é usado como valores iniciais para a validação do próximo ponto.

Cada ponto representa a interseção de um número real ($x$) à um número imaginário ($y$), isto é, um número no plano dos complexos ($c$). A sucessão de pontos no plano complexo pertencente ao Conjunto de Mandelbrot é definido na seguinte formula matemática:

$$z_n = z_{n-1}^2 - c$$

Para este cálculo, $z_0$ sempre será $0$. 

<br />

### **Tempo de Escape**

<br />

O número de iterações neste cálculo _tende ao infinito_, com isso, para determinar se um valor, número complexo, pertence ao conjunto de Mandelbrot é verificado seu tempo de escape.

Na tabela a seguir são exemplificados alguns valores para $c$ e suas respectivas sequências:


<div align="center">

 iteração | c = 1 | c = -1 | c = 0
----------|-------|--------|---------
 [ 0 ]    | 0     | 0      | 0
 [ 1 ]    | 1     | -1     | 0
 [ 2 ]    | 2     | 0      | 0
 [ 3 ]    | 5     | -1     | 0
 [ 0 ]    | 26    | 0      | 0
 [ ∞ ]    | ...   | ...    | ...

</div>

Como é possível perceber, o valor $c=1$ possui um _crescimento que tende ao infinito_, por está razão este valor não participa do conjunto de Mandelbrot, já os valores $c=-1$ e $c=0$ a um _escape_ no crescimento logo no início da iteração, sendo assim, este valor pertence ao conjunto de Mandelbrot.


<br /><br />


## **REFERÊNCIAS**

> O PROGRAMADOR, [Um programa que Desenha o Infinito][link-oprogramador] <br/>
> REAL PYTHON, [Draw the Mandelbrot Set in Python][link-realpython] <br/>
> EN-WIKIPEDIA [Mandelbrot Set][link-wiki1] <br/>
> EN-WIKIPEDIA [Ploting algorithms for the Mandebrot set][link-wiki2]



<!-- LOCAL VARIABLES -->
[link-oprogramador]: https://github.com/oprogramadorreal/Mandelbrot
[link-realpython]: https://realpython.com/mandelbrot-set-python/
[link-wiki1]: https://en.wikipedia.org/wiki/Mandelbrot_set
[link-wiki2]: https://en.wikipedia.org/wiki/Plotting_algorithms_for_the_Mandelbrot_set

[img-fractal-low-density]: img/fractal_low_density.png
