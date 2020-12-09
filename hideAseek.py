import os
import random
import keyboard
ai_con=0
# making map
map_range=10
lis = [[random.randrange(0,3,1) for x in range(map_range)] for x in range(map_range)]
# goal
goal = ["8","9"]
lis[random.randrange(0,map_range)][random.randrange(0,map_range)]=goal[0]
lis[random.randrange(0,map_range)][random.randrange(0,map_range)]=goal[1]
#Player
Player=4 # cannot use 0,1,2,Goals
x=random.randrange(0,map_range)
y=random.randrange(0,map_range)
lis[y][x]=Player
# player control
def Player_control():
    global x,y,map_range,goal,lis,Player,ai_con
    if y-1!=-1:# prevent out of range
        if((keyboard.is_pressed('8')or ai_con==8) and lis[y-1][x]!=2):# prevent through a wall
            y=y-1# go forward

            if lis[y][x] in goal: # print goal clear
                goal[goal.index(lis[y][x])]="clear"
            else:
                lis[y][x]=Player # print Player
            lis[y+1][x]=0 # remove Player
    if y+1!=map_range:# prevent out of range
        if((keyboard.is_pressed('2')or ai_con==2) and lis[y+1][x]!=2):# prevent through a wall
            y=y+1# go forward

            if lis[y][x] in goal:# print goal clear
                goal[goal.index(lis[y][x])]="clear"
            else:
                lis[y][x]=Player# print Player
            lis[y-1][x]=0# remove Player
    if x-1!=-1:# prevent out of range
        if((keyboard.is_pressed('4')or ai_con==4) and lis[y][x-1]!=2):# prevent through a wall
            x=x-1# go forward

            if lis[y][x] in goal:# print goal clear
                goal[goal.index(lis[y][x])]="clear"
            else:
                lis[y][x]=Player # print Player
            lis[y][x+1]=0# remove Player
    if x+1!=map_range:# prevent out of range
        if((keyboard.is_pressed('6')or ai_con==6) and lis[y][x+1]!=2):# prevent through a wall
            x=x+1# go forward

            if lis[y][x] in goal:# print goal clear
                goal[goal.index(lis[y][x])]="clear"
            else:
                lis[y][x]=Player # print Player
            lis[y][x-1]=0# remove Player

    if y-1!=-1 and x-1!=-1:# prevent out of range
        if((keyboard.is_pressed('7')or ai_con==7) and lis[y-1][x-1]!=2):# prevent through a wall
            y=y-1# go forward
            x=x-1
            if lis[y][x] in goal: # print goal clear
                goal[goal.index(lis[y][x])]="clear"
            else:
                lis[y][x]=Player # print Player
            lis[y+1][x+1]=0 # remove Player

    if y-1!=-1 and x+1!=map_range:# prevent out of range
        if((keyboard.is_pressed('9')or ai_con==9) and lis[y-1][x+1]!=2):# prevent through a wall
            y=y-1# go forward
            x=x+1
            if lis[y][x] in goal: # print goal clear
                goal[goal.index(lis[y][x])]="clear"
            else:
                lis[y][x]=Player # print Player
            lis[y+1][x-1]=0 # remove Player

    if y+1!=map_range and x-1!=-1:# prevent out of range
        if((keyboard.is_pressed('1')or ai_con==1) and lis[y+1][x-1]!=2):# prevent through a wall
            y=y+1# go forward
            x=x-1
            if lis[y][x] in goal: # print goal clear
                goal[goal.index(lis[y][x])]="clear"
            else:
                lis[y][x]=Player # print Player
            lis[y-1][x+1]=0 # remove Player

    if y+1!=map_range and x+1!=map_range:# prevent out of range
        if((keyboard.is_pressed('3')or ai_con==3) and lis[y+1][x+1]!=2):# prevent through a wall
            y=y+1# go forward
            x=x+1
            if lis[y][x] in goal: # print goal clear
                goal[goal.index(lis[y][x])]="clear"
            else:
                lis[y][x]=Player # print Player
            lis[y-1][x-1]=0 # remove Player
def map_info():
    global Player,goal,map_range
    # map info
    os.system('cls')
    print('\033[38;5;112m'+'Player : bot | Seeker # = '+str(Player)+'\033[0m')
    print('\033[38;5;178m'+'Goal : [ %s, %s ]'%(goal[0],goal[1])+'\033[0m')
    print('\033[38;5;69m'+'Map Size :',map_range,'x',map_range,'\033[0m')
def print_map():
    global lis,goal,Player
    # print map
    for i in lis:
        for j in i:
            # print wall
            if j==2:
                print('\033[38;5;166m'+str(j)+'\033[0m',end=" ")
            # print goal
            elif str(j)==goal[0] or str(j)==goal[1]:
                print('\033[38;5;178m'+str(j)+'\033[0m',end=" ")
            # print road
            elif j==Player:
                print('\033[38;5;112m'+str(Player)+'\033[0m',end=" ")
            else:
                print('0',end=" ")
        print()
    print()
def control_info():# print control info
    c1='◆'
    c2='▲'
    c3='◆'
    c4='◀'
    c6='▶'
    c7='◆'
    c8='▼'
    c9='◆'

    global ai_con
    if keyboard.is_pressed('8')or ai_con==8:
        c2='\033[38;5;69m'+'▲'+'\033[0m'

    if keyboard.is_pressed('2')or ai_con==2:
        c8='\033[38;5;69m'+'▼'+'\033[0m'

    if keyboard.is_pressed('6')or ai_con==6:
        c6='\033[38;5;69m'+'▶'+'\033[0m'

    if keyboard.is_pressed('4')or ai_con==4:
        c4='\033[38;5;69m'+'◀'+'\033[0m'

    if keyboard.is_pressed('7')or ai_con==7:
        c1='\033[38;5;69m'+'◆'+'\033[0m'

    if keyboard.is_pressed('9')or ai_con==9:
        c3='\033[38;5;69m'+'◆'+'\033[0m'

    if keyboard.is_pressed('1')or ai_con==1:
        c7='\033[38;5;69m'+'◆'+'\033[0m'

    if keyboard.is_pressed('3')or ai_con==3:
        c9='\033[38;5;69m'+'◆'+'\033[0m'

    print('\t'+c1+c2+c3)
    print('\t'+c4+'  '+c6)
    print('\t'+c7+c8+c9)
# loop
print("PRESS Enter")
for loop in range(100000):

    if keyboard.is_pressed('Enter') or keyboard.is_pressed('8') or keyboard.is_pressed('2')or keyboard.is_pressed('4')or keyboard.is_pressed('6')or keyboard.is_pressed('7')or keyboard.is_pressed('9')or keyboard.is_pressed('1')or keyboard.is_pressed('3'):
        map_info()
        # finish
        if goal[0]=="clear" and goal[1]=="clear":
            break
        Player_control()
        print_map()
        control_info()

print("good job")
