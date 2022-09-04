class Payment:
    def __init__(self, price):
        self.__instrument_price = price + price*0.25  
        
instrument = Payment(1285)
print(instrument.__instrument_price)

"""The above print would fail to work, as the instrument price is private. To make it 
work you need to add a get"""
class Payment:
    def __init__(self, price):
        self.__instrument_price = price + price*0.25

    def get_instrument_price(self):
        return self.__instrument_price

instrument = Payment(1285)
print(instrument.get_instrument_price())

"""However, if you need to make an adjustment
to the instrument price e.g. an exchange value for an instrument, you need to call a set 
method. """
class Payment:
    def __init__(self, price):
        self.__instrument_price = price + price*0.25

    def get_instrument_price(self):
        return self.__instrument_price

    def set_instrument_price(self, exchange):
        self.__instrument_price = (self.__instrument_price-exchange)

instrument = Payment(1285)
instrument.set_instrument_price(225)
print(instrument.get_instrument_price())
