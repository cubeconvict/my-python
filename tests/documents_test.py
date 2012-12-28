import unittest
from sopy.documents import DocumentStatistics

class DocumentsTestCase(unittest.TestCase):

  def setUp(self):
    self.lines = [
      'abc,123,xyz',
      'axskskdkd,xx,aaa',
      'akdjfkjakdf,akdfkksksksk,xx'
    ]

  def test_Printing(self):
    doc_stats = DocumentStatistics(self.lines)
    doc_stats.PrintAll()

  def test_ObjectFetch(self):
    doc_stats = DocumentStatistics(self.lines)
    column_widths = doc_stats.GetStatistic('Longest_Columns').column_widths

