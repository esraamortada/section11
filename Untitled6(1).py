#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pyopenms


# In[ ]:


import pyopenms
help(pyopenms.Constants)
print("avogadros number is",pyopenms.Constants,AVOGADRO)


# In[ ]:


from pyopenms import*
edb =ElementDB()

edb.hasElement("O")
edb.hasElement("S")

oxygen = edb.getElement("O")
print(oxygen.getName())
print(oxygen.getSymbol())
print(oxygen.getMonoWeight())
print(oxgyen.getAverageWeight())

sulfur = edb.getElement("S")
print(sulfur.getName())
print(sulfur.getSymbol())
print(sulfur.getMonoWeight())
print(sulfur,getAverageWeight())
isotopes = sulfur.getIsotopeDistribution()

print("one mole of oxgyen weighs",2*oxygen.getAverageWeight(),"grams")
print("one mole of 1602 weighs",2*oxgyen.getMonoWeight(),"grams")


# In[ ]:


edb = ElementDB()
oxgyen_isoDict = {"mass":[],"abundance":[]}
sulfur_isoDict = {"mass":[],"abundance":[]}

oxgyen = edb.getElement("O")
isotopes = oxygen.getIsotopeDistribution()
for iso in isotopes.getContainer():
    print("oxygen isotope",iso.getMZ(),"has abundance",iso.getIntensity()*100,"%")
    oxygen_isoDist["mass"].append(iso.getMZ())
    oxygen_isoDist["abundance"].append((iso.getIntensity() * 100))


sulfur= edb.getElement("S")
isotopes = sulfur.getIsotopeDistribution()
for iso in isotopes.getContainer():
    print("sulfur isoptope", iso.getMZ(),"hasabundance",iso.getIntensity()*100, "%")
    sulfur_isoDist["mass"].append(iso.getMZ())
    sulfur_isoDist["abundance"].append((iso.getIntentsity() * 100 ))
    


# In[ ]:


import math
from matplotib import pyplot as plt

def adjustText(x1,y1,x2,y2):
    if y1 > y2:
        plt.annotate('%0.3f'%(y2), xy=(x2,y2), xytext=(x2+0.5,y2+9)),textcoords='data',arrowprops=dict(arrowstyle="->",color='r', lw=0.5),horizontalignment='right',verticalalignment='top')
        else:
        plt.annotate('%0.3f'%(y1),xy=(x1,y1), xytext=(x1+0.5,y1+9)),textcoords='data',arrowprops=dict(arrowstyle="->",color='r', lw=0.5),horizontalignment='right',verticalalignment='top')
        
        
def plotDistribution(distribution):
    n = len(distrribution["mass"])
    for i in range(0, n):
        plt.vlines(x=distribution["mass"][i], ymin=0, ymax=distribution["abundance"][i])
        if int(distribution["mass"][i - 1])== int(distribution["mass"][i]) \ and i != 0:
            adjustText(distribution["mass"][i - 1], distribution["abundance"][i - 1], distribution["mass"][i], distribution["abundance"][i])
        else:
            plt.text(x=distribution["mass"][i],y=distribution["abundance"][i] + 2),s='%0.3f' % (distribution["abundance"][i]), va='center', ha='center')
    plt.ylim([0,110])
    plt.xticks(range(math.ceil(distribution["mass"][0]) - 2, math.ceil(distribution["mass"][-1]) + 2))
    
plt.figure(figsize=(10,7))

plt.subplot(1,2,1)
plt.title("isotopic distribution of oxygen")
plotDistribution(oxygen_isoDist)
plt.xlabel("atomic mass (u)")
plt.ylabel("relative adundance (%)")

plt.subplot(1,2,2)
plt.title("isotopic distribution of sulfur")
plotDistribution(sulfur_isoDist)
plt.xlabel("atomic mass (u)")
plt.ylabel("relative adundance (%)")

plt.show()


        


# In[ ]:


edb = ElementDB()
isotopes = edb.getElement("c").getIsotopeDistribution().getContainer()
carbon_isotope_difference = isotopes[1].getMZ() - isotopes[0].getMZ()
isotopes = edb.getElement("n").getIsotopeDistribution().getContainer()
nitrogen_isotope_difference = isotopes[1].getMZ() - isotopes[0].getMZ()

print ("mass difference between 12c and 13c :", carbon_isotope_difference)
print ("mass difference between 14n and 15n :", nitrogen_isotope_difference)
print ("relative deviation:",100*(carbon_isotope_difference - nitrogen_isotope_difference)/carbon_isotope_difference, "%")


# In[ ]:





