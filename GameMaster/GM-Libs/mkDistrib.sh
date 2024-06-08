#!/bin/bash
rm -Rf ~/GameMaster
mkdir ~/GameMaster
A=~/GameMaster
cp GamePlayer_A.jsfx GamePlayer_B.jsfx GamePlayer.jsfx-inc FilePlayer_A.jsfx FilePlayer_B.jsfx FilePlayer.jsfx-inc $A
cp clip_lib.jsfx-inc clip_lib_MIDI.jsfx-inc colors-def.jsfx-inc mSL_Clib.jsfx-inc mSL_Extend.jsfx-inc  $A
cp mSL_Utilities.jsfx-inc mSL_Xlib.jsfx-inc mSL_strsDcl.jsfx-inc mkConfigs.sh Scheduler.jsfx-inc $A
cp ui-lib.jsfx-inc ui-lib-JJ.jsfx-inc ui-lib-JJ-GUI.jsfx-inc xfilter.jsfx-inc $A
cp -R themes scripts mSL_tests $A
cp MIDI_In.jsfx MIDI_In.jsfx-inc MIDI_Out.jsfx Mix8to2.jsfx Multichannel_VU_meter MuteAll.jsfx $A
cp ChannelsSwitcher.jsfx MCBM-64.jsfx Skope2.jsfx SmoothMultiLimiter.jsfx channels-folder.jsfx $A
cp APC_Sensors.jsfx APCmini_Disp.jsfx GP_Parameters.jsfx-inc GM_User_ini.jsfx-inc $A
cp Banks.txt Clips.txt HPConfigs.txt PlayModes.txt Sensors.txt SpaceModes.txt $A
cp ../Doc/GameMaster-Version-1.0.pdf $A
cd $A; ./mkConfigs.sh
