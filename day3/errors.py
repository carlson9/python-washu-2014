import traceback

class CustomException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


def i_call_a_function_with_errors():
    try:
        print "Calling a function..."
        #function_with_generic_error()
        #function_with_custom_error()
        function_with_unknown_error(1)
        #function_that_doesnt_exist()
        print "Tada!"
    except CustomException as inst:
        print "Custom Error Caught! Error({0})".format(inst.value)
    except NameError, AttributeError:
        print "Whoa"
    except:
        print "Default Error Caught!"
    else:
        print "No error raised."
        traceback.print_exc()
    finally:
        print "GoodBye!"

def function_with_generic_error():
    raise Exception, "Foo!"

def function_with_custom_error():
    raise CustomException, "FooBar!"

def function_with_unknown_error(foo):
    foo.bar()

i_call_a_function_with_errors()
