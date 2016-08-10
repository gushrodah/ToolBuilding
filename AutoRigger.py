import maya.cmds as cmds
from functools import partial

def createWindow(pTitle, pApplyCallback):
    #set up window
    windowID = 'windowID'
    
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)
        
    cmds.window(windowID, title=pTitle, resizeToFitChildren=True)
    cmds.rowColumnLayout(numberOfColumns=2)

    cmds.separator(h=10,style='none')
    cmds.separator(h=10,style='none')
    #display fields and save data
    cmds.text(label='num spine joints')
    iField =  cmds.intField(value =5)

    #callbacks here
    cmds.text(label='Step 1:')
    cmds.button(label='Load Sample Rig', command=functools.partial(SampleCallback, iField))
    cmds.separator(h=10,style='none')
    cmds.separator(h=10,style='none')
    
    cmds.text(label='Step 2:')
    cmds.text(label='Adjust joints to fit mesh')
    cmds.separator(h=10,style='none')
    cmds.separator(h=10,style='none')
    
    cmds.text(label='Step 3:')    
    cmds.button(label='Mirror Joints', command=MirrorCallback)
    cmds.separator(h=10,style='none')
    cmds.separator(h=10,style='none')
    
    cmds.text(label='Step 4:')
    cmds.button(label='Create Handles', command=HandlesCallback)
    cmds.separator(h=10,style='none')
    cmds.separator(h=10,style='none')
    
    cmds.text(label='Step5:')
    cmds.button(label='Bind Skin', command=BindCallback)
    cmds.separator(h=10,style='none')
    cmds.separator(h=10,style='none')
    
    cmds.separator(h=10,style='none')
    
    def cancelCallback(*pArgs):
		if cmds.window(windowID, exists=True):
			cmds.deleteUI(windowID)
    
    cmds.button(label="Cancel", command=cancelCallback)
    
    cmds.showWindow()
        
	
def HandlesCallback(*pArgs):
    l_armPosition = cmds.joint('leftArmIK', query=True, position=True)
    armHandle = cmds.circle()
    #cmds.select('leftShoulder')
    cmds.move(int((l_armPosition))
	
def BindCallback(*Args):
    #cmds.select('root')
    cmds.bindSkin('root')
	
def MirrorCallback(*pArgs):
    if cmds.objExists('rightShoulder'):
        cmds.delete('rightShoulder')
        #cmds.delete('rightArmIK')
    else:
        cmds.mirrorJoint('leftShoulder', myz=True, mxz=True, searchReplace=['left','right'])
    if cmds.objExists('right_upLeg'):
        cmds.delete('right_upLeg')
        #cmds.delete('rightLegIK')
    else:
        cmds.mirrorJoint('left_upLeg', myz=True,searchReplace=['left','right'])
	
def SampleCallback(field, *pArgs):
    centerX = 0
    centerY = 15
    centerZ = 0

    if cmds.objExists('root'):
        cmds.delete('root')

    rootJoint = cmds.joint(p=(0,centerY,0), name='root')
                
    numSpineJoints = cmds.intField(field, query=True, value=True)
    #pNumSpine = numSpineJoints
    for i in range(1,numSpineJoints):
        cmds.joint(p=(0,(2*i+centerY),0), name='spine#')
  		
    #cmds.ikHandle(sj='spine1',ee='spine5', name='spineHandleIK')
    
    cmds.select('spine'+str(numSpineJoints-1))    
    cmds.joint(p=(0,2*i+centerY,1), name='collarBone')

    #left arm
    cmds.joint(p=(3,2*i+centerY,1),name='leftShoulder')
    cmds.joint(p=(numSpineJoints+3,2*i+centerY,.75),name='leftElbow')
    cmds.joint(p=((numSpineJoints+3)*2,2*i+centerY,1),name='leftWrist')
    cmds.joint(p=((numSpineJoints+3)*2+.5,2*i+centerY,1),name='leftHand')
    cmds.ikHandle(sj='leftShoulder',ee='leftWrist', name='leftArmIK')

    cmds.joint(p=(0,centerY-2,centerZ+1), name='pelvis')
    cmds.parent('pelvis', 'root')
    # left leg
    cmds.joint(p=(centerX+3,centerY-2,0), name='left_upLeg')
    cmds.joint(p=(centerX+3,centerY-7,centerZ+.5), name='left_loLeg')
    cmds.joint(p=(centerX+3,centerY-12,0), name='left_foot')
    cmds.joint(p=(centerX+3,centerY-14,1), name='left_ball')
    cmds.joint(p=(centerX+3,centerY-14,3), name='left_ball_end')
    cmds.ikHandle(sj='left_upLeg',ee='left_foot', name='leftLegIK')

    #joint orientation 
    cmds.joint('root', edit = True, orientJoint = 'xyz',sao= 'yup', ch = True, zso= True)
        
createWindow('Auto Rigger', applyCallback)