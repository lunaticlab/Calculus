# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 23:04:55 2021

@author: 劉之岳
"""

import sys
import numpy as np

class Calculus():
    def __init__(self,f,h=10**-6):
        self.f=f #f is given function
        self.h=h #h is the number approach to zero
        
    def diff(self,f,x):#differential
        
        h=self.h
        differential=(f(x+h)-f(x))/h
        return differential
    def newton(self,x,error=10**-5):#x is the initial_guess
        temp=0;f=self.f
        while abs(temp-x)>error:
            root=x-f(x)/self.diff(f,x)
            temp=x
            x=root
        return root


    def integral(self,a,b,f,n=100000):# a is downside;b is upside; f is function ;n is the slicenumber
        x = np.linspace(a, b, n)
        delta_x=(b-a)/n
        
        integral=0
        
        
        if type(f)!=str:#directly input function
            for i in x:
                integral+=f(i)*delta_x

        else:#input calculus method ex:like arc          
            f=getattr(Calculus, f)
            for i in x:
                integral+=f(self,i)*delta_x
        return integral
        
    
    def arc(self,x):#arc length
        f=self.f
        differential=self.diff(f,x)
        
        arc_length=np.sqrt(1+differential**2)
        return arc_length
    def surface(self,x):
        f=self.f
        differential=self.diff(f,x)
        solid_surface=2*np.pi*f(x)*np.sqrt(1+differential**2)
        return solid_surface
    
    
    def prints(self,var_string):#f is the variable string
        frame = sys._getframe(1)
        all_vars = frame.f_locals
        
        var_name=var_string.split(',')
        for j in var_name:
            for i in all_vars:
                if i==j:
                    print(f'{i}={all_vars[i]:.4f}')
                    break
                    

