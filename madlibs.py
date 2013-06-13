import random
import re


print" Madlibs - by surya "
print"---------------------"

noun=['cat','sachin','apple','gorrila','DeltaTeam','persons']
verb=['eat','sleep','drink','kill','program','fly']
number=['5','100','Infinite']
adjective=['fat','thin','intelligent','foolish','white']



s1="adjective,noun,adjective,verb,adjective,noun,verb,$a p1 p2 should be p3 to p4 p5 p6 and p7 p6" 
s2="verb,noun,number,noun$p2 was able to p1 p3 p4"
s3="noun,adjective$p1 is p2" 
s4="noun,verb,noun$p1 can p2 p3"
s5="adjective,noun,verb,adjective,noun$a p1 p2 can p3 a p4 p5 to make the p5 p1"
s6="noun,verb,noun,noun,noun,adjective$Delta is an p6 group of p1 who are responsible to p2 p3 , p4 and p5 "
#
#
#
#
#

sentences=[s1,s2,s3,s4,s5,s6]
def game():
    print"New Sentence "
    print"-------------"
    sel_sen=random.choice(sentences)
    s=sel_sen.split('$')
    parts=s[0]
    parts=parts.split(',')
    madlib=s[1]
    usrinp=input(" (1)Random words or (2)User words ? ")-1
    
    t=re.findall(r"\bp\d\b",madlib)
    for i in t:
        if usrinp:
            x=raw_input("Enter a "+parts[int(int(i[1])-1)]+" : ")
        else :
            v=parts[int(int(i[1])-1)]
            if v=='noun':
                req=noun
            elif v=='verb':
                req=verb
            elif v=='number':
                req=number
            elif v=='adjective':
                req=adjective
            x=random.choice(req)
        madlib=madlib.replace(i,x)
    print "---"
    print madlib
    print "---"
game()       
while input("Exit(1) or Continue(2)")-1 :
    game()
