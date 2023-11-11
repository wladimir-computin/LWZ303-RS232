from protocol.defs.defs2x6.defs2x6 import *
from transport.transport_common import FLAG_HELLO, FLAG_READ, FLAG_RESET
import time

class Wrapper:
	def __init__(self, comm):
		self.comm = comm
		
	def getSingleGroup(self, group, keepalive=False):
		if keepalive:
			flags = [FLAG_HELLO, FLAG_READ, FLAG_RESET]
		else:
			flags = [FLAG_HELLO, FLAG_READ]
		out = group(self.comm.readRegister(group.command, flags=flags))
		return out
	
	def getSingleParameter(self, param):
		group = paramToGroup(param)
		out = self.getSingleGroup(group).values[param.name]
		return out
	
	def getSingleStatus(self, status):
		group = statusToGroup(status)
		out = self.getSingleGroup(group).values[status.name]
		return out
	
	def getBulkGroups(self, groups):
		commands = [g.command for g in groups]
		response = self.comm.readRegisterBulk(commands)
		results = dict(map(lambda x, y: (x.name, x(y)), groups, response))
		return results
	
	def getBulkParameters(self, parameters):
		pmap = {}
		for p in parameters:
			pmap[p] = paramToGroup(p)
		groups = []
		for p,g in pmap.items():
			if g not in groups:
				groups.append(g)
		results1 = self.getBulkGroups(groups)
		results2 = {}
		for p,g in pmap.items():
			results2[p.name] = results1[g.name].values[p.name]
		return results2
	
	def getBulkStatus(self, status):
		smap = {}
		for s in status:
			smap[s] = statusToGroup(s)
		groups = []
		for s,g in smap.items():
			if g not in groups:
				groups.append(g)
		results1 = self.getBulkGroups(groups)
		results2 = {}
		for s,g in smap.items():
			results2[s.name] = results1[g.name].values[s.name]
		return results2
			
	def setSingleParameter(self, param, value):
		group = paramToGroup(param)
		reg = self.getSingleGroup(group, keepalive=True)
		print(reg)
		if isinstance(reg.values[param.name].value, InformationObj):
			reg.values[param.name].value.value = value
		else:
			reg.values[param.name].value = value
		reg.update_recursive()
		return group(self.comm.writeRegister(reg.command, reg.toBytes(), flags=[FLAG_READ, FLAG_RESET])).values[param.name]
		
	def setSingleGroup(self, group, values):
		reg = self.getSingleGroup(group, keepalive=True)
		print(reg)
		for k,v in values.items():
			if k in reg.values.keys():
				if isinstance(reg.values[k].value, InformationObj):
					reg.values[k].value.value = v
				else:
					reg.values[k].value = v
		reg.update_recursive()
		return group(self.comm.writeRegister(reg.command, reg.toBytes(), flags=[FLAG_READ, FLAG_RESET])).values
		
