import multiprocessing
import time





#the function now takes an argument called 'seconds'

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)....')
    time.sleep(seconds)
    print('done sleeping...')

# below, two multiprocessing object are created.
# these objects dont actually run anything


#this loop is used to start multiple processes, and call the do_something fucntion
# the _ is a 'throw away variable".
#we cannot use p.join here because that would mean ithe processes would still run
#sequentially.

#we will therefore create an empty list, called 'processes' and append to it
def main ():

    #start the counter at start of execution
    start=time.perf_counter()

    processes = []

    #also, now lets feed an arument into the function of letting it sleep 1.5 seconds

    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.6])
        p.start()
        #this will append all processes to the list caLLed "processes"
        processes.append(p)

    #now let us use that list, to join so all the processes finish before the
    #remaining code is executed, which is what this following loop does

    for process in processes:
        process.join()

    #stop the clock/counter
    finish=time.perf_counter()

    #now substract the sfinish minus start, (essentially a stop watch)
    print(f'Finished in {round(finish-start,3)} second(s)')


if __name__ == '__main__':
    # freeze_support()
    main()