import output
import datetime

class Print(output.Output):
	requiredData = []
	optionalData = []
	def __init__(self,data):
		pass
	def outputData(self,dataPoints):
		# print "Time: " + str(datetime.datetime.now())
		for i in dataPoints:
			# print i["name"] + ": " + str(i["value"]) + " " + i["symbol"]
			print str(i["value"])
		return True
