import maya.cmds as cmds

def createUI(pWindowTitle, pApplyCallback):
    
    windowID = 'myWindowID'
    
    #if cmds.window(windowID, e = True):
    #    cmds.deleteUI(windowID)
        
    #else:
    cmds.window(windowID, title=pWindowTitle, sizeable=False, resizeToFitChildren=True)
    # layout and size 
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1,75), (2,60), (3,60)], columnOffset=[1,'right',3])
    
    # Display text
    cmds.text(label = 'Time Range:')
    
    # int field
    value = cmds.playbackOptions(q=True, minTime=True)
    startTime = cmds.intField(value)
    
    # empty space 
    cmds.separator(h=10, style='none')
    
    # text field
    targetAttributeField = cmds.textField(text='rotateY')
    
    cmds.button(label='Apply', command=pApplyCallback)
    
    def cancelCallback(*pArgs):
		if cmds.window(windowID, exists=True):
			cmds.deleteUI(windowID)
    
    cmds.button(label='Cancel', command=cancelCallback)
    
    cmds.showWindow()

def applyCallback( *pArgs):
	print 'this shit is bananas'

 
createUI('this is a window', applyCallback)