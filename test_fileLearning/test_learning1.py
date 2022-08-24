
"""def setup_module(module): # module setup
    print("Setup Module!")

def teardown_module(module): # module teardown
    print("Teardown Module!")

def setup_function(function): # function setup
    if function == test1:
        print("\nSetting up test1")
    elif function == test2:
        print("\nSetting up test2")
    else:
        print("\nSetting up unknown test")

def teardown_function(function): # function teardown
    if function == test1:
        print("\nTearing down test1")
    elif function == test2:
        print("\nTearing down test2")
    else:
        print("\nTearing down test")


def test1(): # function1
    print("Executing test1!")
    assert True

def test2(): # function2
    print("Executing test2!")
    assert True"""


"""class TestClass:
    @classmethod
    def setup_class(cls): # class setup
        print("Setup TestClass!")

    @classmethod
    def teardown_class(cls):  # class teardown
        print("teardown TestClass!")

    def setup_method(self,method):  # method setup
        if method == self.test1:
            print("\nSetting up test1")
        elif method == self.test2:
            print("\nSetting up test2")
        else:
            print("\nSetting up unknown test")

    def teardown_method(self,method):  # method teardown
        if method == self.test1:
            print("\nTearing down test1")
        elif method == self.test2:
            print("\nTearing down test2")
        else:
            print("\nTearing down test")

    def test1(self):  # function1
        print("Executing test1!")
        assert True

    def test2(self):  # function2
        print("Executing test2!")
        assert True 
        """
