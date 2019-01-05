from collections import defaultdict
def test():
    sum = []
    sum.append(1+2+3+4)
    print(max(sum))
    
def checkMagazine_1(magazine, note):
    magSet = set(magazine.split(" "));
    found = True
    for w in note.split(" "):
        if w.strip() not in magSet:
            found = False
            break
        else:
            magSet.remove(w)
    if found:
        print('Yes')
    else:
        print('No')
        
def checkMagazine(magazine, note):
    found = True;
    mag = defaultdict(int)
    for m in magazine:
        mag[m] += 1
    for n in note:
        if (mag.get(n) is not None) and (mag.get(n) > 0):
            mag[n] -= 1
        else:
            found = False
            break
            
    print(mag)
    if found:
        print('Yes')
    else:
        print('No')
        
def twoStrings_1(s1, s2):
    wrd = [0]*26
    for w in s1:
       wrd[ord('a') - ord(w)] += 1
    for w1 in s2:
        if  wrd[ord('a') - ord(w1)] > 0:
            return 'YES'
    return 'NO'

def twoStrings(s1, s2):
    w1 = list(set(s1.strip()))
    w2 = list(set(s2.strip()))
    print(w1)
    print(w2)
    print(set(w1+w2))
    print(w1+w2)
    return 'YES' if len(set(w1+w2)) < len(w1+w2) else 'NO'
if __name__ == '__main__':
    #checkMagazine("ive got a lovely bunch of coconuts".split(" "), "ive got  coconuts".split(" "))
    twoStrings('hello', 'bakp')
    