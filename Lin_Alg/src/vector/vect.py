import math


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    
    
    def plus(self,x):
        new_coordinates= []
        n = len(self.coordinates)
        
        for i in range(n):
            new_coordinates.append(self.coordinates[i] + x.coordinates[i])
            
        return Vector(new_coordinates)
            
            
    def minus(self,x):
        new_coordinates = []
        n=len(self.coordinates)
        
        for i in range(n):
            new_coordinates.append(self.coordinates[i] - x.coordinates[i])
            
         
        return Vector(new_coordinates)   
                
    
    def scalar(self,x):
        new_coordinates = []
        n=len(self.coordinates)
        
        for i in range(n):
            new_coordinates.append(self.coordinates[i] * x)
            
         
        return Vector(new_coordinates)
    
            
            
    def magnitude(self):
        n=len(self.coordinates)
        res = 0
        
        for i in range(n):
            res = res + math.pow(self.coordinates[i], 2)
        
        res = math.sqrt(res)
        
        return res
    
    
    def normalize(self):
        magnitude = self.magnitude()
        magnitude = 1 /magnitude
        
        return (self.scalar(magnitude))
        
    def dot_product(self,x):
        n=len(self.coordinates)
        res = 0
        
        for i in range(n):
            res = res + (self.coordinates[i] * x.coordinates[i])
            
                
        return res
        
        
    def angle_rad(self,x):
        res = self.dot_product(x)
        res = res / (self.magnitude() * x.magnitude())
        angle = math.acos(res)
        
        return angle
    
    def angle_deg(self,x):
        
        return math.degrees(self.angle_rad(x))
    
    
        
        
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
