# Learning_steps_robots

Study series steps for learning multiple axis problems, robots problems as the exploring problems we cannot use only power of calculations that is because it will take a long time or it will create multiple of variables and that is not sufficient costs. One way to solve this problem with fewer efforts of codings is to use the steps ladder, only gradients decents power of calculation and optimizers algorithms approches of next critical points for the functions and result from back-propagatyions multiple time to decide it is positive or negative with or without learning rules or scores.

## For comparison with codes ## 

One axis problem, you do not need to consider actions continue targets from another axis but one action per cross section is possible with AI - Deep_Learning as the Ping-Pong games.

#### One axis problem ####

The player tries to move the player's cursor to balance with increasing steps value until it reaches one side of the game's stage ( Mario Games ) by the equation ```step - player_x_position``` and the player jumps with the equation ```player_x_position - player_y_position``` .  It can be applied to Ping-Pong games by limiting the maximum of the step values or ```step % 50``` 

``` [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5] ```

```
for i in range( game_step ):
    step = step + 1
    
    coeff_01 = step 
    coeff_02 = step - player_x_position
    coeff_03 = player_x_position - player_y_position
```

### Multiple axis problem ####

It required significants for AI to learning additional task from the current task and its continuity, see the output there are possibilities to learn additional tasks by its significant and continue do it with the ratios until robots learn all possible rules. The AI auto-play learns that ladder, fireball, and coins are conditions it which it moves. This is number magitudes equation ```gamescores + len( list_ladder ) + len( coinGroup ) + len( fireballGroup )``` and this is number relative position ```player[0][0] - series_1``` .

``` [0, 0, 2, 2, 4, 1, 1, 1, 3, 3, 0, 0, 2, 2, 4, 1, 1, 1, 3, 3, 0, 0, 2, 2, 4, 1, 1, 1, 3, 3] ```

```
input = [ ]	
for i in range( 30 ) :

    n_steps = abs( steps % ( 5 ) - steps % ( 2 ) )

    series_1 = n_steps
    input.append( series_1 )
    steps = steps + 1
	
    contrl = gamescores + len( list_ladder ) + len( coinGroup ) + len( fireballGroup )
    contr2 = player[0][0] - series_1
    contr3 = 1
    contr4 = 1
    contr5 = 1
```

## Constants ##


```
PATH = "C:\\Python310\\PLE\\ple\\games\\monsterkong\\assets\\"
PLAYER_ST_PIC = "still.png"
PLAYER_LF_PIC = "left.png"
PLAYER_L2_PIC = "left2.png"
PLAYER_RT_PIC = "right.png"
PLAYER_R2_PIC = "right2.png"

MONSTER_01 = "monster0.png"
MONSTER_02 = "monster01.png"
MONSTER_03 = "monster1.png"
MONSTER_04 = "monster2.png"
MONSTER_05 = "monster3.png"
MONSTER_06 = "monster11.png"
MONSTER_07 = "monster21.png"
MONSTER_08 = "monster31.png"
MONSTER_09 = "monsterstill0.png"
MONSTER_10 = "monsterstill1.png"
MONSTER_11 = "monsterstill10.png"
MONSTER_12 = "monsterstill11.png"

dic_image = { "still" : PLAYER_ST_PIC, "left" : PLAYER_LF_PIC, "left2" : PLAYER_L2_PIC, "right" : PLAYER_RT_PIC, 
              "right2" : PLAYER_R2_PIC }

dic_monster = { "right" : MONSTER_01, "left" : MONSTER_02, "right2" : MONSTER_03, "right3" : MONSTER_04, "right4" : MONSTER_05, 
                "left3" : MONSTER_06, "left4" : MONSTER_07, "left5" : MONSTER_08, "left6" : MONSTER_09, "still1" : MONSTER_10, 
                "still2" : MONSTER_11, "still3" : MONSTER_12 }
```

## Controls ##


#### Sample series for player actions #5 ####

There are possible 5 actions for the player, see the attached picture it is the same way the robots explored conditions, sample values must be dependent on one axis and vary in scope for another axis for time efficient.

```
input = [ 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 4, 4, 4, 4, 4, 4, 3, 3, 3, 1, 1, 1, 0, 0 ]
```


#### Sample series for player actions #12 ####


There are possible 12 actions for the player, see the attached picture it is the same way the robots explored conditions, sample values must be dependent on one axis and vary in scope for another axis for time efficient.

```
monster = []
for i in range( 30 ) :
    monster.append( i % 12 )
    
monster = [0, 0, 2, 2, 4, 1, 1, 1, 3, 3, 0, 0, 2, 2, 4, 1, 1, 1, 3, 3, 0, 0, 2, 2, 4, 1, 1, 1, 3, 3]
```

## Files and Dictionary ##

|File Name|Description |
--- | --- |
|sample.py|sample codes|
|Figure_1.png|sample actions|
|Figure_2.png|learning actions|
|ladder.gif|action to ladder|
|README.md|readme file|

## Result ##

The result from our learning steps series indicated how samples explored the data in the game axes.

#### Sample player actions ####

Possible actions no learning.

![Sample player actions](https://github.com/jkaewprateep/Learning_steps_robots/blob/main/Figure_1.png?raw=true "Sample player actions")

#### Sample monster actions ####

Possible actions learning.

![Sample monster actions](https://github.com/jkaewprateep/Learning_steps_robots/blob/main/Figure_2.png?raw=true "Sample monster actions")

#### Find ladder ###

AI find and took action on the target with no rules added to its condition.

![Find ladder](https://github.com/jkaewprateep/Learning_steps_robots/blob/main/ladder.gif?raw=true "Find ladder")
