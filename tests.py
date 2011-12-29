import unittest
from htmltable2matrix import htmltable2matrix
from lxml.html import fromstring
import fixtures.row1
import fixtures.row2
import fixtures.bodyrows

def get_table():
  return fromstring(open('fixtures/table.html','r').read())

class Test_lxml(unittest.TestCase):

  def setUp(self):
    self.table_xml=get_table()
    self.table_matrix=htmltable2matrix(self.table_xml)

  def no_side_effects(self):
    self.assertEqual(self.table_xml,get_table())

  def row_count(self):
    self.assertEqual(len(self.table_matrix),14)

  def row1(self):
    expected=[]
    self.assertEqual(self.table_matrix[0],expected)

  def row2(self):
    expected=[
      row2.days
    , row2.fromstop1
    , row2.fromstop2
    , row2.fromstop3
    , row2.fromstop4
    , row2.arrow
    , row2.tostop
    , row2.route
    ]

    self.assertEqual(self.table_matrix[1],expected)

  def bodyrows(self):
    expected=[]
    self.assertEqual(self.table_matrix[2:len(self.table_matrix)],expected)

if __name__ == '__main__':
  unittest.main()
