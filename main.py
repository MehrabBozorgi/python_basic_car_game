command = ''
started = False
while True:

    command = input('> ').lower()

    if command == 'start':
        if started:

            print('Hoy, car is started')
        else:
            started = True
            print('Car Started... Ready to go')

    elif command == 'stop':
        if not started:
            print('Hoy, car is stopped')
        else:
            started = False
            print('Car stopped')

    elif command == 'quit':
        print('Good by then.')
        break

    elif command == 'help':
        print("""
 start - to start the car
 stop - to stop the car
 exit - to exit
        """)

    else:
        print("I don't understand")
