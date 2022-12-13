"""python -m pydoc Fraction"""
import math
from builtins import print, property, str, range, ValueError, isinstance, float, TypeError, int, abs
from math import gcd, floor


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : November 2020
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num doit etre un entier et den doit etre un entier non null 0
        POST : num et den sont initialises et peuvent etre utilises. Si le den est négatif,
        renvoie sa forme absolu et transforme le num en négatif.
        RAISES : renvoie code error ZeroDivisionError si den = 0
                                    ValueError si num, den égal à +- Infinity
                                    TypeError si num ou den ne sont pas des entiers
        """
        self.pgcd = None
        self.fr = None
        self.compteur = 0
        self.interim = 0
        self.interim_float = 0
        self._numerator = num
        self._denominator = den
        if self._denominator == 0:
            raise ZeroDivisionError("den doit etre different de 0")
        elif self._denominator == math.inf or self._numerator == math.inf:
            raise ValueError("valeur trop extrême")
        elif self._denominator == -math.inf or self._numerator == -math.inf:
            raise ValueError("valeur trop extrême")
        elif isinstance(self._denominator, float):
            raise TypeError("den n'est pas un entier")
        if isinstance(self._numerator, float):
            raise TypeError("num n'est pas un entier")
        self.fr = self._numerator / self._denominator
        if self._denominator < 0:
            self._denominator = abs(self._denominator)
            self._numerator = -abs(self._numerator)

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    # ------------------ Textual representations ------------------
    def trouver_pgcd(self, _numerator, _denominator):
        if self._denominator == 0:
            raise ValueError("le denominateur ne peut etre egal a 0")
        if self._numerator > self._denominator:
            petit = self._denominator
        else:
            petit = self._numerator
        for i in range(1, abs(petit) + 1):
            if (self._numerator % i == 0) and (self._denominator % i == 0):
                self.pgcd = i
        return self.pgcd

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : utilise num et den si initialise correctement, doit pouvoir calculer le pgcd en appeleant une fonction
        POST : return la forme silpmifiee au max de la fraction
        """
        if self._numerator == 0:
            print(0)
        else:
            d = self.trouver_pgcd(self._numerator, self._denominator)

            self._numerator = self._numerator // d
            self._denominator = self._denominator // d

            if self._denominator == 1:
                print(str(self._numerator))

            elif self._denominator != 1:
                print(str(self._numerator) + "/" + str(self._denominator))

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : doit utiliser une fonction pour trouver le pgcd et den, num initialises correctement
        POST : return la valeur simplifie de la fraction sous forme d'un entier et du reste sous forme de fraction
        """
        if self._numerator == 0:
            print(0)
        else:
            d = self.trouver_pgcd(self._numerator, self._denominator)

            self._numerator = self._numerator // d
            self._denominator = self._denominator // d
            self.interim = abs(self._numerator)

            while self.interim > self._denominator:
                self.interim = self.interim - self._denominator
                self.compteur += 1
            if self.compteur == 0 and self._numerator > 0 and self._denominator != 1:
                print(str(self.interim) + "/" + str(self._denominator))
            elif self.compteur == 0 and self._numerator < 0 and self._denominator != 1:
                print("-" + str(self.interim) + "/" + str(self._denominator))
            elif self._denominator == 1 and self._numerator > 0 and self.compteur != 0:
                print(self._numerator / self._denominator)
            elif self._denominator == 1 and self._numerator < 0 and self.compteur != 0:
                print(self._numerator / self._denominator)
            elif self.compteur != 0 and self._denominator != 1 and self._numerator > 0:
                print(str(self.compteur) + " " + str(self.interim) + "/" + str(self._denominator))
            elif self.compteur != 0 and self._denominator != 1 and self._numerator < 0:
                print("-" + str(self.compteur) + " " + str(self.interim) + "/" + str(self._denominator))

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other n'est pas un string
         POST : return la somme entre la fraction et other
         RAISE : TypeError si other est different de int et float
         RAISE : ValueError si other est egal a +- infinity
         """
        if self._denominator == math.inf or self._numerator == math.inf:
            raise ValueError("valeur trop extrême")
        elif self._denominator == -math.inf or self._numerator == -math.inf:
            raise ValueError("valeur trop extrême")
        self.fr = self.fr + other
        print(self.fr)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other n'est pas un string
        POST : return la diff entre la fraction et other
        RAISE : TypeError si other est different de int et float
        RAISE : ValueError si other est egal a +- infinity
        """
        if self._denominator == math.inf or self._numerator == math.inf:
            raise ValueError("valeur trop extrême")
        elif self._denominator == -math.inf or self._numerator == -math.inf:
            raise ValueError("valeur trop extrême")
        self.fr = self.fr - other
        print(self.fr)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other n'est pas un string
        POST : return la multiplication entre la fraction et other soit un int, soit un float
        RAISE : TypeError si other est different de int et float
        RAISE : ValueError si other est egal a +- infinity
        """
        if self._denominator == math.inf or self._numerator == math.inf:
            raise ValueError("valeur trop extrême")
        elif self._denominator == -math.inf or self._numerator == -math.inf:
            raise ValueError("valeur trop extrême")
        self.fr = self.fr * other
        print(self.fr)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other n'est pas un string ni egal a 0
        POST : return la division entre la fraction et other, soit un int soit un float
        RAISE : TypeError si other est different de int et float
        RAISE : ValueError si other est egal a +- infinity
        RAISE : ZeroDivisionError si other est egal a 0
        """

        if self._denominator == math.inf or self._numerator == math.inf:
            raise ValueError("valeur trop extrême")
        elif self._denominator == -math.inf or self._numerator == -math.inf:
            raise ValueError("valeur trop extrême")
        try:
            self.fr = self.fr / other
        except ZeroDivisionError:
            print("on ne divise pas par 0")
        else:
            print(self.fr)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other n'est pas un string
        POST : return la fraction puissance other sous forme de float
        RAISE : TypeError si other est different de int et float
        RAISE : ValueError si other est egal a +- infinity
        """
        if self._denominator == math.inf or self._numerator == math.inf:
            raise ValueError("valeur trop extrême")
        elif self._denominator == -math.inf or self._numerator == -math.inf:
            raise ValueError("valeur trop extrême")
        self.fr = self.fr ** other
        print(self.fr)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other n'est pas un string
        POST : return True si la fraction est egal a other
        RAISE : TypeError si other est different de int et float
        RAISE : ValueError si other est egal a +- infinity

        """
        if other == 0 or self.fr == 0:
            raise ValueError("valeur impossible transmise")
        if self.fr == other:
            print("c'est egal")
        elif self.fr == 0:
            print("not possible")
        else:
            print("pas egal")

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : recoit un float
        POST : return la partie decimale d'une fraction
        RAISE : TypeError si la fraction est un entier
        """
        if self.fr > 0:
            self.interim_float = self.fr - floor(self.fr)
            print(self.interim_float)
        elif self.fr < 0:
            self.interim_float = self.fr + round(self.fr)
            print(self.interim_float)

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : recoit un int ou float en fonction des precedentes operations
        POST : return true si la fraction egal 0
        """
        if self.fr == 0:
            print("egal 0")
        else:
            print("diff de 0")

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : a tester sur une instance de la classe Fraction
        POST : return true si la valeur teste est un int, false si c'est un float
        RAISE : ValueError si la fraction est egal a 0
        """
        if isinstance(self.fr, int):
            print("int")
        else:
            print("pas int")

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : a tester sur une instance de la classe Fraction
        POST : return true si la valeur teste est plus petite que 1
        RAISE : ValueError si la fraction est egal a 0
        """
        if abs(self.fr) < 1:
            print("<1")
        else:
            print(">1")

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : a tester sur une instance de la classe Fraction
        POST : return true si le numerateur de la fraction simplifie est 1
        RAISE : ValueError si la fraction est egal a 0
        """
        d = gcd(self._numerator, self._denominator)

        self._numerator = self._numerator // d
        if self._numerator == 1:
            print("oui")
        else:
            print("non")

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : a tester sur une instance de la classe Fraction
        POST : return true si condition remplie, false dans le cas contraire
        RAISE : ValueError si other est egal a 0 ou si la fraction recue egale 0
        """
        if other == 0 or self.fr == 0:
            raise ValueError("valeur impossible transmise")
        for i in range(1000):
            i = + 1
            if (abs(self.fr) - abs(other)) == 1 / i:
                print("adj")

    @numerator.setter
    def numerator(self, value):
        self._numerator = value

    @denominator.setter
    def denominator(self, value):
        self._denominator = value


if __name__ == "__main__":
    a = Fraction(8, -4)
    a.__str__()
    a.as_mixed_number()
    b = Fraction(2, 6)
    b.__str__()
    b.as_mixed_number()
    c = Fraction(-27, 4)
    c.__str__()
    c.as_mixed_number()
    d = Fraction(0, 4)
    d.__str__()
    d.as_mixed_number()
    print()
    a.__add__(4/5)
    b.__add__(-4/5)
    c.__add__(-4/5)
    d.__add__(4/5)
    print()
    a.__sub__(8/7)
    b.__sub__(-8/7)
    c.__sub__(8/7)
    d.__sub__(8/7)
    print()
    a.__mul__(3/8)
    b.__mul__(0)
    c.__mul__(-6)
    d.__mul__(2)
    print()
    a.__truediv__(7)
    b.__truediv__(3/6)
    c.__truediv__(0)
    d.__truediv__(-3)
    print()
    a.__float__()
    b.__float__()
    c.__float__()
    d.__float__()
    print()
    a.is_zero()
    b.is_zero()
    c.is_zero()
    d.is_zero()
    print()
    a.is_proper()
    b.is_proper()
    c.is_proper()
    d.is_proper()
    print()
    a.is_integer()
    b.is_integer()
    c.is_integer()
    d.is_integer()
    j = Fraction(math.inf, 4)
    j.__str__()