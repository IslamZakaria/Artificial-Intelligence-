from  math import *

class item:
    def __init__(self, age, prescription, astigmatic, tearRate, needLense):
        self.age = age
        self.prescription = prescription
        self.astigmatic = astigmatic
        self.tearRate = tearRate
        self.needLense = needLense
def getDataset():
    data = []
    labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    data.append(item(0, 0, 0, 0,	labels[0]))
    data.append(item(0, 0, 0, 1,	labels[1]))
    data.append(item(0, 0, 1, 0,	labels[2]))
    data.append(item(0, 0, 1, 1,	labels[3]))
    data.append(item(0, 1, 0, 0,	labels[4]))
    data.append(item(0, 1, 0, 1,	labels[5]))
    data.append(item(0, 1, 1, 0,	labels[6]))
    data.append(item(0, 1, 1, 1,	labels[7]))
    data.append(item(1, 0, 0, 0,	labels[8]))
    data.append(item(1, 0, 0, 1,	labels[9]))
    data.append(item(1, 0, 1, 0,	labels[10]))
    data.append(item(1, 0, 1, 1,	labels[11]))
    data.append(item(1, 1, 0, 0,	labels[12]))
    data.append(item(1, 1, 0, 1,	labels[13]))
    data.append(item(1, 1, 1, 0,	labels[14]))
    data.append(item(1, 1, 1, 1,	labels[15]))
    data.append(item(1, 0, 0, 0,	labels[16]))
    data.append(item(1, 0, 0, 1,	labels[17]))
    data.append(item(1, 0, 1, 0,	labels[18]))
    data.append(item(1, 0, 1, 1,	labels[19]))
    data.append(item(1, 1, 0, 0,	labels[20]))

    return data
class Feature:
    def __init__(self, name):
        self.name = name
        self.visited = -1
        self.infoGain = -1
class ID3:
    def __init__(self, features):
        self.features = features
        self.dataset = getDataset()
    def genentropy(self,ds):
        mydataset=ds
        needed = 0
        for d in mydataset:
            needed += d.needLense
        neednot = mydataset.__len__()-needed
        generalentropy = -(needed/mydataset.__len__())*log((needed/mydataset.__len__()), 2)-(neednot/mydataset.__len__())*log((neednot/mydataset.__len__()), 2)
        return generalentropy
    def split (self,dtst,fname,val):
        redueced=[]
        normal=[]
        if fname=='tearRate':
            for d in dtst:
                if d.tearRate == 1:
                    redueced.append(d)
                elif d.tearRate == 0:
                    normal.append(d)
        elif fname=='age':
            for d in dtst:
                if d.age == 1:
                    redueced.append(d)
                elif d.age == 0:
                    normal.append(d)
        elif fname=='prescription':
            for d in dtst:
                if d.prescription == 1:
                    redueced.append(d)
                elif d.prescription == 0:
                    normal.append(d)
        elif fname=='astigmatic':
            for d in dtst:
                if d.astigmatic == 1:
                    redueced.append(d)
                elif d.astigmatic == 0:
                    normal.append(d)
        mydata=[]
        mydata.append(redueced)
        mydata.append(normal)
        if val ==1:
            return redueced
        elif val ==0:
            return normal
        return mydata
    def infogain(self,ds,fname):
        re=self.split(ds,fname,3)
        dtst=ds
        redueced = re[0]
        normal = re[1]
        red_need = 0
        for x in redueced:
            red_need += x.needLense
        red_notneed=redueced.__len__()-red_need
        y=redueced.__len__()/dtst.__len__()
        if redueced.__len__()!=0:
            if red_need==0 :
                reduced_entropy1 = - (red_notneed / redueced.__len__()) * log((red_notneed / redueced.__len__()), 2)
            elif red_notneed==0 :
                reduced_entropy1 = -(red_need / redueced.__len__()) * log((red_need / redueced.__len__()), 2)
            else:
                reduced_entropy1 = -(red_need / redueced.__len__()) * log((red_need / redueced.__len__()), 2) - (red_notneed / redueced.__len__()) * log((red_notneed / redueced.__len__()), 2)
        else:
            reduced_entropy1=0
        nor_need = 0
        for x in normal:
            nor_need += x.needLense
        nor_notneed = normal.__len__() - nor_need
        xx=normal.__len__()/dtst.__len__()
        if normal.__len__()!=0:
            if nor_need == 0:
                normal_entropy = - (nor_notneed / normal.__len__()) * log((nor_notneed / normal.__len__()), 2)
            elif nor_notneed == 0:
                normal_entropy = -(nor_need / normal.__len__()) * log((nor_need / normal.__len__()), 2)
            else:
                normal_entropy = -(nor_need/normal.__len__())*log((nor_need/normal.__len__()),2)-(nor_notneed/normal.__len__())*log((nor_notneed /normal.__len__()),2)
        else:
            normal_entropy=0
        tot=self.genentropy(ds)
        tear_ig=tot-(y*reduced_entropy1)-(xx*normal_entropy)
        for a in self.features:
            if a.name == fname:
                a.infoGain=tear_ig
        return tear_ig
    def pure (self,chedata):
        zerocounter=0
        onecounter=0
        for ea in chedata:
            if ea.needLense ==1:
                onecounter+=1
            elif ea.needLense==0:
                zerocounter+=1
            if zerocounter > 0 and onecounter >0 :
                return 0
        if onecounter>0:
            return 2
        elif zerocounter>0:
            return 1
    def max_info(self):
        max=Feature('ret')
        for elem in self.features :
            if max.infoGain<elem.infoGain and elem.visited==-1:
                max = elem
        return max
    def classify(self,input):
        ds=self.dataset
        for c in self.features:
            if c.visited ==-1:
                self.infogain(ds,c.name)
        max_ig=self.max_info()
        index=-1
        if max_ig.name=='age':
            index=0
        elif max_ig.name=='prescription':
            index=1
        elif max_ig.name == 'astigmatic':
            index=2
        elif max_ig.name == 'tearRate':
            index=3
        if index==-1:
            count1=0
            count0=0
            for el in ds:
                if el.needLense==0:
                    count0+=1
                else:
                    count1+=1
            if count1>count0:
                return 1
            return 0

        ndata=self.split(ds,max_ig.name,input[index])
        p=self.pure(ndata)
        if p !=0 :
            p-=1
            for c in self.features:
                c.visited=-1
            self.dataset = getDataset()
            return p
        for k in self.features:
            if k.name == max_ig.name:
                k.visited=0
        self.dataset=ndata
        return self.classify(input)

dataset = getDataset()
features = [Feature('age'), Feature('prescription'), Feature('astigmatic'), Feature('tearRate')]
id3 = ID3(features)
cls = id3.classify([0, 0, 1, 1])
print('testcase 1: ', cls)
cls = id3.classify([1, 1, 0, 0])
print('testcase 2: ', cls)
cls = id3.classify([1, 1, 1, 0])
print('testcase 3: ', cls)
cls = id3.classify([1, 1, 0, 1])
print('testcase 4: ', cls)