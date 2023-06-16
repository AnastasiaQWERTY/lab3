


class Otdel(object):
    pass

    def __init__(self, name = 'Name', amount = 0, wamount = 0):
        self._number = _next_number()
        self.name = name
        self.amount = amount
        self.wamount = wamount

    def changename(self, name):
        self.name = name

    def add(self, amount):
        self.amount += amount


_next = 0

def _next_number():
    global _next
    _next += 1
    return  _next



class Client(object):

    def __init__(self, clientname = 'Name', address = 'Address' , paymenttype = 'Cash'):
        self.clientname = clientname
        self.address = address
        self.paymenttype = paymenttype

    def changeaddress(self, address):
        self.address = address


    def test_changeaddress(self):
        print(self.address)
        address = raw_input('enter address')
        #address = str(input('enter address'))
        self.changeaddress(address)
        print('new address is ' + ' ' + str(self.address))


class Provider(object):
    def __init__(self, name = 'Name', address = 'Address', country = 'Country', typet = 'Car', typep = 'Cash'):
        self.name = name
        self.address = address
        self.country = country
        self.typet = typet
        self.typep = typep


class Tovar(object):
    def __init__(self, name = 'Name', otdel = 'Otdel_0', provider = 'Provider', hr = '-15 ~ +2', expdate = ''):
        self.name = name
        self.otdel = otdel
        self.provider = provider
        self.hr = hr
        self.expdate = expdate


class Sell(object):
    def __init__(self, client = 'Name', tovar = 'Name', date = '', time = '', amount = 0, price = 0):
        self.client = client
        self.tovar = tovar
        self.date = date
        self.time = time
        self.amount = amount
        self.price = price

    def add(self, amount):
        self.amount += amount

    def remove(self, amount):
        self.amount -= amount

    def transfer_from(self, tovar, amount):
        tovar.remove(amount)
        self.add(amount)

    def test_add(self):
        amount = int(input('enter how much you want to add:' + ' '))
        self.add(amount)
        print('new amount =' + ' ' + str(self.amount))

        


if __name__ == '__main__':

    o1 = Otdel()
    print(o1.name)
    o2 = Otdel('new name', 2, 3)
    print(o2.name)
    o3 = Otdel(amount=2)
    print(o3._number, o3.amount)
    o4 = Otdel(wamount=2)
    print(o4._number)
    o5 = Otdel()
    o5.add(30)
    print(o5.amount)

    c1 = Client()
    print(c1.address)
    c1.changeaddress('new address')
    print(c1.address)

    c2 = Client()
    c2.test_changeaddress()

    p1 = Provider('sName', 'someaddress', 'somecountry', 'car', 'card')
    print(p1.country)
    p2 = Provider(country='Lakahaha')
    print(p2.country)


    t = Tovar('Pizza', 1, 'FunnyPizza', 'hranit pri -10', '22.12.22')
    print(t.expdate)
    t1 = Tovar(name = 'PizzaCool')
    from datetime import date
    t1.expdate = date.today()
    print(t1.name +' '+ str(t1.expdate))



    s = Sell('client', 'sometovar', '20.10.22', '12:41', 3, 599)
    from datetime import date
    s.date = date.today()
    print(s.date)
    print(s.amount)
    s.add(6)
    print(s.amount)

    s1 = Sell(amount=7)
    print(s1.amount)
    s.transfer_from(s1, 2)
    print(s1.amount)
    print(s.amount)

    s2 = Sell(amount=100)
    print(s2.amount)
    s2.test_add()
