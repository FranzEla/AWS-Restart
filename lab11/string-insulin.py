# Store the human preproinsulin sequence in a variable called preproinsulin:

#preproInsulin = "C:/Users/dci-student/Desktop/Restart/lab10-insulin-sequences/preproinsulin-seq-clean.txt"

preproInsulin = "./lab10-insulin-sequences/preproinsulin-seq-clean.txt"
with open(preproInsulin, "r") as f:
    preproInsulin = f.read()
print("\n", preproInsulin, "\n")

lsInsulin = "./lab10-insulin-sequences/Isinsulin-seq-clean.txt"
with open(lsInsulin, "r") as f:
    lsInsulin = f.read()
print("ls Insulin is:", lsInsulin)

bInsulin = "./lab10-insulin-sequences/binsulin-seq-clean.txt"
with open(bInsulin, "r") as f:
    bInsulin = f.read()
print("b Insulin is:",bInsulin)

aInsulin = "./lab10-insulin-sequences/ainsulin-seq-clean.txt"
with open(aInsulin, "r") as f:
    aInsulin = f.read()
print("a Insulin is:",aInsulin)

cInsulin = "./lab10-insulin-sequences/cinsulin-seq-clean.txt"
with open(cInsulin, "r") as f:
    cInsulin = f.read()
print("c Insulin is:",cInsulin, "\n")

insulin = bInsulin + aInsulin

# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")
print(preproInsulin, "\n")

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T','V', 'W', 'Y']})  

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))


molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))