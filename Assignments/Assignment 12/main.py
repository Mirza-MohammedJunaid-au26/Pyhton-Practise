# Q-1 ) Design Tiny Url and explain all the steps and estimations.

"""

URL : https://university.attainu.com:80/dashboard/index.html?key1=value1&key2=value2
     |_____| |_____________________||_| |__________________| |_____________________|
        |               |            |           |                     |
     Scheme        Domain Name     Port    Path to the File        Parameters


1. Scheme :
-> The first part of the URL is the scheme, which indicates the protocol that the browser must use to request
-> Usually for websites the protocol is HTTPS or HTTP (its unsecured version). 

2. Authority :
-> Next follows the authority, which is separated from the scheme by the character pattern ://. If present the authority includes both the domain 
(e.g. www.university,attainu.com) and the port (80), separated by a colon:

3. Path to Resource :
-> /dashboard/index.html is the path to the resource on the Web server. In the early days of the Web, a path like this represented a physical file location on the Web server. Nowadays, it is mostly an abstraction handled by Web servers without any physical reality.

4. Parameters :
-> ?key1=value1&key2=value2 are extra parameters provided to the Web server. Those parameters are a list of key/value pairs separated with the & symbol.

"""

# Q-2)

def firstUniqChar(s):        
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1

str = "aabb"
print(firstUniqChar(str)) 


# Q.3)

import collections

def predictPartyVictory(senate):
    n = len(senate)
    qr = collections.deque([i for i, c in enumerate(senate) if c == "R"])
    qd = collections.deque([i for i, c in enumerate(senate) if c == "D"])
    while qr and qd:
        if qr[0] < qd[0]:
            qd.popleft()
            qr.append(qr.popleft() + n)
        else:
            qr.popleft()
            qd.append(qd.popleft() + n)
    return "Radiant" if qr else "Dire"

senate = "RD"
print(predictPartyVictory(senate))
senate = "RDD"
print(predictPartyVictory(senate))