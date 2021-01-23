import math
import random
import time
import datetime
import asteroid


class Controller:
    """
    Represents a controller for asteroids in space.
    """
    def __init__(self):
        """
        Initializer for controller. Uses random.randint to assign random values for each asteroid's
        radius and velocity.
        """
        self._ast_list = []
        for i in range(0, 100):
            self._ast_list.append(asteroid.Asteroid(2 * math.pi * random.randint(1, 4),
                                                    100, 100, 100, random.randint(0, 5),
                                                    random.randint(0, 5), random.randint(0, 5)))

    def simulate(self, seconds):
        """
        Waits until a whole second, then simulates moving asteroids.
        :param seconds: an int
        """
        time_until_second = 1000000 - datetime.datetime.now().microsecond
        time.sleep(time_until_second / 1000000)

        print("Simulation Start Time: ", datetime.datetime.now(), "\n")
        print("Moving Asteroids! \n--------------------")

        for i in range(0, seconds):
            for j in range(0, len(self._ast_list)):
                print(self._ast_list[j].move())
                print(self._ast_list[j].__str__())
            time.sleep(1)


def main():
    """
    Instantiates a controller and simulates asteroids moving.
    """
    control1 = Controller()
    control1.simulate(3)


if __name__ == "__main__":
    main()
