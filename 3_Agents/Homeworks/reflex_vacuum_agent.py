A = 'A'
B = 'B'
C = 'C'
D = 'D'

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Dirty',
    D: 'Dirty',
    'Current': A
}


def REFLEX_VACUUM_AGENT(loc_st):  # Determine action
    if loc_st[1] == 'Dirty':
        return 'Suck'
    elif loc_st[0] == A:
        return 'Right'
    elif loc_st[0] == B:
        return 'Down'
    elif loc_st[0] == C:
        return 'Left'
    elif loc_st[0] == D:
        return 'Up'


def Sensors():  # Sense Environment
    location = Environment['Current']
    return (location, Environment[location])


def Actuators(action):  # Modify Environment
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    # From position A to B and B back to A
    elif action == 'Right' and location == A:
        Environment['Current'] = B
    elif action == 'Left' and location == B:
        Environment['Current'] = A
    # From position B to C and C back to B
    elif action == 'Down' and location == B:
        Environment['Current'] = C
    elif action == 'Up' and location == C:
        Environment['Current'] = B
    # From position C to D and D back to C
    elif action == 'Left' and location == C:
        Environment['Current'] = D
    elif action == 'Right' and location == D:
        Environment['Current'] = C
    # From position D to A and A back to D
    elif action == 'Up' and location == D:
        Environment['Current'] = A
    elif action == 'Down' and location == A:
        Environment['Current'] = D


def run(n):  # run the agent through n steps
    print('    Current                        New')
    print('location    status  action  location    status')
    for i in range(1, n):
        (location, status) = Sensors()  # Sense Environment before action
        print("{:12s}{:8s}".format(location, status), end='')
        action = REFLEX_VACUUM_AGENT(Sensors())
        Actuators(action)
        (location, status) = Sensors()  # Sense Environment after action
        print("{:8s}{:12s}{:8s}".format(action, location, status))


if __name__ == '__main__':
    run(20)
