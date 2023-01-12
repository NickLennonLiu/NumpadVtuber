import keyboard
#from pynput import keyboard as kb

num_to_pad = {
	0: 82, # 0 will set insert mode so better not to 
	1: 79, 
	2: 80,
	3: 81, 
	4: 75,
	5: 76,
	6: 77,
	7: 71,
	8: 72,
	9: 73
}

pad_scancodes = num_to_pad.values()

