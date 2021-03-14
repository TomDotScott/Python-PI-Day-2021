# Pi day 2021 - Generating PI from random numbers
For PI-Day this year, I wanted to take a crack at estimating PI with PI-thon (sorry). Rather effective, this method uses randomly generated number pairs and checks their gcd. this method is ~99.88% accurate!

To do this, I am using the fact that the probability of two numbers being co-prime is 6 over Pi squared:

![Equation](showcase/latex.gif "Equation")


My thought process was as follows: 

![My scribbles](showcase/method.jpg "My scribbles!")

<i>The Euclidean Algorithm <a href = "https://mathworld.wolfram.com/EuclideanAlgorithm.html">was researched here</a></i>

The result is ~99.88677510815323 % accurate!
