
# Definition and test function for class Cylinder.

import math
from PointModule import Point
from CircleModule import Circle

class Cylinder( Circle ):
   """Class that represents a cylinder"""

   def __init__( self, x, y, radius, height ):
      """Constructor for Cylinder takes x, y, height and radius"""

      Circle.__init__( self, x, y, radius )
      self.height = float( height )

   def area( self ):
      """Calculates (surface) area of a Cylinder"""

      return 2 * Circle.area( self ) + \
         2 * math.pi * self.radius * self.height

   def volume( self ):
      """Calculates volume of a Cylinder"""

      return Circle.area( self ) * self.height

   def __str__( self ):
      """String representation of a Cylinder"""

      return "%s; Height = %f" % \
         ( Circle.__str__( self ), self.height )

# main program
def main():

   # create object of class Cylinder
   cylinder = Cylinder( 12, 23, 2.5, 5.7 )

   # print Cylinder attributes
   print("X coordinate is:", cylinder.x)
   print("Y coordinate is:", cylinder.y)
   print("Radius is:", cylinder.radius)
   print("Height is:", cylinder.height)

   # change Cylinder attributes
   cylinder.height = 10
   cylinder.radius = 4.25
   cylinder.x, cylinder.y = 2, 2
   print("\nThe new points, radius and height of cylinder are:", \
      cylinder)

   print("\nThe area of cylinder is: %.2f" % cylinder.area())

   # display the Cylinder as a Point
   print("\ncylinder printed as a Point is:", \
      Point.__str__( cylinder ))

   # display the Cylinder as a Circle
   print("\ncylinder printed as a Circle is:", \
      Circle.__str__( cylinder ))

if __name__ == "__main__":
   main()

