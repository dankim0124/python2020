import simpy
import random

eventLog = []
waitingShoppers = []
idleTime = 0
workingRecord=[0,0,0,0,0]

def shopper(env, id):
    # record time.
    arrive = env.now
    print("Process Shopper, ", env.now)
    # set num of items.
    items = random.randint(5, 20)
    shoppingTime = items // 2  # shopping takes 1/2 a minute per item.

    yield env.timeout(shoppingTime)  # ??? why wait here.
    waitingShoppers.append((id, items, arrive, env.now))


def checker(env, num):
    num = num
    print("Process checker :%d, time : %d " % (num, env.now))
    print(waitingShoppers)
    global idleTime
    while True:
        while len(waitingShoppers) == 0:
            idleTime += 1
            yield env.timeout(1)  # wait a minute and check again

        print("checker %d back!, time %d"% (num, env.now))
        customer = waitingShoppers.pop(0)
        checkoutTime = customer[2] // 10 + 1
        workingRecord[num]+=1

        yield env.timeout(checkoutTime)
        # customer :  id, item, arrive, env.now
        eventLog.append((customer[0], customer[1], customer[2], customer[3], env.now))


def customerArrival(env):
    # make new shopper. each shopper need to wait 2 min before getting registered.
    print("Process customerArrival, ", env.now)
    customerNumber = 0
    while True:
        customerNumber += 1
        env.process(shopper(env, customerNumber))
        yield env.timeout(2)  # New shopper every two minutes


def processResults():
    print("process processResult, ")
    totalWait = 0
    totalShoppers = 0

    for e in eventLog:
        waitTime = e[4] - e[3]  # depart time - done shopping time
        totalWait += waitTime
        totalShoppers += 1

    avgWait = totalWait / totalShoppers

    print("The average wait time was %.2f minutes." % avgWait)
    print("The total idle time was %d minutes" % idleTime)
    print ("checker record")
    total = sum(workingRecord)
    print ("total %d cases" %total)
    for i in range(5):
        print("checker %d deals %d cases" % (i, workingRecord[i]))


def main():
    # iteration num
    numberCheckers = 5

    # setup environment.
    env = simpy.Environment()

    # start customArrival process.
    env.process(customerArrival(env))

    for i in range(numberCheckers):
        env.process(checker(env, i))

    env.run(until=180)
    print(len(waitingShoppers))
    processResults()


if __name__ == '__main__':
    main()

# For me to go
# 1. get simulation working. (o)
# 2. process some other data than average wait time.
# 3. write a summary what learrned from this lecture.
