"""
  class project definitions
  Project
  - has a name
  - has a ID
"""

class tr_project:
	def __init__(self, name, orderdate, startdate, enddate, budget):
		self.name = name
		self.orderdate = orderdate
		self.startdate = startdate
		self.enddate = enddate
		self.budget = budget

	def set_startdate(self, new_startdate)
		self.startdate = new_startdate

	def set_enddate(self, new_enddate)
		self.enddate = new_enddate


