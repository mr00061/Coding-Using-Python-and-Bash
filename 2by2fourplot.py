#Code By Mohammad Rahman, Chemistry, West Virginia University
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
def dataprocess(dt1, dt2, dt3, dt4, imagefilename):
    file=imagefilename
    dt1=open(dt1)
    dt1 = dt1.read()
    dt1=dt1.split('\n')
    dt2=open(dt2)
    dt2 = dt2.read()
    dt2=dt2.split('\n')
    dt3=open(dt3)
    dt3 = dt3.read()
    dt3=dt3.split('\n')
    dt4=open(dt4)
    dt4 = dt4.read()
    dt4=dt4.split('\n')
    d1=[]
    d2=[]
    d3=[]
    d4=[]
    res1=[]
    #out=open(filename, 'a')
    #outhdx=open(datafile, 'a')
    for i in dt1:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d1.append(x)
    for i in dt2:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d2.append(x)
    for i in dt3:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d3.append(x)
    for i in dt4:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d4.append(x)

    d1.pop()
    d2.pop()
    d3.pop()
    d4.pop()
    d1_in=np.array(d1)
    d2_in=np.array(d2)
    d3_in=np.array(d3)
    d4_in=np.array(d4)
    x1=d1_in[:,0]
    x2=d2_in[:,0]
    x3=d3_in[:,0]
    x4=d4_in[:,0]
    y1=d1_in[:,1]
    y2=d2_in[:,1]
    y3=d3_in[:,1]
    y4=d4_in[:,1]
    x1=np.array(x1)
    x2=np.array(x2)
    x3=np.array(x3)
    x4=np.array(x4)
    y1=np.array(y1)
    y2=np.array(y2)
    y3=np.array(y3)
    y4=np.array(y4)
    plot4(x1, x2, x3, x4, y1, y2, y3, y4,file)
    

def plot4(x1, x2, x3, x4, m1, m2, m3, m4,file):
    import matplotlib
    fig, axs = plt.subplots(2, 2, sharex=False, sharey=False,figsize=(10, 8))
    axs[0, 0].plot(x1, y1, ls='--', lw=2, color='black', marker='^')
    axs[0, 1].plot(x2, y2, ls='--', lw=2, color='blue', marker='o')
    axs[1, 0].plot(x3, y3,ls='--', lw=2, color='red', marker='+')
    axs[1, 1].plot(x4, y4 ls='--', lw=2, color='brown', marker='*')
    axs[0, 0].set_ylabel('Y', fontsize=11)
    axs[0, 0].set_xlabel('X', fontsize=11)
    axs[0, 0].set_title('A', fontsize=11, loc='right')
    resolution=1200
    plt.savefig("file", format="png", dpi=resolution)
    

#Self test your code and where you will write code where you can
#purge your data from bash shell to python script generate plot
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 6:
        print
        print("usage: python 2by2fourplot.py file1 file2 file3 file4 imagefilename")
        print("[1] Datafile from intrinsic rate")
        print("[2] Data filename from MD analysis")
        print("[3] Write filename for HDx contribution per residue")
        print("[3] write datafile for individual for statistical calculation")
        sys.exit()
    else:
        dt1 = sys.argv[1]
        dt2 = sys.argv[2]
        dt3 = sys.argv[3]
        dt4 = sys.argv[4]
        imagefile=sys.argv[5]
        dataprocess(dt1, dt2, dt3, dt4, imagefilename)



