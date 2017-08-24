import unittestdemo
import  unittest

#mysuite = unittest.TestSuite()
#mysuite.addTest(unittestdemo.MyTestCase("testLogInFailed"))
#mysuite.addTest(unittestdemo.MyTestCase("testLogInOK"))
cases = unittest.TestLoader().loadTestsFromTestCase(unittestdemo.MyTestCase)
mysuite = unittest.TestSuite([cases])
#mysuite.addTest(unittestdemo.MyTestCase("testLogIn"))

myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)