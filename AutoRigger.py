#createSkeleton w/ ik handles 
import maya.cmds as cmds

centerX = 0
centerY = 15
centerZ = 0
numSpineJoints = 6

if cmds.objExists('root'):
    cmds.delete('root')

rootJoint = cmds.joint(p=(0,centerY,0), name='root')
                
#spine
for i in range(1,numSpineJoints):
    cmds.joint(p=(0,(2*i+centerY),0), name='spine#')
  		
cmds.ikHandle(sj='spine1',ee='spine5', name='spineHandleIK')
    
cmds.select('spine5')    
cmds.joint(p=(0,(numSpineJoints-2)*numSpineJoints,1), name='collarBone')

#left arm
cmds.joint(p=(4,(numSpineJoints-2)*numSpineJoints,1),name='leftShoulder')
cmds.joint(p=(4,(numSpineJoints-3)*numSpineJoints,0),name='leftElbow')
cmds.joint(p=(4,(numSpineJoints-4)*numSpineJoints,1),name='leftWrist')
cmds.joint(p=(4,(numSpineJoints-4)*numSpineJoints-1,1),name='leftHand')
cmds.ikHandle(sj='leftShoulder',ee='leftWrist', name='leftArmIK')
    
cmds.select('collarBone')
#right arm
cmds.joint(p=(-4,(numSpineJoints-2)*numSpineJoints,1),name='rightShoulder')
cmds.joint(p=(-4,(numSpineJoints-3)*numSpineJoints,0),name='rightElbow')
cmds.joint(p=(-4,(numSpineJoints-4)*numSpineJoints,1),name='rightWrist')
cmds.joint(p=(-4,(numSpineJoints-4)*numSpineJoints-1,1),name='rightHand')                
cmds.ikHandle(sj='rightShoulder',ee='rightWrist', name='rightArmIK')

cmds.joint(p=(0,centerY-2,centerZ+1), name='pelvis')
cmds.parent('pelvis', 'root')
# left leg
cmds.joint(p=(centerX+3,centerY-2,0), name='left_upLeg')
cmds.joint(p=(centerX+3,centerY-7,centerZ+.5), name='left_loLeg')
cmds.joint(p=(centerX+3,centerY-12,0), name='left_foot')
cmds.joint(p=(centerX+3,centerY-14,1), name='left_ball')
cmds.joint(p=(centerX+3,centerY-14,3), name='left_ball_end')
cmds.ikHandle(sj='left_upLeg',ee='left_foot', name='leftLegIK')
#right leg
cmds.select('pelvis')
cmds.joint(p=(centerX-3,centerY-2,0), name='right_upLeg')
cmds.joint(p=(centerX-3,centerY-7,centerZ+.5), name='right_loLeg')
cmds.joint(p=(centerX-3,centerY-12,0), name='right_foot')
cmds.joint(p=(centerX-3,centerY-14,1), name='right_ball')
cmds.joint(p=(centerX-3,centerY-14,3), name='right_ball_end')
cmds.ikHandle(sj='right_upLeg',ee='right_foot', name='rightLegIK')

#joint orientation 
cmds.joint('root', edit = True, orientJoint = 'xyz',sao= 'yup', ch = True, zso= True)