# Exercise 28 Boolean Practice

True and True
False and True
1 == 1 and 2 == 1
"test" == "test"
1 == 1 or 2 != 1
True and 1 == 1
False and 0 != 0
True or 1 == 1
"test" == "testing"
1 != 0 and 2 == 1
"test" != "testing"
"test" == 1
not (True and False)
not (1 == 1 and 0 != 1)
not (10 == 1 or 3 == 4)
not ("testing" == "testing" and "Zed" == "Cool Guy")
1 == 1 and (not ("testing" == 1 or 1 == 0))
"chunky" == "bacon" and (not (3 == 4 or 3 == 3))
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))

# Python interpreter results:

>>> True and True
True
>>> False and True
False
>>> 1 == 1 and 2 == 1
False
>>> "test" == "test"
True
>>> 1 == 1 or 2 != 1
True
>>> True and 1 == 1
True
>>> False and 0 != 0
False
>>> True or 1 == 1
True
>>> "test" == "testing"
False
>>> 1 != 0 and 2 == 1
False
>>> "test" != "testing"
True
>>> "test" == 1
False
>>> not (True and False)
True
>>> not (1 == 1 and 0 != 1)
False
>>> not (10 == 1 or 3 == 4)
True
>>> not ("testing" == "testing" and "Zed" == "Cool Guy")
True
>>> 1 == 1 and (not ("testing" == 1 or 1 == 0))
True
>>> "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
False
>>> 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
False