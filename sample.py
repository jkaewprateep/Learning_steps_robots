
import tensorflow as tf

import matplotlib.pyplot as plt

steps = 0

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

dic_image = { "still" : PLAYER_ST_PIC, "left" : PLAYER_LF_PIC, "left2" : PLAYER_L2_PIC, "right" : PLAYER_RT_PIC, "right2" : PLAYER_R2_PIC }

dic_monster = { "right" : MONSTER_01, "left" : MONSTER_02, "right2" : MONSTER_03, "right3" : MONSTER_04, "right4" : MONSTER_05, "left3" : MONSTER_06,
				"left4" : MONSTER_07, "left5" : MONSTER_08, "left6" : MONSTER_09, "still1" : MONSTER_10, "still2" : MONSTER_11, "still3" : MONSTER_12 }

# input = [ 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 4, 4, 4, 4, 4, 4, 3, 3, 3, 1, 1, 1, 0, 0 ]

monster = []
for i in range( 30 ) :
	n_steps = abs( steps % ( 12 ) - steps % ( 5 ) )

	series_1 = n_steps
	monster.append( series_1 )
	steps = steps + 1
	
print( monster )

input = [ ]	
for i in range( 30 ) :

	n_steps = abs( steps % ( 5 ) - steps % ( 2 ) )

	series_1 = n_steps
	input.append( series_1 )
	steps = steps + 1
	
print( input )
	
plt.figure(figsize=(2 , 30))
plt.suptitle(" Monster Kong - eq. ")

for i in range( len(input) ) :
	
	action = list(dic_image.keys())[input[i]]
	
	image = tf.io.read_file( PATH + list(dic_image.values())[int(input[i])] )
	image = tf.io.decode_png( image, dtype=tf.dtypes.uint8, name="decode_png" )
	image = tf.keras.preprocessing.image.array_to_img(image)
	plt.subplot( 2 , 30, i + 1 )
	plt.xticks([])
	plt.yticks([])
	plt.grid(False)
	plt.imshow( image )
	plt.xlabel( input[i] )
	plt.title( action )
	
for i in range( len(input) ) :

	action = list(dic_monster.keys())[monster[i]]

	image = tf.io.read_file( PATH + list(dic_monster.values())[int(monster[i])] )
	image = tf.io.decode_png( image, dtype=tf.dtypes.uint8, name="decode_png" )
	image = tf.keras.preprocessing.image.array_to_img(image)
	plt.subplot( 2 , 30, len(input) + i + 1 )
	plt.xticks([])
	plt.yticks([])
	plt.grid(False)
	plt.imshow( image )
	plt.xlabel( monster[i] )
	plt.title( action )


plt.show()
