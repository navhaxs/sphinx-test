class my_app_to_autodoc:
    
    def add (a, b):
        '''
        Adds two numbers.

        :return: the sum.

        :param a: the first number. asdasfksdkdgas;dkasgsdf/
        :param b: the second number.

        '''
        return a + b

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale
