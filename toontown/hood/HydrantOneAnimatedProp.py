# 2013.08.22 22:20:54 Pacific Daylight Time
# Embedded file name: toontown.hood.HydrantOneAnimatedProp
from toontown.hood import ZeroAnimatedProp
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal

class HydrantOneAnimatedProp(ZeroAnimatedProp.ZeroAnimatedProp):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('HydrantOneAnimatedProp')
    PauseTimeMult = base.config.GetFloat('zero-pause-mult', 1.0)
    PhaseInfo = {0: ('tt_a_ara_ttc_hydrant_firstMoveArmUp1', 40 * PauseTimeMult),
     1: ('tt_a_ara_ttc_hydrant_firstMoveStruggle', 20 * PauseTimeMult),
     2: ('tt_a_ara_ttc_hydrant_firstMoveArmUp2', 10 * PauseTimeMult),
     3: ('tt_a_ara_ttc_hydrant_firstMoveJump', 8 * PauseTimeMult),
     4: ('tt_a_ara_ttc_hydrant_firstMoveJumpBalance', 6 * PauseTimeMult),
     5: ('tt_a_ara_ttc_hydrant_firstMoveArmUp3', 4 * PauseTimeMult),
     6: ('tt_a_ara_ttc_hydrant_firstMoveJumpSpin', 2 * PauseTimeMult)}
    PhaseWeStartAnimating = 3

    def __init__(self, node):
        ZeroAnimatedProp.ZeroAnimatedProp.__init__(self, node, 'hydrant', self.PhaseInfo, ToontownGlobals.HYDRANT_ZERO_HOLIDAY)

    def startIfNeeded(self):
        try:
            self.curPhase = self.getPhaseToRun()
            if self.curPhase >= self.PhaseWeStartAnimating:
                self.request('DoAnim')
        except:
            pass

    def handleNewPhase(self, newPhase):
        if newPhase < self.PhaseWeStartAnimating:
            self.request('Off')
        else:
            self.startIfNeeded()
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\hood\HydrantOneAnimatedProp.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:20:54 Pacific Daylight Time
