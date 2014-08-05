def is_triangle(first, second, third):
    lengths = sorted([first,second,third])
    if lengths[2] <= lengths[0]+lengths[1]:
        print "Yes"
    else: print "No"

def prompt():
    first = int(raw_input("Input first side: ",))
    second = int(raw_input("Input second side: ",))
    third = int(raw_input("Input third side: ",))
    is_triangle(first, second, third)

