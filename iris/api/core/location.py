# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from util.core_helper import INVALID_NUMERIC_INPUT


class Location(object):
    """Class Location with setters and getters for screen location parameters(x, y)."""

    def __init__(self, x=0, y=0):
        """Function assign values to the location parameters x and y."""
        self._x = x
        self._y = y

    @property
    def x(self):
        """Getter for the location x property."""
        return self._x

    @x.setter
    def x(self, x):
        """Setter for the location x property."""
        if isinstance(x, int):
            self._x = x
        else:
            raise ValueError(INVALID_NUMERIC_INPUT)

    @property
    def y(self):
        """Getter for the location y property."""
        return self._y

    @y.setter
    def y(self, y):
        """Setter for the location y property."""
        if isinstance(y, int):
            self._y = y
        else:
            raise ValueError(INVALID_NUMERIC_INPUT)

    def set_location(self, x=0, y=0):
        """Setter for the location x  and location y properties."""
        self._x = x
        self._y = y

    def offset(self, away_x, away_y):
        """Return a location object with offset for both x and y location parameters.

        :param away_x: Offset added to location x parameter.
        :param away_y: Offset added to location y parameter.
        :return: Location object.
        """
        new_x = int(self._x + away_x)
        new_y = int(self._y + away_y)
        return Location(new_x, new_y)

    def above(self, away_y):
        """Return a location object with offset for location y parameter.

        :param away_y: Offset decreased from the location y parameter.
        :return: Location object.
        """
        new_y = int(self._y - away_y)
        return Location(self._x, new_y)

    def below(self, away_y):
        """Return a location object with offset for location y parameter.

        :param away_y: Offset added to location y parameter.
        :return: Location object.
        """
        new_y = int(self._y + away_y)
        return Location(new_y)

    def left(self, away_x):
        """Return a location object with offset for location x parameter.

        :param away_x: Offset decreased from the location x parameter.
        :return: Location object.
        """
        new_x = int(self._x - away_x)
        return Location(new_x, self.y)

    def right(self, away_x):
        """Return a location object with offset for location x parameter.

        :param away_x: Offset added to location x parameter.
        :return: Location object.
        """
        new_x = int(self._x + away_x)
        return Location(new_x, self.y)
