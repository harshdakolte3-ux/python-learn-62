def main():

    a = 2
    b = 3.4
    c = True
    d = "Apple"
    e = [2, 'app', False]
    f = {1: "sunday", 2: "monday"}

    print(type(a))

    num_int=123
    num_flo=1.23
    num_new=num_int+num_flo
    print("Value of num_new:",num_new)
    print("Data types of num_new:",type(num_new))

def segregateMarks(lst):
    a = []
    b = []
    c = []

    for val in lst:
        if val > 80:
            a.append(val)
        elif val < 80 and val > 50:
            b.append(val)
        else:
            c.append(val)

    return a, b, c



def main():
    marks = [23, 65, 85, 29, 78, 93, 46, 62, 39]

    A_grade, B_grade, C_grade = segregateMarks(marks)

    print(f"A grade students are {A_grade}")
    print(f"B grade students are {B_grade}")
    print(f"C grade students are {C_grade}")

def main():
    units=int(input("enter the units of electricity used"))
    
    if(units==100):
        print("Bill is 100")
    elif(units>100 and units <200):
        bill=100+2*(200-units)
        print("Bill is",bill)
    elif(units==200):
        print("Bill is 300")
    else:
        bill=300+3*(units-200)
        print(bill)

        def week(i):
            switcher={
                0:'sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'saturday',

            }

            return switcher.get(i,"Invalid day of week")
        print(week(6))

        def cumulativeAddition(lst):
            out=[]
            addition =0
            for val in lst:
                addition += val
            out.append(addition)
            return out        

def main():
    numbers=[3,5,2,4,1]
    result=cumulativeAddition(numbers)
    print(result)
    
if __name__ == "__main__":
    main()
