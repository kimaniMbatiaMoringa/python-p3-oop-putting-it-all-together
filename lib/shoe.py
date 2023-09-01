#!/usr/bin/env python3
import ipdb
class Shoe:
    def __init__(self,brand,size,condition="Old"):
        self.brand = brand
        self.size = size
        self.conditon = condition
    
    def get_shoe_size(self):
        return self._size
    
    def set_shoe_size(self,value):
        if type(value)!= int:
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self, condition="New"):
        print("Your shoe is as good as new!")
        self.conditon = condition

    size = property(fget=get_shoe_size,fset=set_shoe_size)

ipdb.set_trace()  