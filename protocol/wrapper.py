from protocol.defs.defs2x6.defs2x6 import *

class Wrapper:
	def __init__(self, comm):
		self.comm = comm
		
	def getSingleGroup(self, group):
		out = group(self.comm.readRegister(group.command))
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
		results = list(map(lambda x, y: x(y), groups, response))
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
		results2 = []
		for p,g in pmap.items():
			for group in results1:
				if isinstance(group, g):
					results2.append(group.values[p.name])
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
		results2 = []
		for s,g in smap.items():
			for group in results1:
				if isinstance(group, g):
					results2.append(group.values[s.name])
		return results2
			
	def setSingleParameter(self, param, value):
		reg = self.getSingleGroup(paramToGroup(param))
		if isinstance(reg.values[param.name].value, InformationObj):
			reg.values[param.name].value.value = value
		else:
			reg.values[param.name].value = value
		reg.update_recursive()
		return group(self.comm.writeRegister(reg.command, reg.toBytes())).value(param.name)
		
	def setSingleGroup(self, group, value):
		#too dangerous
		return None
		#return group(comm.writeRegister(group.command, value.toBytes()))
		
