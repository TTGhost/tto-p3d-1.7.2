import wx
from direct.task.Task import Task

def wxLoop(self):
    # Do all the wxPython events waiting on this frame
    while base.wxApp.Pending():
        base.wxApp.Dispatch()
    return Task.cont

def spawnWxLoop():
    if not getattr(base, 'wxApp', None):
        # Create a new base.wxApp, but only if it's not already
        # created.
        base.wxApp = wx.App(False)

    # Spawn this task
    taskMgr.add(wxLoop, "wxLoop")
