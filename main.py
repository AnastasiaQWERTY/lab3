class Otdel(object):
    pass

    def __init__(self, number, name, amount, wamount):
        self.number = number
        self.name = name
        self.amount = amount
        self.wamount = wamount

    def changename(self, name):
        self.name = name

    def add(self, amount):
        self.amount += amount

class Client(object):

    def __init__(self, clientname, address, paymenttype):
        self.clientname = clientname
        self.address = address
        self.paymenttype = paymenttype

    def changeadress(self, address):
        self.address = address

class Provider(object):
    def __init__(self, name, address, country, typet, typep):
        self.name = name
        self.address = address
        self.country = country
        self.typet = typet
        self.typep = typep


class Tovar(object):
    def __init__(self, name, otdel, seller, hr, expdate):
        self.name = name
        self.otdel = otdel
        self.seller = seller
        self.hr = hr
        self.expdate = expdate

class Sell(object):
    def __init__(self, client, tovar, date, time, amount, price):
        self.client = client
        self.tovar = tovar
        self.date = date
        self.time = time
        self.amount = amount
        self.price = price

    def add(self, amount):
        self.amount += amount

if __name__ == '__main__':
    o = Otdel(1, 'magazin', 6, 7)
    print(o.name + ' ' + '-name before')
    o.changename('nemagazin')
    print(o.name + ' ' + '-name after')
    print(o.amount)
    o.add(50)
    print(o.amount)

    c = Client('Lala', 'old address', 'card')
    print(c.address)
    c.changeadress('new address')
    print(c.address)

    p = Provider('sName', 'someaddress', 'somecountry', 'car', 'card')
    print(p.typet)

    t = Tovar('Pizza', 1, 'FunnyPizza', 'hranit pri -10', '22.12.22')
    print(t.expdate)

    s = Sell('client', 'sometovar', '20.10.22', '12:41', 3, 599)
    s.add(6)
    a = s.amount * s.price
    print(s.amount)
    print(a)

