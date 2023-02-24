''''class Transport:# Имя класса всегода пишется с большой буквы
	def __init__(self):# Инит инициализирует  функцию Селф Выбирает аргументом функцию в которой рабодтает
		self.name = 'Car'
		
	def get_name(self):
		self.name = str(input())# Если имя класса компонента начинается с двух подчеркиваний они считаются приватными
		return self.name


trans = Transport()
print(trans.get_name())




'''

''''class Stack:
	def __init__(self):
		self.__stack_List = []# Тут два пробела перед стэк листом наверное не просто так хз. Почитай
		
	def push(self,coin):
		self.__stack_List.append(coin)
		return coin
	
	def pop(self):
		coin = self.__stack_List[-1]
		self.__stack_List.pop()
		return coin
		
	def get_coins(self):
		return self.__stack_List
	

class SumStack(Stack):# Тут мы тип наследуемся и пишем новый класс в предыдуший
	def __init__(self):
		Stack.__init__(self)
		self.__sum = 0
		
	def get_Sum(self):
		return self.__sum
	
	def push(self, coin):
		self.__sum += coin
		Stack.push(self, coin)
		
	def pop(self):
		coin = Stack.pop(self)
		self.__sum -= coin
		return coin
	
object = SumStack()

for i in range(1,5):
	object.push(i)
	
	
object.push(5)
object.push(5)

#print(object.pop())
print(object.get_Sum())

print(object.get_coins())
'''

class Auto:
	def __init__(self):
		self.model = []
		self.ear = []
		self.manufacturer = []
		self.volume = []
		self.color = []
		self.price = []
		

	def push_mod(self,mod):
		self.model.append(mod)
		return self.model
		
	def push_ear(self, ear):
		self.ear.append(ear)
		return self.ear
	
	def push_man(self, man):
		self.manufacturer.append(man)
		return self.manufacturer
	
	def push_vol(self,vol):
		self.volume.append(vol)
		return self.volume
	
	def push_col(self, col):
		self.color.append(col)
		return self.color
	
	def push_pri(self,pri):
		self.price.append(pri)
		return self.price
	
	def __len__(self):
		return [len(self.model), len(self.ear),len(self.manufacturer)]
	
	def get_list(self):
		return [self.push_mod(input()),self.push_ear(input()),self.push_man(input())]


car = Auto()

car.push_ear('qwe')
print(car.get_list())
print(car.__len__())




'''x = int(input())
y = int(input())

class Book:
	def __init__(self):
		self.x = 0
		self.y = 0

	def pushX(self):
		self.x = int(input())# Можно сделать с определением имен классов внутри класса, но чет хз
		
	def pushY(self):
		self.y = int(input())

	def sum(self):
		return self.x + self.y
	
	def minus(self):
		return self.x - self.y
	
	def umnoj(self):
		return self.x * self.y
	
	def deli(self):
		return self.x / self.y
	
	def all(self):
		return [self.sum(),self.minus(),self.umnoj(),self.deli()]
dr = Book()
print(dr.all())
'''


















