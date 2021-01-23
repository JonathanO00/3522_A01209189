class Vector:
    """
    Represents a vector in x, y, and z coordinates.
    """

    def __init__(self, x, y, z):
        """
        Initializer for vector.
        :param x: an int
        :param y: an int
        :param z: an int
        """
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, vector):
        """
        Adds a vector to the current vector.
        :param vector: a vector
        :return: none
        """
        self._x += vector.get_x()
        self._y += vector.get_y()
        self._z += vector.get_z()

    def __str__(self):
        """
        Returns vector as a string.
        :return: Vector's coordinates as a string.
        """
        return "Vector as (X, Y, Z): ({0}, {1}, {2})".format(self._x, self._y, self._z)

    def return_tuple(self):
        """
        Returns vector as a tuple.
        :return: Vector's coordinates as a tuple.
        """
        return tuple((self._x, self._y, self._z))

    def get_x(self):
        """
        Getter for x coordinate.
        :return: X
        """
        return self._x

    def get_y(self):
        """
        Getter for y coordinate.
        :return: Y
        """
        return self._y

    def get_z(self):
        """
        Getter for z coordinate.
        :return: Z
        """
        return self._z

    prop_x = property(get_x)
    prop_y = property(get_y)
    prop_z = property(get_z)


class Asteroid:
    """
    Represents an asteroid.
    """

    # Static id for each asteroid.
    asteroid_id = 0

    def __init__(self, circumference, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z):
        """
        Initializer for the asteroid.
        :param circumference: a float
        :param pos_x: an int
        :param pos_y: an int
        :param pos_z: an int
        :param vel_x: an int
        :param vel_y: an int
        :param vel_z: an int
        """
        self.asteroid_id = Asteroid.assign_id()
        self._circumference = circumference
        self._position = Vector(pos_x, pos_y, pos_z)
        self._velocity = Vector(vel_x, vel_y, vel_z)

    @classmethod
    def assign_id(cls):
        """
        Helper method. Assigns an id to each asteroid automatically and increments the id number.
        :return: Asteroid's id
        """
        cls.asteroid_id += 1
        return cls.asteroid_id

    def __str__(self):
        """
        Returns the asteroid as a string.
        :return: Asteroid as a string
        """
        return "Asteroid {0} is currently at {1}, {2}, {3} and moving at {4}, {5}, {6} m/s." \
               " It has a circumference of {7}".format(self.asteroid_id, self._position.get_x(),
                                                       self._position.get_y(), self._position.get_z(),
                                                       self._velocity.get_x(),
                                                       self._velocity.get_y(), self._velocity.get_z(),
                                                       self._circumference)

    def move(self):
        """
        Moves the asteroid according to the velocity.
        :return: Asteroid's new position.
        """
        self._position.__add__(self._velocity)
        return "Asteroid {0} moved! New Position: {1}"\
            .format(self.asteroid_id, self._position.return_tuple())

    def get_circumference(self):
        """
        Getter for circumference.
        :return: circumference
        """
        return self._circumference

    def set_circumference(self, circumference):
        """
        Setter for circumference.
        :param circumference: a float
        :return: none
        """
        self._circumference = circumference

    def get_position(self):
        """
        Getter for position.
        :return: position
        """
        return self._position

    def set_position(self, position):
        """
        Setter for position.
        :param position: a vector
        :return: none
        """
        self._position = position

    def get_velocity(self):
        """
        Getter for velocity.
        :return: velocity
        """
        return self._velocity

    def set_velocity(self, velocity):
        """
        Setter for velocity.
        :param velocity: a vector
        :return: none
        """
        self._velocity = velocity

    prop_circumference = property(get_circumference, set_circumference)
    prop_position = property(get_position, set_position)
    prop_velocity = property(get_velocity, set_velocity)
