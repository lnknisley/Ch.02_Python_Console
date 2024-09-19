'''
2.0 Jedi Training (20pts)  Name: Logan Knisley

1.) How do you enter a single line comment in a program? Give an example. (2pt)
You use a hashtag in order to have a single line comment (Ex: self.world_pull = 9.80 #this sets the global gravity)

2.) If a=2 and b=5, predict all of the following below and record your predictions. (9pts)
Then in the Python Console window, enter a=2 and b=5 and then all of the following and record the actual output.
If the output is an error record the error and try to determine what the error is!
Comment about any of your predictions that didn't match the actual output

input               = output (prediction)

b//a                = 2.0 (2, I didn't expect the float)
b/a                 = 2.5 (2.5)
b**a                = 25 (25)
b%a                 = 1 (1)
a+B                 = error, undefined variable (error, undefined variable)
type(42)            = class 'int' (42, I thought this was a deprecated print function. Data types passed through my mind when doing this.)
type(42.0)          = class 'float' 42.0 (42.0, same as above)
type("C3PO")        = class 'str' (C3PO, same as above)
type(True)          = class 'bool' (True, same as above)


3.) Predict what would be the final output of (a) and type(a) if you enter the following 5 lines        (3pts)
into the Python Console Window? Then actually do it and record the output and comment on differences
between your predictions and the output.

a=2
a*=10
a/=2
a+=12
a-=7
a             = 15.0 (15, I didn't expect the float)
type(a)       = class 'float' (class 'int', same as above)


4.) What is the mistake in the following code? Comment it and fix it!  (3pt)

x,y = (4,5)
a = 3 * (x + y)
a
# The mistake is applying math syntax to programming syntax, assuming that a number before parentheses multiplies it. This can be fixed by adding the multiplication operator.

5.) What is the mistake in the following code so it will calculate the average? Comment it and fix it!  (3pt)

x,y,z = (3,4,5)
ave = (x+y+z)/3
ave
# The mistake is fundamentally misunderstanding the order of operations, with only z being divided. This can be fixed by adding parentheses around x, y, and z.

'''
