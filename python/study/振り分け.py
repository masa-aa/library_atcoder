import itertools
name=['masa_aa','cis_yuta','kazunami','garangara','hkr3686','Ranuma']
score=[0]*6
for i in range(6):
    l=list(map(int,input(name[i]+'の点数を新しい順に3つ入力 :').split()))
    if len(l)==3:
        score[i]=5*l[0]+3*l[1]+2*l[2]
    elif len(l)==2:
        score[i]=7*l[0]+3*l[1]
    else:
        score[i]=10*l[0]
Sum=sum(score)
team=[0]*3
Abs_score=10000000
for v in itertools.combinations(range(6),3):
    if abs(Sum-2*(score[v[0]]+score[v[1]]+score[v[2]]))<Abs_score:
        Abs_score=abs(Sum-2*(score[v[0]]+score[v[1]]+score[v[2]]))
        for i in range(3):
            team[i]=v[i]
teamA=[]
teamB=[]
for i in range(6):
    if i in team:
        teamA.append(name[i])
    else:
        teamB.append(name[i])
print('Aチームは',*teamA,sep=', ')
print('Bチームは',*teamB,sep=', ')
print('点数差は, ',Abs_score/10)
#22行目からはO(n)でできる。DPでもできそう