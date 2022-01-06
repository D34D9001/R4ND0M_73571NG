#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: 73RM1N41@9R0GR4M13
"""
import kerri
import math
import sys

##########################
# MATHEMATICAL FUNCTIONS #
##########################

class Math(object):
    """ This class controls mathimatical opperations.
        Most of these opperations use the [math] module.
        This set of functions was added for increased ease
        of use developing and using equations in your programs."""

    pi = math.pi

    euler = math.e

    def __str__(self):
        return """ Controls All Mathimatical Operations Preformed By Kaos """

    def add(self, *args):
        """ Add integers """

        try:
            if len(args) <= 1:
                sys.stderr.write("You Must Insert At Least 2 Integers!")
            else:
                answer = 0
                if len(args) >= 2:
                    for arg in args:
                        answer = float(arg) + float(answer)
                return "%.256f" % float(answer)
        except TypeError:
            raise kerri.InvalidInput(1, "add()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("add()", error)

    def sub(self, *args):
        """ Subtract integers """

        try:
            if len(args) >= 2:
                var_count = int(len(args)) -1
                answer = args[0]
                while int(var_count) >= 1:
                    try:
                        answer = float(answer) - float(args[int(var_count)])
                        var_count -= 1
                    except Exception as error:
                        sys.stderr.write(error)
                return float(answer)
            else:
                print("That Didnt Work")
        except TypeError:
            raise kerri.InvalidInput(1, "sub()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("sub()", error)

    def div(self, *args):
        """ Divide integers """

        try:
            if len(args) >= 2:
                var_count = int(len(args)) -1
                answer = args[0]
                while int(var_count) >= 1:
                    try:
                        answer = float(answer) / float(args[int(var_count)])
                        var_count -= 1
                    except Exception as error:
                        sys.stderr.write(error)
                return "%.32f" % answer
            else:
                sys.stderr.write("You Must Input At Least 2 Integers!")
        except TypeError:
            raise kerri.InvalidInput("div()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("div()", error)

    def rdiv(self, x, y, numb_only=True, *args):
        """ Divide (2) integers and return the answer along with remainder """

        if len(args) >= 1:
            raise kerri.ExcessArguments("rdiv()", 3)
        else:
            pass
        try:
            answer = divmod(x,y)
            if numb_only == False:
                return "%i [Rem: %i]" % (float(answer[0]), float(answer[1]))
            elif numb_only == True:
                a = float(answer[0])
                b = float(answer[1])
                return "%.16f %16f" % (a,b)
            else:
                raise kerri.InvalidInput("rdiv()")
        except TypeError:
            raise kerri.InvalidInput('rdiv()', " All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("rdiv()", error)

    def mult(self, *args):
        """ Multiply intergers """

        try:
            if len(args) >= 2:
                var_count = int(len(args)) -1
                answer = args[0]
                while int(var_count) >= 1:
                    try:
                        answer = float(answer) * float(args[int(var_count)])
                        var_count -= 1
                    except Exception as error:
                        sys.stderr.write(error)
                return "%.32f" % answer
            else:
                sys.stderr.write("You Must Input At Least 2 Integers!")
        except TypeError:
            raise kerri.InvalidInput("mult()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("mult()", error)

    def ceil(self, x, *args):
        """ Return the smallest integral value >= (x) """

        if len(args) >= 1:
            raise kerri.ExcessArguments("ceil()", 1)
        else:
            pass
        try:
            answer = math.ceil(x)
            return answer
        except TypeError:
            raise kerri.InvalidInput("ceil()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("ceil()", error)

    def cos(self, x, *args):
        """ Return cosine of (x) [measured in radians] """

        if len(args) >= 1:
            raise kerri.ExcessArguments("cos()", 1)
        else:
            pass
        try:
            answer = math.cos(x)
            return answer
        except TypeError:
            raise kerri.InvalidInput("cos()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("cos()", error)

    def deg(self, x, *args):
        """ Convert (x) from radians to degrees """

        if len(args) >= 1:
            raise kerri.ExcessArguments("deg()", 1)
        else:
            pass
        try:
            answer = math.degrees(x)
            return answer
        except TypeError:
            raise kerri.InvalidInput("deg()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("deg()", error)

    def rad(self, x, *args):
        """ Convert (x) from degrees to radians """

        if len(args) >= 1:
            raise kerri.ExcessArguments("rad()", 1)
        else:
            pass
        try:
            answer = math.radians(x)
            return answer
        except TypeError:
            raise kerri.InvalidInput("rad()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("rad()", error)

    def exp(self, x, *args):
        """ Returns e raised to the power of (x)"""

        if len(args) >= 1:
            raise kerri.ExcessArguments("exp()", 1)
        else:
            pass
        try:
            answer = math.exp(x)
            return answer
        except TypeError:
            raise kerri.InvalidInput("exp()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("exp()", error)

    def power(self, x, y, z=None, *args):
        """ raise kerri.(x) to power of (y) [to the power of (z)] """

        try:
            if len(args) >= 1:
                raise kerri.ExcessArguments("power()", 3)
            else:
                if z == None:
                    answer = x ** y
                    return answer
                else:
                    answer = x ** y ** z
                    return answer
        except TypeError:
            raise kerri.InvalidInput("power()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("power()", error)

    def floor(self, x, *args):
        """ Return the largets integral value <= (x)."""

        try:
            if len(args) >= 1:
                raise kerri.ExcessArguments("floor()", 1)
            else:
                answer = math.floor(x)
                return answer
        except TypeError:
            raise kerri.InvalidInput("floor()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("floor()", error)

    def hypot(self, x, y, *args):
        """ Return Euclidean distance   [sqrt(x*x+y*y)] """

        try:
            if len(args) >= 1:
                raise kerri.ExcessArguments("hypot()", 2)
            else:
                answer = math.hypot(x, y)
                return answer
        except TypeError:
            raise kerri.InvalidInput("hypot()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("hypot()", error)

    def log(self, x, base=None, *args):
        """ Return the logarithm of (x) to the given base
            If the base is not specified, returns natural
            logarithm (base e) of (x) """

        try:
            if len(args) >= 1:
                raise kerri.ExcessArguments("log()", 1)
            else:
                pass
            if base == None:
                answer = math.log(x)
                return answer
            else:
                answer = math.log(x, base)
                return answer
        except TypeError:
            raise kerri.InvalidInput("log()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("log()", error)

    def pow(self, x, y, z=None, *args):
        """ With (2) arguments, equivalent to (x**y)
            With (3) arguments, equivalent to (x**y)%z but may be
            more efficient (e.g.  for longs) """

        try:
            if len(args) >= 1:
                raise kerri.ExcessArguments("pow()", 3)
            else:
                if z == None:
                    answer = pow(x, y)
                    return answer
                else:
                    answer = pow(x, y, z)
                    return answer
        except TypeError:
            raise kerri.InvalidInput("pow()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("pow()", error)

    def sin(self, x, *args):
        """ Return the sine of (x) [measured in radians] """

        try:
            if len(args) >= 1:
                raise kerri.ExcessArguments("", )
            else:
                answer = math.sin(x)
                return answer
        except TypeError:
            raise kerri.InvalidInput("sin()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("sin()", error)

    def sqrt(self, x, *args):
        """ Return the positive square root of (x) """

        try:
            if len(args) >= 1:
                raise kerri.ExcessArguments("", )
            else:
                try:
                    answer = math.sqrt(x)
                    return answer
                except ValueError:
                    sys.stderr.write("[4] [ERROR]: sqrt() only accepts positive integers.")
        except TypeError:
            raise kerri.InvalidInput("sqrt()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("sqrt()", error)

    def tan(self, x, *args):
        """ Return the tangent of (x) [measured in radians] """

        try:
            if len(args) >= 1:
                raise kerri.ExcessArguments("tan()", x)
            else:
                answer = math.tan(x)
                return answer
        except TypeError:
            raise kerri.InvalidInput("tan()", "All variables must be integers!")
        except Exception as error:
            raise kerri.Unknown("tan()", error)

#########
# INITs #
#########

kmath = Math()
add = kmath.add
ceil = kmath.ceil
cos = kmath.cos
deg = kmath.deg
div = kmath.div
exp = kmath.exp
floor = kmath.floor
hypot = kmath.hypot
log = kmath.log
mult = kmath.mult
pow = kmath.pow
power = kmath.power
rad = kmath.rad
rdiv = kmath.rdiv
sin = kmath.sin
sqrt = kmath.sqrt
sub = kmath.sub
tan = kmath.tan

#############
# Constants #
#############

e = kmath.euler
pi = kmath.pi
