baseAddress = "192.168.0."

hostAddress = range(20)

ipRange = []

for i in hostAddress:
	ipRange.append(baseAddress + str(i))

for ipAddr in ipRange:
	print ipAddr

print "process completed"