from time import sleep
import threading


# Suggestion: add threading
def scheduler(func, n):
    def main():
        sleep(n / 1000)
        func()

    # main()
    t = threading.Thread(target=main)
    t.start()


# Testing
def sideTask():
    print("Side Task starting...")


print("Main Program: Starting...")
scheduler(sideTask, 1000)
print("Main Program: Continuing...")
