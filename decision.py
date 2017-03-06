import numpy as np
from numpy import linalg as LA

#DEFINITIONS
SaatyIndex=[0,0,0.58,0.9,1.12,1.24,1.32,1.41,1.45,1.49]

#ENTER THE GOAL
print('Time to make some decisions\n\r')

goal=raw_input('What are we deciding upon?')


#ENTER THE CRITERIA
print('\n\rEnter each criteria for making this decision, type "done" when complete')

criterias=[]
criteria='undefined'
while(criteria!='done'):
	criteria=raw_input('\n\rcriteria >>')
	if criteria!='done':
		criterias.append(criteria)
	

print('OK, so we are deciding upon ' + goal + ' based on the following criteria:')
print(criterias)

print(' ')


#ENTER THE CANDIDATES
print('Now type in the candidates for selection, type "done" when complete:')

candidates=[]
candidate='undefined'
while(candidate!='done'):
	candidate=raw_input('\n\rcandidate >>')
	if candidate!='done':
		candidates.append(candidate)

print('\n\r')
print('OK, so we are deciding upon ' + goal + ' based on the following criteria:')
print(criterias)
print('With the following candidates:')
print(candidates)

print('\n\r')


#DO PAIRWISE COMPARISONS OF CRITERIA
print('Now let us add weights to each criteria via pairwise comparison')


criteriaMatrix=np.zeros((len(criterias),len(criterias)))
for i in range (0,len(criterias)):
	criteriaMatrix[i,i]=1


for i in range (0,len(criterias)-1):
	for j in range (i+1,len(criterias)):
		valid=0;
		while not valid:
			selection=raw_input('Which is more important, ' + criterias[i] + ' or ' + criterias[j] +'? >>')
			if selection==criterias[i]:
				valid=1
				inverted=0
				score = float(raw_input('How many times more important is ' + criterias[i] + ' compared to ' + criterias[j] +'?>>'))
				criteriaMatrix[i,j]=score
				criteriaMatrix[j,i]=1/score
			if selection==criterias[j]:
				valid=1
				inverted=1
				score = float(raw_input('How many times more important is ' + criterias[j] + ' compared to ' + criterias[i] +'?>>'))
				criteriaMatrix[i,j]=1/score
				criteriaMatrix[j,i]=score

		
n=len(criterias)			
#print(criteriaMatrix)
eigens=LA.eigvals(criteriaMatrix)
#print(eigens)
#print(max(eigens))
#print(np.absolute(max(eigens)))
CI = (np.absolute(max(eigens))-float(n))/(float(n)-1)
#print(CI)
CR = 0;
if n>10:
	RI=1.5
	CR=CI/RI*100
elif n>2:
	RI=SaatyIndex[n-1]
	#print(RI)
	CR=CI/RI*100

print('\n\r')
print('Your inputs are ' + str(CR) +'% inconsistent')
print('Your weights are:')

w, v = LA.eig(criteriaMatrix)
maxindex=np.argmax(w)
preWeights=v[:,maxindex]
weights=[]
for i in range(0,n):
	weights.append(np.absolute(preWeights[i]))

uniter=sum(weights)

for i in range(0,n):
	weights[i]=weights[i]/uniter

for i in range(0,n):
	print(criterias[i] + ' gets a weight of ' + str(weights[i]))
	

criteriaWeights=weights


numCriterias=len(criterias)
numCandidates=len(candidates)


#NOW ASSIGN SCORES FOR EACH CANDIDATE FOR EACH CRITERIA

print('time to find out how well each candidate does per the given criteria')

#DO PAIRWISE COMPARISONS OF CRITERIA
print('Now let us determine how well each candidate does in each criteria via pairwise comparison')


qualificationWeights=np.zeros((numCriterias,numCandidates))

contest=0;
for criteria in criterias:
	
	contest=contest+1;
	
	qualificationMatrix=np.zeros((numCandidates,numCandidates))
	for i in range (0,numCandidates):
		qualificationMatrix[i,i]=1


	for i in range (0,numCandidates-1):
		for j in range (i+1,numCandidates):
			valid=0;
			while not valid:
				selection=raw_input('Which is better at ' + criteria + ', ' + candidates[i] + ' or ' + candidates[j] +'? >>')
				if selection==candidates[i]:
					valid=1
					inverted=0
					score = float(raw_input('How many times better is ' + candidates[i] + ' compared to ' + candidates[j] + ' with regards to '+ criteria+'?>>'))
					qualificationMatrix[i,j]=score
					qualificationMatrix[j,i]=1/score
				if selection==candidates[j]:
					valid=1
					inverted=1
					score = float(raw_input('How many times better is ' + candidates[j] + ' compared to ' + candidates[i] +' with regards to '+ criteria+'?>>'))
					qualificationMatrix[i,j]=1/score
					qualificationMatrix[j,i]=score

			
	n=len(candidates)			
	#print(qualificationMatrix)
	eigens=LA.eigvals(qualificationMatrix)
	#print(eigens)
	#print(max(eigens))
	#print(np.absolute(max(eigens)))
	CI = (np.absolute(max(eigens))-float(n))/(float(n)-1)
	#print(CI)
	CR = 0;
	if n>10:
		RI=1.5
		CR=CI/RI*100
	elif n>2:
		RI=SaatyIndex[n-1]
		#print(RI)
		CR=CI/RI*100

	print('\n\r')
	print('Your inputs are ' + str(CR) +'% inconsistent')
	print('Your qualifications are:')

	w, v = LA.eig(qualificationMatrix)
	maxindex=np.argmax(w)
	preWeights=v[:,maxindex]
	weights=[]
	for i in range(0,n):
		weights.append(np.absolute(preWeights[i]))
	
	uniter=sum(weights)
	for i in range(0,n):
		weights[i]=weights[i]/uniter

	for i in range(0,n):
		print(candidates[i] + ' gets a score of ' + str(weights[i]) + ' for ' + criteria)
		
	qualificationWeights[contest-1:contest,0:numCandidates+1]=weights
	print(qualificationWeights)

qualificationWeights=np.transpose(qualificationWeights)

finalScores=qualificationWeights.dot(criteriaWeights)

for i in range(0,numCandidates):
	print(candidates[i] + ' gets a final score of ' + str(finalScores[i]))
