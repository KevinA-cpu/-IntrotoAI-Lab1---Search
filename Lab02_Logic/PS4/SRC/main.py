from copy import deepcopy

ALPHA = []
KB = []
newClauses = []
numberOfResolventPerLoop = []

def readFile(filename):
    global ALPHA
    global KB
    
    file = open(filename, 'r')
    
    ALPHA = file.readline().rstrip().split(' OR ')
    numberOfKBClause = int(file.readline()) 
    KB = [file.readline().rstrip().split(' OR ') for _ in range(numberOfKBClause)]
    
    file.close()

def writeFile(filename, solution):
    global newClauses  
    
    file = open(filename, 'w')
    
    clausePos = 0
    Max = 0
    for number in numberOfResolventPerLoop:
        file.write(str(number))
        file.write('\n')
        Max =  Max + number
        for i in range(clausePos, Max):
            if (newClauses[i] == []):
                file.write('{}')  
            else:    
                file.write(" OR ".join(newClauses[i]))
            file.write('\n')
        clausePos = clausePos + number
        
    if solution:
        file.write("YES")
    else:
        file.write("NO")
        
    file.close()

def isComplementary(Ci, Cj):
    return Ci[-1] == Cj[-1] and ('-' + Ci == Cj or Ci == '-' + Cj)

def alphaNegation(clause):
    temp = []
    for literal in clause:
        if literal[0] == '-':
            temp.append(literal[1])
        else:
            temp.append('-' + literal)
    return temp;

def isUselessResolvent(resolvent):
    for i in range(len(resolvent)):
        for j in range(i+1, len(resolvent)):
            if resolvent[i] == resolvent[j] or isComplementary(resolvent[i], resolvent[j]):
                return True
    return False

def sortResolve(resolve):
    temp = []
    length = len(resolve)
    for i in range(length):
        if (resolve[i][0] == '-'):
            temp.append(resolve[i]);
            resolve[i] = resolve[i][1]     
            
    resolve.sort()
    
    for i in temp:
        for j in range(length):
            if ('-' + resolve[j]) == i:
                resolve[j] = '-' + resolve[j];
                break;           
    return resolve

def appendNumberOfResolventPerLoop(numberOfResolventPerLoop):
    if len(numberOfResolventPerLoop) == 0:
        numberOfResolventPerLoop.append(len(newClauses))
    else:
        numberOfResolventPerLoop.append(len(newClauses) - sum(numberOfResolventPerLoop))
 
def appendNewClauses(clauses, newClauses, resolvents):
    for resolvent in resolvents:
        checkResolvent = isUselessResolvent(resolvent)
        if checkResolvent:
            break;
                    
        resolvent = sortResolve(resolvent)
        if resolvent not in clauses and resolvent not in newClauses:
            newClauses.append(resolvent)
    
def resolutionMainLoop(clauses):
    global numberOfResolventPerLoop
    global newClauses
    while True:
        for i in range(len(clauses)):
            for j in range(i+1,len(clauses)):
                resolvents = pl_resolve(clauses[i], clauses[j])
               
                # resolvents where -B resovle B = []
                if [] in resolvents:
                    newClauses.append([])
                    appendNumberOfResolventPerLoop(numberOfResolventPerLoop)
                    return True;
        
                appendNewClauses(clauses, newClauses, resolvents)
                
        appendNumberOfResolventPerLoop(numberOfResolventPerLoop)
        
        #no new resolvent appear
        if 0 in numberOfResolventPerLoop:
            return False
        
        for resolvent in newClauses:
            if resolvent not in clauses:
                clauses.append(resolvent)
        
    
def pl_resolution():
    negativeAlpha = alphaNegation(ALPHA)
    clauses = deepcopy(KB)

    for literal in negativeAlpha:
        if literal not in clauses:
            clauses.append([literal])
            
    return resolutionMainLoop(clauses)
    
def pl_resolve(Ci, Cj):
    resolvents = []
    for i in range(len(Ci)):
        for j in range(len(Cj)):
            if isComplementary(Ci[i], Cj[j]):
                temp1 = deepcopy(Ci)
                temp2 = deepcopy(Cj)
                del temp1[i]
                del temp2[j]
                resolvents.append(temp1 + temp2)
    return resolvents

FILENAME = ["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"]

if __name__ == '__main__':
    # enter "1.txt", "2.txt",... only
    for fileName in FILENAME:
        readFile('INPUT/' + fileName)
        solution = pl_resolution()
        writeFile('OUTPUT/' + fileName, solution)
        ALPHA.clear()
        KB.clear()
        newClauses.clear()
        numberOfResolventPerLoop.clear()
    