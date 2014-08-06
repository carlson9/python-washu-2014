<<<<<<< HEAD
<<<<<<< HEAD
#file = open('words.txt')

#for line in file:
#  word = line.strip()
#  print word
 
def has_no_e(word):
    return not 'e' in word
    
def uses_only(word1,word2):
    for i in range(len(word1)):
        if not word1[i] in word2: return False
    return True

def uses_all(word1, word2):
    for i in range(len(word2)):
        if not word2[i] in word1: return False
    return True

def is_abecedarian(word):
    return ''.join(sorted(word))==word
    
=======
=======
>>>>>>> upstream/master
file = open('words.txt')

for line in file:
  word = line.strip()
<<<<<<< HEAD
  print word
>>>>>>> 800df7bcaa57e0935c0836f1f49de6407c55c212
=======
  print word
>>>>>>> upstream/master
