# 2013.08.22 22:18:49 Pacific Daylight Time
# Embedded file name: toontown.coghq.DistributedMintBattle
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleBase import *
from toontown.coghq import DistributedLevelBattle
from direct.directnotify import DirectNotifyGlobal
from toontown.toon import TTEmote
from otp.avatar import Emote
from toontown.battle import SuitBattleGlobals
import random
from toontown.suit import SuitDNA
from direct.fsm import State
from direct.fsm import ClassicFSM, State
from toontown.toonbase import ToontownGlobals

class DistributedMintBattle(DistributedLevelBattle.DistributedLevelBattle):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMintBattle')

    def __init__(self, cr):
        DistributedLevelBattle.DistributedLevelBattle.__init__(self, cr)
        self.fsm.addState(State.State('MintReward', self.enterMintReward, self.exitMintReward, ['Resume']))
        offState = self.fsm.getStateNamed('Off')
        offState.addTransition('MintReward')
        playMovieState = self.fsm.getStateNamed('PlayMovie')
        playMovieState.addTransition('MintReward')

    def enterMintReward(self, ts):
        self.notify.debug('enterMintReward()')
        self.disableCollision()
        self.delayDeleteMembers()
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
            if self.bossBattle:
                messenger.send('localToonConfrontedMintBoss')
        self.movie.playReward(ts, self.uniqueName('building-reward'), self.__handleMintRewardDone)

    def __handleMintRewardDone(self):
        self.notify.debug('mint reward done')
        if self.hasLocalToon():
            self.d_rewardDone(base.localAvatar.doId)
        self.movie.resetReward()
        self.fsm.request('Resume')

    def exitMintReward(self):
        self.notify.debug('exitMintReward()')
        self.movie.resetReward(finish=1)
        self._removeMembersKeep()
        NametagGlobals.setMasterArrowsOn(1)
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\coghq\DistributedMintBattle.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:18:49 Pacific Daylight Time
