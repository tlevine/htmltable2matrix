import unittest
from htmltable2matrix import htmltable2matrix
from lxml.html import fromstring
from lxml.etree import tostring
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

  def abstract_test_col(self,rownum,colnum,expected):
    self.assertEqual(self.table_matrix[rownum][colnum],expected)

  def test_row0_col0(self):
    self.abstract_test_col(0,0,row0.days)

  def test_row0_col1(self):
    self.abstract_test_col(0,1,row0.fromcity)

  def test_row0_col2(self):
    self.abstract_test_col(0,2,row0.fromcity)

  def test_row0_col3(self):
    self.abstract_test_col(0,3,row0.fromcity)

  def test_row0_col4(self):
    self.abstract_test_col(0,4,row0.fromcity)

  def test_row0_col5(self):
    self.abstract_test_col(0,5,row0.arrow)

  def test_row0_col6(self):
    self.abstract_test_col(0,6,row0.tocity)

  def test_row0_col7(self):
    self.abstract_test_col(0,7,row0.route)

  def test_row1_col0(self):
    self.abstract_test_col(1,0,row1.days)

  def test_row1_col1(self):
    self.abstract_test_col(1,1,row1.fromstop1)

  def test_row1_col2(self):
    self.abstract_test_col(1,2,row1.fromstop2)

  def test_row1_col3(self):
    self.abstract_test_col(1,3,row1.fromstop3)

  def test_row1_col4(self):
    self.abstract_test_col(1,4,row1.fromstop4)

  def test_row1_col5(self):
    self.abstract_test_col(1,5,row1.arrow)

  def test_row1_col6(self):
    self.abstract_test_col(1,6,row1.tostop)

  def test_row1_col7(self):
    self.abstract_test_col(1,7,row1.route)

  def bodyrows(self):
    expected=[]
    self.assertEqual(self.table_matrix[2:len(self.table_matrix)],expected)

if __name__ == '__main__':
  unittest.main()
