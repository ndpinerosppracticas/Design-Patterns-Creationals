class Director:
   __builder = None

   def setBuilder(self, builder):
      self.__builder = builder

   def getCar(self):
      car = Car()


      body = self.__builder.getBody()
      car.setBody(body)


      engine = self.__builder.getEngine()
      car.setEngine(engine)


      i = 0
      while i < 4:
         wheel = self.__builder.getWheel()
         car.attachWheel(wheel)
         i += 1
      return car


class Car:
   def __init__(self):
      self.__wheels = list()
      self.__engine = None
      self.__body = None

   def setBody(self, body):
      self.__body = body

   def attachWheel(self, wheel):
      self.__wheels.append(wheel)

   def setEngine(self, engine):
      self.__engine = engine

   def specification(self):
      print "Body: %s" % self.__body.shape
      print "Engine horsepower: %d" % self.__engine.horsepower
      print "Tire size: %d\'" % self.__wheels[0].size

class Builder:
      def getWheel(self): pass
      def getEngine(self): pass
      def getBody(self): pass

class JeepBuilder(Builder):

   def getWheel(self):
      wheel = Wheel()
      wheel.size = 12
      return wheel

   def getEngine(self):
      engine = Engine()
      engine.horsepower = 300
      return engine

   def getBody(self):
      body = Body()
      body.shape = "SUV"
      return body


class Wheel:
   size = None

class Engine:
   horsepower = None

class Body:
   shape = None

def main():
   jeepBuilder = JeepBuilder() # initializing the class

   director = Director()

   print "Jeep"
   director.setBuilder(jeepBuilder)
   jeep = director.getCar()
   jeep.specification()
   print ""

if __name__ == "__main__":
   main()