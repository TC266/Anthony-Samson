def a():
    distance = float(input("how far was it?"))
    time = float(input("how long did it take?"))
    print(distance*time)


def b():
    mass = float(input("what is the mass?"))
    velocity = float(input("what is the velocity?"))
    print(mass*velocity)


def c():
    mass = float(input("what is the mass?"))
    acceleration = float(input("what is the acceleration"))
    print(mass*acceleration)


def d():
    # speed = distance/time
    distance = float(input("what was the distance?"))
    time = float(input("how long was it"))
    print(distance/time)


def e():
    length = float(input("what is the length?"))
    breadth = float(input("what is the breadth?"))
    print(length*breadth)

def main():
    choice = input("wat question do you want to work on?")

    if  choice == "a":
        a()
    elif choice == "b":
        b()
    elif choice == "c":
        c()
    elif choice == "d":
        d()
    elif choice == "e":
        e()
    else:
      print("invalid input")

if __name__  == '__main__':
    main()