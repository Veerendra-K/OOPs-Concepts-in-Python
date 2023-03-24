

class Sagar: #class created

    print("Hey, This is Veerendra K")
    #write something that you want to print

    optional = "This is an optional variable coz of showing How to access variable inside class"
    #optnl variable created

    def display(self):
    # user-defined function is created
    
        v = 103
        b = 40
        #Two variables created and assigned diff values
        
        print("The Sum is:" + str(v+b))
        print("Please Do Support and Follow for more...")
        #Note: To 'CONCAT' str with int, use ' str() ' function
        #performing addition n printing results
        
#if we need to call a function So required an 'object'
obj=Sagar() #Sagar() is class name
#object is created n it will work like 'Constructor'

obj.display()
#calling a user-defined function with obj

print(obj.optional)
#To access variable 'optional' that is available inside class
