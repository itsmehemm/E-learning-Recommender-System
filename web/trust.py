

def overallTrust(globalTrust, localTrust, b, users):
	

def globalTrust(reputation, vote, a, users):
	gt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(0, len(reputation)):
		gt[i] = a * reputation[i] + (1-a) * vote[i]
	return gt	
	

reputation = [0.233451, 0.432233, 0.603234, 0.872123, 0.004323, 0.187345, 0.912090, 0.598312, 0.000404, 0.390123]

vote = [10, 2, 0, 4, 100, 193, 233, 12, 46, 31]

a = 0.75
b = 0.5
globaltrust = globalTrust(reputation, vote, a, 10)
#localtrust = localTrust()
#overall = overallTrust(globalTrust, localTrust, b)
#print(overall)

