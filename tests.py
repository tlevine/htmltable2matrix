import unittest
from htmltable2matrix import htmltable2matrix
from lxml.html import fromstring,tostring
from fixtures import row0,row1,bodyrows

def get_table():
  return fromstring(open('fixtures/table.html','r').read())

class TestLXML(unittest.TestCase):
  def setUp(self):
    self.table_xml=get_table()
    self.table_matrix=htmltable2matrix(self.table_xml)

  def test_no_side_effects(self):
    observed=tostring(self.table_xml)
    expected=tostring(get_table())
    self.assertEqual(observed,expected)

  def test_row_count(self):
    self.assertEqual(len(self.table_matrix),14)

  def row0(self):
    expected=[]
    self.assertEqual(self.table_matrix[0],expected)

  def row1(self):
    expected=[
      row1.days
    , row1.fromstop1
    , row1.fromstop2
    , row1.fromstop3
    , row1.fromstop4
    , row1.arrow
    , row1.tostop
    , row1.route
    ]
    self.assertEqual(self.table_matrix[1],expected)

  def abstract_test_col(self,colnum,expected):
    self.assertEqual(self.table_matrix[1][colnum],expected)

  def test_row1_col0(self):
    self.abstract_test_col(0,row1.days)

  def test_row1_col1(self):
    self.abstract_test_col(1,row1.fromstop1)

  def test_row1_col2(self):
    self.abstract_test_col(2,row1.fromstop2)

  def test_row1_col3(self):
    self.abstract_test_col(3,row1.fromstop3)

  def test_row1_col4(self):
    self.abstract_test_col(4,row1.fromstop4)

  def test_row1_col5(self):
    expected=row1.arrow

  def test_row1_col6(self):
    expected=row1.route

  def bodyrows(self):
    expected=[]
    self.assertEqual(self.table_matrix[2:len(self.table_matrix)],expected)

if __name__ == '__main__':
  unittest.main()
