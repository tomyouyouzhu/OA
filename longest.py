# A list for saving the length of each byte. The length of L should be the number of files. The usage is for tracking which file the byte is from.
L = []

# A list for saving all lengthes of bytes. The usage of it is finding the max length.
S = []

# Load files. This part could be modfied for loading different names. Time complexity: O(n). Space complexity: O(n)
for i in range(1, 11):
    name = "sample." + str(i)
    f = open(name, 'rb')
    a = []
    for line in f:
        a.append(len(line))
        S.append(len(line))
    f.close()
    L.append(a)
    
# Soring S from max to min and saving the first one (max one). Time complexity: O(n log(n). Space complexity: O(n)
S.sort()
S.reverse()
for i in range(0, len(S)-1):
    if S[i] == S[i+1]:
        m = S[i]
        break
    
# A list for output or returnning. 
M = []

# Loop L to find where is the max length and save its information. Time complexity: O(n). Space complexity: O(n)
for i in range(0, 10):
    l = 0
    for j in range(0, len(L[i])):
        if L[i][j] == m:
            M.append(("sample." + str(i+1), l))
        l = l + L[i][j]
        
# Output or return.
print ("The longest length is ", m, " in ", M)

"""
#test
v = []
q = open("sample.2", 'rb')
for line in q:
    v.append(line)
q.close()
index = 0
for x in v:
    print (index, x)
    index += len(x)
"""
    
"""
Thre reuqirment:
- the length of the strand
- the file names where the largest strand appears
- the offset where the strand appears in each file

Explaination :
1. Finding the max length. (Do not need to show the byte.) 
2. Which file.
3. Where in the file. 
So, we do not need to read the content of files. Saving length of each byte is enough, but we need to keep tracking filenames for output or return.

The most time compleity is O(n), and the most space complexity is O(n). 
Because we need to read all files and keep tracking them, so the time complexity and space complexity should be fine.
No library used.
"""
