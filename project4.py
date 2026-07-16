# ========================================================
# PROJRCT:- FUNCTIONAL TREAT 
#=========================================================

#====================
# BY HITESH CHAUDHARY 
#====================


data = []

def input_data():
    """ Input 1D list"""
    global data

    data = list(map(int,input("enter numbers:").split()))


def factorial(n):
    """ Recursion"""
    if n == 0 or n== 1:
        return 1
    
    return n * factorial (n-1)


def filter_data ():
    """ Lambda with filter()"""
    value = int(input ( "enter a threshold)"))
    result = list(filter ( lambda x:x*x,data))
    print("squared data:",result)


def square_data ():

    """Lambda with map()"""
    result = list (map(lambda x:x*x,data))

    print("squared data ", result)

    
def statistics():
    """ Return multiples value """
    minimum=min(data)
    maximum=max(data)
    average=sum(data) / len(data)
    return minimum , maximum , average 


def sort_data():
    """ Sorting 1D list """
    temp=data.copy()

    temp.sort()
    print("ascending",temp)

    temp.sort(reverse=True)
    print ("descending", temp)

def display_2d():
    """Display 2D list""" 

    matrix =[
        [9,1,5],
        [1,8,3],
        [7,2,6]]
    

    print("\n2D list")
    for row in matrix :
        print (row)   


    print("\nsorted rows ")
    print(sorted(matrix))


while True:

    print("n\======== PART 2 =======")
    print("1. input data")
    print("2.factorial")
    print("3.filter data")
    print("4.square data")
    print("5.dataset statistics")
    print("6.sort data")
    print("7.display 2D List")
    print("8.exit")

    choice= input("enter ur choice")

    if choice == "1":
        input_data()

    elif choice =="2":
        n = int(input("enter a no")) 
        print("factorial =",factorial(n))

    elif choice =="3":
        filter_data()

    elif choice =="4":
        square_data()

    elif choice == "5":
        mn,mx,avg = statistics ()

        print ("minimum",mn)
        print ("maximum" , mx)
        print("average",avg) 

    elif choice =="6":
        sort_data()


    elif choice == "7" :
        display_2d()

    elif choice =="8":
        print("thank u !")
        break
    else:
        print("invalid choice")                         

       
               

            