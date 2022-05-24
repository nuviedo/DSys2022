import numpy as np
import matplotlib.pyplot as plt
import scipy,scipy.optimize

Data_OW={
    (1999-1999):96776439*.179,
    (2006-1999):106789067*.202,
    (2012-1999):116489125*.186,
    (2018-1999):125489863*.180,
    (2020-1999):128257849*.196,
}
Data_OB={
    (1999-1999):96776439*.09,
    (2006-1999):106789067*.146,
    (2012-1999):116489125*.146,
    (2018-1999):125489863*.175,
    (2020-1999):128257849*.186,
}

Data_BO={i:Data_OW[i]+Data_OB[i] for i in Data_OW.keys()}

fig,ax=plt.subplots() 

P0=0
#dp/dt = 
def P(t,r,K):
    global P0
    return K/(1+((K-P0)/P0) * np.exp(-r*t) )

i=0
colors=[(.8,0,0,.7),(0,.8,0,.7),(0,0,.8,.7)]
for D in [Data_OW,Data_OB,Data_BO]:
    i+=1
    P0=D[0]
    lab=(["OW","OB","BO"])[i-1]
    ax.scatter(np.array(list(D.keys()))+1999,list(D.values()),label=lab,color=colors[i-1])
    X=np.array(list(D.keys()))
    Y=np.array(list(D.values()))
    Sol=scipy.optimize.curve_fit(P,X,Y,p0=[1,D[0]])[0]
    
    XTEND=X.tolist()+[list(D.keys())[-1]+i*6 for i in range(1,10)]
    ypred=[P(x,Sol[0],Sol[1]) for x in XTEND]
    print(lab)
    for j in range(len(ypred)):
        print(XTEND[j]+1999,ypred[j])
        
    XTEND=np.array(XTEND)+1999
    ax.scatter(XTEND,ypred,s=5,color=colors[i-1])
    ax.plot(XTEND,ypred,linewidth=.5,color=colors[i-1])

ax.legend()
plt.savefig("weightpopulation.png")
plt.show()
