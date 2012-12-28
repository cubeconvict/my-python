from collections import defaultdict

class LineStatistic(object):

  def __repr__(self):
    """Convert class to string"""

    heading = self.__class__.__name__.replace('_', ' ')

    item_keys = []
    for key in dir(self):
      if not key.startswith('_') and not callable(getattr(self, key)):
        item_keys.append(key)

    item_values = [getattr(self, key) for key in item_keys]
    key_value_pairs = zip(item_keys, item_values)

    line = '  {0}:  {1}\n'
    lines = [line.format(k.replace('_', ' '), v) for k, v in key_value_pairs]

    body = ''.join(lines)

    return """{0}:\n{1}""".format(heading, body)

  def CountLine(self, line_number, line, line_items):

    raise NotImplementedError('You must override the CountLine method')

class LineStats(object):
  class Most_Items(LineStatistic):
    """Count most items"""

    def __init__(self):

      self.line_number = -1
      self.item_count = -1

    def CountLine(self, line_number, line, line_items):

      item_count = len(line_items)

      if item_count > self.item_count:
        self.item_count = item_count
        self.line_number = line_number

  class Longest_Line(LineStatistic):
    """ Count the longest line """

    def __init__(self):
      self.line_number = -1
      self.line_length = -1

    def CountLine(self, line_number, line, line_items):

      line_length = len(line)
      if line_length > self.line_length:
        self.line_length = line_length
        self.line_number = line_number

  class Longest_Item(LineStatistic):
    """Count longest item in line"""

    def __init__(self):

      self.line_number = -1
      self.item_count = -1
      self.item_length = -1
      self.item_position = -1

    def CountLine(self, line_number, line, line_items):

      for position, item in enumerate(line_items):

        item_length = len(item)

        if  item_length > self.item_length:
          self.item_count = len(line_items)
          self.item_length = item_length
          self.line_number = line_number
          self.item_position = position

  class Longest_Columns(LineStatistic):
    """Count the longest columns"""

    def __init__(self):
      self.column_widths = defaultdict(int)

    def CountLine(self, line_number, line, line_items):

      column_widths = self.column_widths

      for position, item in enumerate(line_items):
        column_width = len(item)

        if column_width > column_widths[position]:
          column_widths[position] = column_width


class DocumentStatistics(object):

  def __init__(self, lines, delimiter=',', statistics=None):
    """ Initialize the object with an iterable

    Each item returned by the lines iterable is assumed to be a line of text

    args:
      lines: a list, generator or file like object for iteration
      delimiter(','): string delimiter to split line into items
      statistics(None): list of statistics objects

    """
    self._lines = lines
    self._delimiter = delimiter
    self._calculated = False

    if statistics:
      self._statistics = statistics
    else:
      self._statistics = [getattr(LineStats, s)() for s in dir(LineStats) if not s.startswith('_')]

    self._stat_lookup = None

  def _CalculateAll(self):
    """Calculate Statistics"""

    line_number = 1
    for line in self._lines:

      line_items = line.split(self._delimiter)

      for statistic in self._statistics:
        statistic.CountLine(line_number, line, line_items)
      line_number += 1

  @property
  def statistics(self):
    if not self._calculated:
      self._CalculateAll()

    return self._statistics

  def PrintAll(self):
    """Print all statistics"""

    for statistic in self.statistics:
      print statistic

  def GetStatistic(self, stat_name):
    """Return all statistics in dictionary with class name as key"""

    if not self._stat_lookup:
      self._stat_lookup = {s.__class__.__name__:s for s in self.statistics}

    return self._stat_lookup[stat_name]
