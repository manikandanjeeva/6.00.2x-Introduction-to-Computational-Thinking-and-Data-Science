# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials):
    
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO
    
    numSteps_01 = 300 
    numSteps_02 = 150 
    numList = []
    numRList = []
    #tVxAxis = []
    histList = []
    histRList = []

    
    for trials in range(numTrials):
        
        rViruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses)]
        tPatient = TreatedPatient(rViruses[:], maxPop)

        tVPop = []
        tVRPop = []
                
        for i in range(numSteps_01):
            tPatient.update()
            tVPop.append(tPatient.getTotalPop())
            tVRPop.append(tPatient.getResistPop(['guttagonol']))
            
        tPatient.addPrescription('guttagonol')
        
        for i in range(numSteps_02):
            tPatient.update()
            tVPop.append(tPatient.getTotalPop())
            tVRPop.append(tPatient.getResistPop(['guttagonol']))
        
        numList.append(tVPop)
        numRList.append(tVRPop)
        
        
    for j in range(numTrials):
            histList.append(numList[j][ numSteps_01 + numSteps_02 - 1])
            histRList.append(numRList[j][ numSteps_01 + numSteps_02 - 1])
        
    pylab.figure(1)
    pylab.hist(histList , bins= 20, label = '300 Histogram')
    #pylab.hist(tVxAxis, avgRList)
    pylab.xlabel('Total virus population')
    pylab.ylabel('Number of trials')
    pylab.title('300 Step simulation')
    pylab.legend(loc = 'upper right')
    pylab.show()


#simulationDelayedTreatment(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials)
simulationDelayedTreatment(100, 1000, 0.1, 0.05, {'guttagonol':False}, 0.005, 10)




#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
