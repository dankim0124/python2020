import simpy
"""
def car(env, id, speed):
  print('Car %d: Start parking at %d' % (id, env.now))
  parking_duration = speed
  yield env.timeout(parking_duration)

  print('Car %d: Start driving at %d' % (id,env.now))
  trip_duration = 2
  yield env.timeout(trip_duration)

def main():
  env = simpy.Environment()
  env.process(car(env, 1, 5))
  env.process(car(env, 2, 10))

  env.run(until=20)
"""
"""
def clock(env, name, tick):
  while True: #Never-ending loop
    print(name, env.now)
    yield env.timeout(tick)

def main():
  env = simpy.Environment()
  env.process(clock(env, 'tick', 1))
  env.process(clock(env, 'tock', .5))
  env.run(until=10)
"""


greenLight = True
def stopLight(env):
    global greenLight #we are going to modify a global variable so it must be declared.
    while True:
        #Cycle from green->yellow->red
        print("Green")
        greenLight = True
        yield env.timeout(30)
        print("Yellow")
        yield env.timeout(2)
        print("Red")
        greenLight = False
        yield env.timeout(20)

def car(env, id):
    print('Car %d: Arrived at %d' % (id, env.now))
    #check to see if we can go, if not wait until we can.
    while greenLight == False:
        yield env.timeout(1)

    print('Car %d: Departed at %d' % (id,env.now))

def carArrival(env):
    #Cars arrive every 5 seconds
    carNum = 0
    while True:
        carNum = carNum + 1
        env.process(car(env, carNum))
        yield env.timeout(5)



def main():
    env = simpy.Environment()
    env.process(carArrival(env))
    env.process(stopLight(env))
    env.run(until=100)
    print("Simulation comptete")

if __name__ == '__main__':
    main()

main()
