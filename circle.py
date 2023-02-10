# The circle module has functions that perform
# calculations related to circles.
#Use math.pi in calculations
import math

circleWhole = math.pi


# The area function accepts a circle's radius as an
# argument and returns the area of the circle.
def calcAreaOfCircleforRadius(radius):
    areaOfCircleResult = circleWhole * radius ** 2

    return areaOfCircleResult


# The circumference function accepts a circle's
# radius and returns the circle's circumference.
def calcCircumference(radius):
    areaOfCircleResultCircumferenceResult = 2 * circleWhole * radius

    return areaOfCircleResultCircumferenceResult