# In[ ]:


from pyopenms.Constants import *

helium = ElementDB().getElement("he")
isotopes = helium.getIsotopeDistribution()

mass_sum = 2*PROTON_MASS_U + 2*ELECTRON_MASS_U + 2*NEUTRON_MASS_U
helium4 = isotopes.getContainer()[1].getMZ()
print ("sum of masses of 2 protons, neutrons and electrons:", mass_sum)
print ("mass of he4:", helium4)
print ("difference between the two masses:", 100*(mass_sum - helium4)/mass_sum, "%")



# In[ ]:


methanol = Empiricalformula("CH3OH")
water = Empiricalformula("H2o")
ethanol = Empiricalformula("CH2") + methanol
print("ethanol chemical formula:", ethanol.toString())
print("ethanol composition:",ethanol.getElementalComposition())
print("ethanol has",ethanol.getElementalComposition()[b"H"], "hydrogen atoms")


# In[1]:


methanol = Empiricalformula("CH3OH")
ethanol = Empiricalformula("CH2") + methanol

methanol_isoDist = {"mass": [], "abundance": []}
ethanol_isoDist = {"mass": [], "abundance": []}

print("coarse isotope distribution:")
isotopes = ethanol.getIsotopeDistribution( coarseIsotopePatternGenerator(4))
prob_sum = sum([iso.getIntensity() for iso in isotopes.getContainer()])
print("this covers", prob_sum, "probability")
for iso in isotopes.geytContainer():
    print("isotope", iso.getMZ(), "has abundance", iso.getIntensity()*100, "%")
    methanol_isoDist["mass"].append(iso.getMZ())
    methanol_isoDist["abundance"].append((iso.getIntensity()*100))
    
print("fine isotope distribution:")
isotopes = ethanol.getIsotopeDistribution( FineIsotopePatternGenerator(le-3))
prob_sum = sum([iso.getIntensity() for iso in isotopes.getContainer()])
print("this covers", prob_sum, "probability")
for iso in isotopes.geytContainer():
    print("isotope", iso.getMZ(), "has abundance", iso.getIntensity()*100, "%")
    ethanol_isoDist["mass"].append(iso.getMZ())
    ethanol_isoDist["abundance"].append((iso.getIntensity()*100))


# In[ ]:


plt.figure(figsize=(10,7))

plt.subplot(1,2,1)
plt.title("Isotopic distribution of methanol")
plotDistribution(methanol_isoDist)
plt.xlabel("atomic mass (u)")
plt.ylabel("relative abundance (%)")

plt.subplot(1,2,2)
plt.title("Isotopic distribution of ethanol")
plotDistribution(ethanol_isoDist)
plt.xlabel("atomic mass (u)")
plt.ylabel("relative abundance (%)")

plt.savefig("methanol_ethanol_isoDistribution.png")


# In[ ]:


methanol = EmpiricalFormula("CH3OH")
ethanol = EmpiricalFormula("Ch2") + methanol

print("fine isotope distribution:")
isotopes = ethanol.getIsotopeDistribution( FineIsotopePatternGenerator(le-6) )
prob_sum = sum([iso.getIntensity() for iso in isotopes.getContainer()])
print("this covers",prob_sum, "probability")
for iso in isotopes.getContainer():
    print("isotope",iso.getMZ(), "has abundance", iso.getIntensity()*100, "%")


# In[ ]:


isotope = ethanol.getIsotopeDistribution( coarseIsotopePatternGenerator(5, True) )
for iso in isotopes.getContainer():
    print ("isotope", iso.getMZ(), "has abundance", iso.getIntensity()*100, "%")


# In[4]:


lys = ResidueDB().getResidue("Lysine")
print(lys.getName())
print(lys.getThreeLetterCode())
print(lys.getOneLetterCode())
print(lys.getAverageWeight())
print(lys.getMonoWeight())
print(lys.getPka())
print(lys.getFormula().toString())


# In[ ]:


isotopes = ox.getDiffFormula().getIsotopeDistribution(CoarseIsoPatternGenerator(5))
for iso in isotopes.getContainer():
    print(iso.getMZ(), ":", iso.getIntensity())


# In[ ]:


uridine = RibonucleotideDB().getRibonucleotide(b"U")
Print(uridine.getName())
print(uridine.getCode())
print(uridine.getAvgMass())
print(uridine.getMonoMass())
print(uridine.getFormula().toString())
print(uridine.isModified())
methyladenosine = RibonucleotideDB().getRibonucleotide(b"m1A")
print(methyladenosine.getName())
print(methyladenosine.isModified())

