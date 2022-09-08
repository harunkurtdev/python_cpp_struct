mouse=open('/dev/input/mice')


while True:
    
    event=mouse.read(3)

    print(event)