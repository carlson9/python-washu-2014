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
    
