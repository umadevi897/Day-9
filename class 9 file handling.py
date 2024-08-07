# class 9 
#  error handling


try:
    print(a)
except:
    print("error vachindi")
else:
    print("errot raledu")
finally:
    print("always")

try:
    print('a'+10)
    print(a)
except TypeError:
    print("Type Error occured")
except NameError:
    print("Name Error occured")
    
try:
    print('a'+10)
except :
    print("Error occured")  

try:
print('a'+10)
except Exception as uma:
   print("Error occured")
 
 
try: 
   print('a'+10)
except type Error:
try:
       print()
    except:
        print("inner") 

try:
    print('a'+10)
except:
    print("outter")
    try:
        print(a)
    except:
        print("inner")

if True:
    print("This is ") 

try:
    print('a'+10)
    print(a)
exceptException as uma:
    print("Error occured")
try:
    print('a'+10)
except TypeError:
    print("Type Error occured")
except NameError:
    print("Name Error occured")

