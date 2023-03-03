Exercise 1: Retrieving the protein sequence of human preproinsulin
The National Center for Biotechnology Information (NCBI) has information on many biological sequences.

Access NCBI at https://ncbi.nlm.nih.gov.

Next to the search bar, choose the dropdown menu and select Protein. Next, in the search bar, enter human insulin and choose Search.

Bonus: Cleaning preproinsulin-seq.txt programmatically
Cleaning source data files is a common task in computer programming. You could programmatically clean preproinsulin-seq.txt in several ways—for example, by using Bash, Python, or another programming language of choice. Try using regex to programmatically strip the file of ORIGIN, its numbers, the two slashes (//), spaces, and line breaks or return carriages. You could also confirm programmatically that the file has 110 characters.

Exercise 2: Obtaining the protein sequence of human insulin
Insulin is obtained from preproinsulin through a series of cut-and-paste procedures. Preproinsulin contains a 24aa signal sequence and an 86aa proinsulin molecule. Amino acids 25–54 and amino acids 90–110 are the processed insulin molecule. Use Python, Bash, or manual manipulation to retrieve only those amino acids in the sequence that compose insulin.

Manually or programmatically delete ORIGIN, 1, 61, //, and the spaces and return carriages.
In the file preproinsulin-seq-clean.txt, copy your results.

Confirm that your file has 110 characters of lowercase letters, which represent the amino acids in the sequence of human preproinsulin.


In lsinsulin-seq-clean.txt, save amino acids 1–24. Verify that your file has 24 characters.


In binsulin-seq-clean.txt, save amino acids 25–54. Verify that your file has 30 characters.


In cinsulin-seq-clean.txt, save amino acids 55–89. Verify that your file has 35 characters.


In ainsulin-seq-clean.txt, save amino acids 90–110. Verify that your file has 21 characters.
