
class TestExceptionHandeling():

    def test_exceptionHandling(self):
        try:
            a = 10
            b = 20
            c = 0

            d = (a + b) / c
            print(d)
        except:
            print("In the except block")
        else:
            print("Because there was no exception, else is executed")
        finally:
            print("Finally, always executed")

