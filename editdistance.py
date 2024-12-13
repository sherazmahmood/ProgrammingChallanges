'''
Edit Distance Problem: (Levenshtein Distance)

Calculate the minimum number of operations needed to transform one string into anotehr using:
- Insertion (add a character)
- Deletion (remove a character)
- Substitution (Replace one character)

Each operation has a cost of 1
'''

def editDistanceProblem(s1,s2):
    memo=[] #use a memoization table
    for i in range(len(s1)):
        for j in range(len(s2)):
            print(f'{s1[i]}={s2[j]}')
            if s1[i]==s2[j]: # same character do not need to insert
    return 0

test_cases = [
    ['GEEXSFRGEEKKS','GEEKSFORGEEKS',3],
    ['geek','gesek',1],
    ['cat','cut',1],
    ['sunday','saturday',3]
]

# iterate through test cases
for test in test_cases:
    result = editDistanceProblem(test[0],test[1])
    assert result==test[2],f'Edit Distance: ({test[0]}) -> ({test[1]}) expected {test[2]} got {result}'