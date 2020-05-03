from bitstring import ConstBitStream, BitStream, Bits

class InformationObj(object):
	name = ""
	description = ""

	parsemap = {}
	parent = None
	unit = ""
	value = None
	val_min = 0
	val_max = 0
	val_default = 0

	def __init__(self, data=None, value=None):
		self.unparsed = bytes()
		if data is not None:
			start = data.bytepos
			for k,v in self.parsemap.items():
				if isinstance(v, str):
					self.value = data.read(v)
				else:
					self.value = v(data)
			self.rawdata = data.bytes[start:data.bytepos]
		else:
			if value >= self.val_min and value <= self.val_max:
				self.value = value
				self.update()

	def update(self):
		bits = BitStream()
		for k,v in self.parsemap.items():
			if isinstance(v, str):
				bits.append(Bits(f"{v}={self.values[k]}"))
			else:
				bits.append(Bits(bytes=self.values[k].toBytes()))
		self.rawdata = bits.bytes

	def update_recursive(self):
		for k,v in self.parsemap.items():
			if not isinstance(v, str):
				self.value.update_recursive()
		self.update()
		
	def toBytes(self):
		return self.rawdata

	def __str__(self):
		return f"{self.name}: {self.value}{self.unit}"


class InformationGroup(object):
	name = ""
	description = ""

	parsemap = []
	values = {}

	def __init__(self, rawbytes=None):
		data = ConstBitStream(rawbytes)
		self.unparsed = bytes()
		if data is not None:
			start = data.bytepos
			for p in self.parsemap:
				if isinstance(p, str):
					data.read(p)
				else:
					self.values[p.name] = p(data)
			self.rawdata = data.bytes[start:data.bytepos]

	def update(self):
		bits = BitStream()
		for p in self.parsemap:
			if isinstance(p, str):
				bits.append(Bits(p))
			else:
				bits.append(Bits(bytes=self.values[p.name].toBytes()))
		self.rawdata = bits.bytes
		
	def update_recursive(self):
		for p in self.parsemap:
			if not isinstance(p, str):
				self.values[p.name].update_recursive()
		self.update()
		
	def toBytes(self):
		return self.rawdata
		
	def __str__(self):
		out = ""
		for k,v in self.values.items():
			out += f" {v}\n"
		return f"Name: {self.name}\n{self.description}\n{out}" 


class FixedPOneDec16():
	value = 0

	def __init__(self, data=None, value=None):
		if data is not None:
			start = data.bytepos
			self.value = data.read("int:16") / 10
			self.rawdata = data.bytes[start:data.bytepos]
		else:
			self.value = value
			self.update()
			
	def update(self):
		bits = BitStream()
		bits.append(Bits(f"int:16={self.value*10:d}"))
		self.rawdata = bits.bytes
		
	def update_recursive(self):
		self.update()
		
	def toBytes(self):
		return self.rawdata
		
	def __str__(self):
		return f"{self.value}"
	
	def __float__(self):
		return self.value
