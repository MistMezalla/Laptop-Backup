def light(signal):
    if signal=='RED':
        return(0)
    elif signal=='YELLOW':
        return(1)
    elif signal=='GREEN':
        return(2)

def trafficLight():
    signal=input('enter the colour of the signal: ')

    if (signal not in ('RED', 'GREEN' ,'YELLOW')):
        print('wrong input')

    else:
        Signal=light(signal)

        if Signal==0:
            print('SOP')
        elif Signal==1:
            print('WAIT')
        elif Signal==2:
            print('GO')

trafficLight()
print('SPEED THRILLS BUT KILLS')
