# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from location import Location
from region import Region


class Match(Region):
    """Class Match with setters and getters for region parameters."""

    def __init__(self, x, y, width, height, score):
        """Function assign values to the x, y, width, height and score region parameters.

        :param x: Location x parameter.
        :param y: Location y parameter.
        :param width: Region's width.
        :param height: Region's height.
        :param score: Similarity with which the pattern is found.
        """

        Region.__init__(self, x, y, width, height)
        self._width = width
        self._height = height
        self._score = score

    def get_target(self):
        """Returns a location object."""
        return Location(self._x, self._y)

    def get_score(self):
        """Returns the similarity with which the pattern is found."""
        return self._score
