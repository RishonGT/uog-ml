import numpy as np

def Exercise_1(x,y):
    return (np.sqrt((x**2) + (y**2)))

result = (Exercise_1(3,4))

def Exercise_2():
    print(np.linspace(0,2*np.pi,20))
    print(np.pi)

def Exercise_3():
    q1 = np.exp(2)
    q2 = np.sqrt(8)
    q3 = np.log(np.exp(2*np.pi))
    q4 = 2**3 + 5**4 + 7
    q5 = np.cos(2*np.pi/3)
    q6 = np.tan(np.deg2rad(30))
    q7 = np.atan(np.sqrt(2))

    print(q1,q2,q3,q4,q5,q6,q7)

def Exercise_4(string1,string2):
    print(string1 + string2)
    print(3*string1)
    # print(string1 - string2)

def Exercise_5():
    print("{0:<2} x {1:<2} = {2:<}".format( 4, 5, 4*5))
    print("{0:<2} x {1:<2} = {2:<}".format( 10, 20, 10*20))
    print("{0:<2} x {1:<2} = {2:<}".format( 10, 5, 10*5))
    print("{0:<2} x {1:<2} = {2:<}".format( 4, 20, 4*20))

def Exercise_6():
    my_list = ['Hello', 'My', 'Name', 'Is', 'Bob']

    my_list.append('Bye')
    print(my_list)
    my_list.extend('See You Soon')
    print(my_list)

    my_list.insert(0,'Oh')
    print(my_list)

    my_list.remove('Hello')
    print(my_list)

def Exercise_7():
    theta = np.deg2rad(25)
    v0 = 7.5
    g = 9.81

    vy0 = v0*np.sin(theta)
    vx0 = v0*np.cos(theta)

    T = (2*vy0)/g

    h = []
    d = []
    for t in [0.2, 0.4, T]:
        h.append(vy0*t - (g*t**2)/2)
        d.append(Exercise_1(vx0*t,vy0*t - (g*t**2)/2))
    
    totald = vx0*T
    maxh = vy0*T/2 - (g*(T/2)**2)/2

    print(f"""
        Initial Horizontal Velocity = {vx0}
        Initial Vertical Velocity   = {vy0}
        Total Time in Air = {T}
        Altitude, Distance at t_1 = {h[0]}, {d[0]}
        Altitude, Distance at t_2 = {h[1]}, {d[1]} 
        Altitude, Distance at T   = {h[2]}, {d[2]} 
        Maximum Altitude = {maxh}
        Total Distance = {totald}
          """)
Exercise_7()