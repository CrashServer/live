#!/bin/bash

cp ~/live/crash_config_live.py ~/live/crash_config.py &

### SC + TROOP server
scide %F /home/zbdm/crashserver/config/startuplive.scd &
cd ~/live/Troop/ && python3 run-server.py &
#konsole --new-tab --hold --workdir ~/live/Troop/ -e python3 run-server.py&
sleep 10

### Carla & jack_mixer  
#non-mixer --osc-port 7788 /home/zbdm/crashserver/Fichier_Config/non_mixer_live/ & 
jack_mixer -c ~/crashserver/config/jack_mixer_crash &

# carla /home/zbdm/crashserver/Fichier_Config/LiveFocNoPedal.carxp &
#konsole --new-tab --hold --workdir ~/crashserver/Fichier_Config/ -e carla carla_master_behringer_pedals.carxp &


#konsole --new-tab --hold --workdir ~/crashserver/config/ -e carla carla_live.carxp &

### Crash Panel + Troop Client
cd ~/live/crashPanel/ && python3 crashpannel.py &
cd ~/live/Troop/ && python3 run-client.py &
# konsole --new-tab --hold --workdir ~/live/crashPanel/ -e python3 crashpannel.py &
# konsole --new-tab --hold --workdir ~/live/Troop/ -e python3 run-client.py &

### Crash OS
# konsole --new-tab --hold --workdir ~/program/openFrameworks/apps/live/crashOS_2022/bin/ -e ./crashOS_2022 &

### Recording
sleep 5
# timemachine -f wav -p /run/media/zbdm/DATA/CRASH_SERVER/Recording/ -s "Carla:x42-dpl - Digital Peak Limiter Stereo:Out Left" "Carla:x42-dpl - Digital Peak Limiter Stereo:Out Right" &
# carla ~/crashserver/config/carla_live.carxp &
carla ~/crashserver/config/carla_home_cave.carxp &

# timemachine -f wav -p /run/media/CRASH_SERVER/Recording/ -s "jack_mixer:Mix L" "jack_mixer:Mix R" &

pkexec cpupower frequency-set -g performance &


#kronometer &
#lebiniou -i jackaudio -t ~crash2 &
#/usr/bin/timemachine -c 7 -s -p /home/zbdm/crashserver/Recording/crash_ -f wav &
#cd /home/zbdm/crashserver/live/crashPanel/ && python3 crashpanel.py &
#cd /home/zbdm/crashserver/live/Troop/ && python3 run-client.py &
#cd ~/crashserver/Recording/ && read -p "Press enter to continue" && jack_capture --channels 7 --port jack_mixer:"FoxDot out"* --port jack_mixer:"fx1 out" --port jack_mixer:"fx2 out" --port jack_mixer:"Voice out"* --bufsize 8
