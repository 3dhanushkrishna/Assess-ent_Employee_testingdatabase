import sqlite3
import unittest
class checkemployeename(unittest.TestCase):
    def setUp(self):
        self.EMPNAME="John "
        self.EMPCODE="1102"
        self.connection=sqlite3.connect("Employee.db")
    def tearDown(self):
        self.EMPNAME=" "
        self.EMPCODE=" "
        self.connection.close()
    def test_employeename(self):
        result=self.connection.execute("select EMPNAME from EMPLOYEEDETAILS where EMPCODE="+self.EMPCODE)
        for i in result:
            fetchemployeename=i[0]
        self.assertEqual(self.EMPNAME,fetchemployeename)
if __name__=="__main__":
    unittest.main()
