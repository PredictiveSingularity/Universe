# Define the International System of Units

# import siunits as u

# from universe.dimentions.space import Space
# from universe.dimentions.time import Time

from universe.technologies.mathematics.numbers.complex.real.rational.constants import *

# Define Second, Time
def second(s=ONE):
    unit = ONE
    return unit * s

def minute(m=ONE):
    unit = second(SIXTY)
    return unit * m

def hour(h=1):
    unit = minute(SIXTY)
    return unit * h

def day(d=ONE):
    unit = hour(TWENTY_THREE) + minute(FIFTY + SIX) + second(FOUR)
    return unit * d

def year(y=ONE):
    unit = day(365.2425)
    return unit * y

# Define Meter, Length, distace mesure, Space
def meter(m=ONE):
    unit = ONE
    return unit * m

def kilo_meter(km=ONE):
    unit = meter(THOUSAND)
    return unit * km

def astonomical_unit(au=ONE):
    unit = kilo_meter(149.6 * MILLION)
    return unit * au

def light_year(ly=ONE):
    unit = C
    return unit * ly

# Define Mass
def gram(g=1):
    unit = 1
    return unit * g

def kilo_gram(kg=1):
    unit = gram(1000)
    return unit * kg

