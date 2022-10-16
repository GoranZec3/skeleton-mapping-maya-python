from maya import cmds 


def dict_Values(dv):
	'''dict with names of joints from Mixamo skeleton. Function returns index of joint''' 
    mappingDict = {"Hips":"1",
                   "Spine":"8",
                   "Spine1":"23",
                   "Spine2":"24",
                   "Neck":"20",
                   "Head":"15",
                   "LeftShoulder":"18",
                   "LeftArm":"9",
                   "LeftForeArm":"10",
                   "LeftHand":"11",
                   "LeftHandThumb1":"50",
                   "LeftHandThumb2":"51",
                   "LeftHandThumb3":"52",
                   "LeftHandIndex1":"54",
                   "LeftHandIndex2":"55",
                   "LeftHandIndex3":"56",
                   "LeftHandMiddle1":"58",
                   "LeftHandMiddle2":"59",
                   "LeftHandMiddle3":"60",
                   "LeftHandRing1":"62",
                   "LeftHandRing2":"63",
                   "LeftHandRing3":"64",
                   "LeftHandPinky1":"66",
                   "LeftHandPinky2":"67",
                   "LeftHandPinky3":"68",
                   "RightShoulder":"19",
                   "RightArm":"12",
                   "RightForeArm":"13",
                   "RightHand":"14",
                   "RightHandThumb1":"74",
                   "RightHandThumb2":"75",
                   "RightHandThumb3":"76",
                   "RightHandIndex1":"78",
                   "RightHandIndex2":"79",
                   "RightHandIndex3":"80",
                   "RightHandMiddle1":"82",
                   "RightHandMiddle2":"83",
                   "RightHandMiddle3":"84",
                   "RightHandRing1":"86",
                   "RightHandRing2":"87",
                   "RightHandRing3":"88",
                   "RightHandPinky1":"90",
                   "RightHandPinky2":"91",
                   "RightHandPinky3":"92",
                   "LeftUpLeg":"2",
                   "LeftLeg":"3",
                   "LeftFoot":"4",
                   "LeftToeBase":"16",
                   "RightUpLeg":"5",
                   "RightLeg":"6",
                   "RightFoot":"7",
                   "RightToeBase":"17"
                   }

    return mappingDict.get(dv, None)

def runMapping():
    print("Mapping in process")
    sk_list = cmds.ls(type='joint')
    ch_name="Charcter01" #character name
    mel.eval('hikCreateCharacter("{}")'.format(ch_name)) #create character
	
    for sk in sk_list:
        mp_jnt = dict_Values(sk)
        mel.eval('setCharacterObject("{}", "{}","{}",0);'.format(sk, ch_name, mp_jnt))
        print(dict_Values(sk))
        
        
