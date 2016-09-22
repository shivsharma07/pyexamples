import time
f=None
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='', flush=True)
        time.sleep(2)
except FileNotFoundError:
    print("Could not find the file")
except KeyboardInterrupt:
    print("!! You cancelled reading from the file.")
finally:
    if f:
        f.close()
    print('Cleaning up: closed the file.')
