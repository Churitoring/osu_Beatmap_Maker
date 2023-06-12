import msvcrt
import time
import os
import win32api
import pygame

def START_MAIN():
    print(f"osu! Beatmap Maker ver. 0.0.1")
    time.sleep(0.2)
    print(f"By Churitoring\n")
    time.sleep(0.2)
    print(f"1: Mania 1K")
    time.sleep(0.05)
    print(f"2: Mania 2K")
    time.sleep(0.05)
    print(f"3: Mania 3K")
    time.sleep(0.05)
    print(f"4: Mania 4K")
    time.sleep(0.05)
    print(f"5: Mania 5K")
    time.sleep(0.05)
    print(f"6: Mania 6K")
    time.sleep(0.05)
    print(f"7: Mania 7K")
    time.sleep(0.05)
    print(f"8: Mania 8K")
    time.sleep(0.05)
    print(f"9: Mania 9K")
    time.sleep(0.05)
    print(f"10: Mania Co-op 5K")
    time.sleep(0.05)
    print(f"11: Mania Co-op 6K")
    time.sleep(0.05)
    print(f"12: Mania Co-op 7K")
    time.sleep(0.05)
    print(f"13: Mania Co-op 8K")
    time.sleep(0.05)
    print(f"14: Mania Co-op 9K")
    time.sleep(0.05)
    print(f"15: Taiko")
    time.sleep(0.05)
    print(f"\n16: Catch(BETA)")
    time.sleep(0.05)
    print(f"17: Standard(BETA)")
    time.sleep(0.2)
    print(f"\n\nEXIT: Ctrl+C")
    time.sleep(0.1)

def START_SEL_KF():
    if mode_input=="1":
        START_1KF()
    if mode_input=="2":
        START_2KF()
    if mode_input=="3":
        START_3KF()
    if mode_input=="4":
        START_4KF()
    if mode_input=="5":
        START_5KF()
    if mode_input=="6":
        START_6KF()
    if mode_input=="7":
        START_7KF()
    if mode_input=="8":
        START_8KF()
    if mode_input=="9":
        START_9KF()
    if mode_input=="10":
        START_10KF()
    if mode_input=="11":
        START_11KF()
    if mode_input=="12":
        START_12KF()
    if mode_input=="13":
        START_13KF()
    if mode_input=="14":
        START_14KF()
    if mode_input=="15":
        START_15KF()
    if mode_input=="16":
        START_16KF()
    if mode_input=="17":
        SELECT_17KF()

def SELECT_17KF():
    print(f"1: 2 Key Mode")
    time.sleep(0.05)
    print(f"2: Keypad Mode(9 Keys)")
    time.sleep(0.05)
    print(f"3: 41 key Mode")
    time.sleep(0.05)
    print(f"4: Full Size Mode")
    time.sleep(0.05)
    print(f"\n5: Setuped Keypad Mode(9 Keys)")
    time.sleep(0.05)
    print(f"6: Setuped 41 key Mode")
    time.sleep(0.05)
    print(f"7: Setuped Full Size Mode")
    time.sleep(0.05)
    select_input=input(f"\n\nPlease enter numbers only.\n\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    if select_input=="1":
        START_17KF1()
    if select_input=="2":
        START_17KF2()
    if select_input=="3":
        START_17KF3()
    if select_input=="4":
        START_17KF4()
    if select_input=="5":
        START_17KF5()
    if select_input=="6":
        START_17KF6()
    if select_input=="7":
        START_17KF7()
        
def START_1KF():
    b = False
    prev_time = win32api.GetTickCount()
    # Received 1 key
    key_inputs = input("Please enter one key.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 256
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_2KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 2 keys
    key_inputs = input("Please enter 2 keys.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 128
                elif input_char == key_list[1]:
                    output_value = 384
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_3KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 3 keys
    key_inputs = input("Please enter 3 keys.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 85
                elif input_char == key_list[1]:
                    output_value = 256
                elif input_char == key_list[2]:
                    output_value = 426
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_4KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 4 keys
    key_inputs = input("Please enter 4 keys.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 64
                elif input_char == key_list[1]:
                    output_value = 192
                elif input_char == key_list[2]:
                    output_value = 320
                elif input_char == key_list[3]:
                    output_value = 448
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_5KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 5 keys
    key_inputs = input("Please enter 5 keys.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 51
                elif input_char == key_list[1]:
                    output_value = 153
                elif input_char == key_list[2]:
                    output_value = 256
                elif input_char == key_list[3]:
                    output_value = 358
                elif input_char == key_list[4]:
                    output_value = 460
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_6KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 6 keys
    key_inputs = input("Please enter 6 keys.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 42
                elif input_char == key_list[1]:
                    output_value = 128
                elif input_char == key_list[2]:
                    output_value = 213
                elif input_char == key_list[3]:
                    output_value = 298
                elif input_char == key_list[4]:
                    output_value = 384
                elif input_char == key_list[5]:
                    output_value = 469
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_7KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 7 keys
    key_inputs = input("Please enter 7 keys.").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 36
                elif input_char == key_list[1]:
                    output_value = 109
                elif input_char == key_list[2]:
                    output_value = 182
                elif input_char == key_list[3]:
                    output_value = 256
                elif input_char == key_list[4]:
                    output_value = 329
                elif input_char == key_list[5]:
                    output_value = 402
                elif input_char == key_list[6]:
                    output_value = 475
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_8KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 8 keys
    key_inputs = input("Please enter 8 keys.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 32
                elif input_char == key_list[1]:
                    output_value = 96
                elif input_char == key_list[2]:
                    output_value = 160
                elif input_char == key_list[3]:
                    output_value = 224
                elif input_char == key_list[4]:
                    output_value = 288
                elif input_char == key_list[5]:
                    output_value = 352
                elif input_char == key_list[6]:
                    output_value = 416
                elif input_char == key_list[7]:
                    output_value = 480
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_9KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 9 keys
    key_inputs = input("Please enter 9 keys.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 28
                elif input_char == key_list[1]:
                    output_value = 85
                elif input_char == key_list[2]:
                    output_value = 142
                elif input_char == key_list[3]:
                    output_value = 199
                elif input_char == key_list[4]:
                    output_value = 256
                elif input_char == key_list[5]:
                    output_value = 312
                elif input_char == key_list[6]:
                    output_value = 369
                elif input_char == key_list[7]:
                    output_value = 426
                elif input_char == key_list[8]:
                    output_value = 483
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_10KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 10 keys
    key_inputs = input("Please enter 10 keys.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 25
                elif input_char == key_list[1]:
                    output_value = 76
                elif input_char == key_list[2]:
                    output_value = 128
                elif input_char == key_list[3]:
                    output_value = 179
                elif input_char == key_list[4]:
                    output_value = 230
                elif input_char == key_list[5]:
                    output_value = 281
                elif input_char == key_list[6]:
                    output_value = 332
                elif input_char == key_list[7]:
                    output_value = 384
                elif input_char == key_list[8]:
                    output_value = 435
                elif input_char == key_list[9]:
                    output_value = 486
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_11KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 12 keys
    key_inputs = input("Please enter 12 keys.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 21
                elif input_char == key_list[1]:
                    output_value = 64
                elif input_char == key_list[2]:
                    output_value = 106
                elif input_char == key_list[3]:
                    output_value = 149
                elif input_char == key_list[4]:
                    output_value = 192
                elif input_char == key_list[5]:
                    output_value = 234
                elif input_char == key_list[6]:
                    output_value = 277
                elif input_char == key_list[7]:
                    output_value = 320
                elif input_char == key_list[8]:
                    output_value = 362
                elif input_char == key_list[9]:
                    output_value = 405
                elif input_char == key_list[10]:
                    output_value = 448
                elif input_char == key_list[11]:
                    output_value = 490
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_12KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 14 keys
    key_inputs = input("Please enter 14 keys.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 18
                elif input_char == key_list[1]:
                    output_value = 54
                elif input_char == key_list[2]:
                    output_value = 91
                elif input_char == key_list[3]:
                    output_value = 128
                elif input_char == key_list[4]:
                    output_value = 164
                elif input_char == key_list[5]:
                    output_value = 201
                elif input_char == key_list[6]:
                    output_value = 237
                elif input_char == key_list[7]:
                    output_value = 274
                elif input_char == key_list[8]:
                    output_value = 310
                elif input_char == key_list[9]:
                    output_value = 347
                elif input_char == key_list[10]:
                    output_value = 384
                elif input_char == key_list[11]:
                    output_value = 420
                elif input_char == key_list[12]:
                    output_value = 457
                elif input_char == key_list[13]:
                    output_value = 493
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_13KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 16 keys
    key_inputs = input("Please enter 16 keys.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 16
                elif input_char == key_list[1]:
                    output_value = 48
                elif input_char == key_list[2]:
                    output_value = 80
                elif input_char == key_list[3]:
                    output_value = 112
                elif input_char == key_list[4]:
                    output_value = 144
                elif input_char == key_list[5]:
                    output_value = 176
                elif input_char == key_list[6]:
                    output_value = 208
                elif input_char == key_list[7]:
                    output_value = 240
                elif input_char == key_list[8]:
                    output_value = 272
                elif input_char == key_list[9]:
                    output_value = 304
                elif input_char == key_list[10]:
                    output_value = 336
                elif input_char == key_list[11]:
                    output_value = 368
                elif input_char == key_list[12]:
                    output_value = 400
                elif input_char == key_list[13]:
                    output_value = 432
                elif input_char == key_list[14]:
                    output_value = 464
                elif input_char == key_list[15]:
                    output_value = 496
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_14KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 18 keys
    key_inputs = input("Please enter 18 keys.\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 14
                elif input_char == key_list[1]:
                    output_value = 42
                elif input_char == key_list[2]:
                    output_value = 71
                elif input_char == key_list[3]:
                    output_value = 99
                elif input_char == key_list[4]:
                    output_value = 128
                elif input_char == key_list[5]:
                    output_value = 156
                elif input_char == key_list[6]:
                    output_value = 184
                elif input_char == key_list[7]:
                    output_value = 213
                elif input_char == key_list[8]:
                    output_value = 241
                elif input_char == key_list[9]:
                    output_value = 270
                elif input_char == key_list[10]:
                    output_value = 298
                elif input_char == key_list[11]:
                    output_value = 327
                elif input_char == key_list[12]:
                    output_value = 355
                elif input_char == key_list[13]:
                    output_value = 384
                elif input_char == key_list[14]:
                    output_value = 412
                elif input_char == key_list[15]:
                    output_value = 440
                elif input_char == key_list[16]:
                    output_value = 469
                elif input_char == key_list[17]:
                    output_value = 497
                print(f"{output_value},192,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

# Beta Version
def START_15KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 9 keys
    key_inputs = input("Please enter 9 keys.\n(Red Red Blue Blue BigRed BigRed BigBlue BigBlue Spinner)\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1

    # Adjusting the spinner length
    s_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        s = int(s_input)
    except ValueError:
        s = 5000
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    print(f"256,192,{a},5,0,0:0:0:0:")
                elif input_char == key_list[1]:
                    print(f"256,192,{a},5,0,0:0:0:0:")
                elif input_char == key_list[2]:
                    print(f"256,192,{a},1,2,0:0:0:0:")
                elif input_char == key_list[3]:
                    print(f"256,192,{a},1,2,0:0:0:0:")
                elif input_char == key_list[4]:
                    print(f"256,192,{a},1,4,0:0:0:0:")
                elif input_char == key_list[5]:
                    print(f"256,192,{a},1,4,0:0:0:0:")
                elif input_char == key_list[6]:
                    print(f"256,192,{a},1,6,0:0:0:0:")
                elif input_char == key_list[7]:
                    print(f"256,192,{a},1,6,0:0:0:0:")
                elif input_char == key_list[8]:
                    print(f"512,384,{a},12,0,{a+s},0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_16KF():
    b = False
    prev_time = win32api.GetTickCount()

    # Received 11 keys
    key_inputs = input("Please enter 11 keys.\n(The last key is the spinner.)\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1

    # Adjusting the spinner length
    s_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        s = int(s_input)
    except ValueError:
        s = 5000
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 0
                elif input_char == key_list[1]:
                    output_value = 57
                elif input_char == key_list[2]:
                    output_value = 114
                elif input_char == key_list[3]:
                    output_value = 171
                elif input_char == key_list[4]:
                    output_value = 228
                elif input_char == key_list[5]:
                    output_value = 285
                elif input_char == key_list[6]:
                    output_value = 342
                elif input_char == key_list[7]:
                    output_value = 339
                elif input_char == key_list[8]:
                    output_value = 456
                elif input_char == key_list[9]:
                    output_value = 512
                if input_char!=key_list[10]:
                    print(f"{output_value},192,{a},1,0,0:0:0:0:")
                if input_char==key_list[10]:
                    print(f"256,192,{a},12,0,{a+s},0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

# osu! Standard
def START_17KF1():
    b = False
    s = 0
    prev_time = win32api.GetTickCount()

    # Received 3 keys
    key_inputs = input("Please enter 3 keys.\n(The last key is the spinner.)\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1

    # Adjusting the spinner length
    s_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        s = int(s_input)
    except ValueError:
        s = 5000
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[2]:
                    print(f"512,384,{a},12,0,{a+s},0:0:0:0:")
                else:
                    print(f"512,384,{a},1,0,0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_17KF2():
    b = False
    prev_time = win32api.GetTickCount()
    
    # Received 10 keys
    key_inputs = input("Please enter 10 keys.\n(The last key is the spinner.)\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    # Adjusting the spinner length
    s_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        s = int(s_input)
    except ValueError:
        s = 5000
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 0
                    output_value2 = 384
                elif input_char == key_list[1]:
                    output_value = 256
                    output_value2 = 384
                elif input_char == key_list[2]:
                    output_value = 512
                    output_value2 = 384
                elif input_char == key_list[3]:
                    output_value = 0
                    output_value2 = 192
                elif input_char == key_list[4]:
                    output_value = 256
                    output_value2 = 192
                elif input_char == key_list[5]:
                    output_value = 512
                    output_value2 = 192
                elif input_char == key_list[6]:
                    output_value = 0
                    output_value2 = 0
                elif input_char == key_list[7]:
                    output_value = 256
                    output_value2 = 0
                elif input_char == key_list[8]:
                    output_value = 512
                    output_value2 = 0
                if input_char!=key_list[9]:
                    print(f"{output_value},{output_value2},{a},1,0,0:0:0:0:")
                if input_char==key_list[9]:
                    print(f"256,192,{a},12,0,{a+s},0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_17KF3():
    b = False
    prev_time = win32api.GetTickCount()
    
    # Received 41 keys
    key_inputs = input("Please enter 41 keys.\n(The last key is the spinner.)\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    # Adjusting the spinner length
    s_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        s = int(s_input)
    except ValueError:
        s = 5000
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                # 1st columns
                if input_char == key_list[0]:
                    output_value = 0
                    output_value2 = 0
                elif input_char == key_list[1]:
                    output_value = 57
                    output_value2 = 0
                elif input_char == key_list[2]:
                    output_value = 114
                    output_value2 = 0
                elif input_char == key_list[3]:
                    output_value = 171
                    output_value2 = 0
                elif input_char == key_list[4]:
                    output_value = 228
                    output_value2 = 0
                elif input_char == key_list[5]:
                    output_value = 285
                    output_value2 = 0
                elif input_char == key_list[6]:
                    output_value = 342
                    output_value2 = 0
                elif input_char == key_list[7]:
                    output_value = 399
                    output_value2 = 0
                elif input_char == key_list[8]:
                    output_value = 456
                    output_value2 = 0
                elif input_char == key_list[9]:
                    output_value = 512
                    output_value2 = 0
                # 2nd columns
                if input_char == key_list[10]:
                    output_value = 0
                    output_value2 = 128
                elif input_char == key_list[11]:
                    output_value = 57
                    output_value2 = 128
                elif input_char == key_list[12]:
                    output_value = 114
                    output_value2 = 128
                elif input_char == key_list[13]:
                    output_value = 171
                    output_value2 = 128
                elif input_char == key_list[14]:
                    output_value = 228
                    output_value2 = 128
                elif input_char == key_list[15]:
                    output_value = 285
                    output_value2 = 128
                elif input_char == key_list[16]:
                    output_value = 342
                    output_value2 = 128
                elif input_char == key_list[17]:
                    output_value = 399
                    output_value2 = 128
                elif input_char == key_list[18]:
                    output_value = 456
                    output_value2 = 128
                elif input_char == key_list[19]:
                    output_value = 512
                    output_value2 = 128
                # 3rd columns
                if input_char == key_list[20]:
                    output_value = 0
                    output_value2 = 256
                elif input_char == key_list[21]:
                    output_value = 57
                    output_value2 = 256
                elif input_char == key_list[22]:
                    output_value = 114
                    output_value2 = 256
                elif input_char == key_list[23]:
                    output_value = 171
                    output_value2 = 256
                elif input_char == key_list[24]:
                    output_value = 228
                    output_value2 = 256
                elif input_char == key_list[25]:
                    output_value = 285
                    output_value2 = 256
                elif input_char == key_list[26]:
                    output_value = 342
                    output_value2 = 256
                elif input_char == key_list[27]:
                    output_value = 399
                    output_value2 = 256
                elif input_char == key_list[28]:
                    output_value = 456
                    output_value2 = 256
                elif input_char == key_list[29]:
                    output_value = 512
                    output_value2 = 256
                # 4th columns
                if input_char == key_list[30]:
                    output_value = 0
                    output_value2 = 384
                elif input_char == key_list[31]:
                    output_value = 57
                    output_value2 = 384
                elif input_char == key_list[32]:
                    output_value = 114
                    output_value2 = 384
                elif input_char == key_list[33]:
                    output_value = 171
                    output_value2 = 384
                elif input_char == key_list[34]:
                    output_value = 228
                    output_value2 = 384
                elif input_char == key_list[35]:
                    output_value = 285
                    output_value2 = 384
                elif input_char == key_list[36]:
                    output_value = 342
                    output_value2 = 384
                elif input_char == key_list[37]:
                    output_value = 399
                    output_value2 = 384
                elif input_char == key_list[38]:
                    output_value = 456
                    output_value2 = 384
                elif input_char == key_list[39]:
                    output_value = 512
                    output_value2 = 384
                if input_char!=key_list[40]:
                    print(f"{output_value},{output_value2},{a},1,0,0:0:0:0:")
                if input_char==key_list[40]:
                    print(f"256,192,{a},12,0,{a+s},0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_17KF4():
    b = False
    prev_time = win32api.GetTickCount()
    
    # Received 46 keys
    key_inputs = input("Please enter 46 keys.\n(The last key is the spinner.)\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    # Adjusting the spinner length
    s_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        s = int(s_input)
    except ValueError:
        s = 5000
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                # 1st columns
                if input_char == key_list[0]:
                    output_value = 0
                    output_value2 = 0
                elif input_char == key_list[1]:
                    output_value = 46
                    output_value2 = 0
                elif input_char == key_list[2]:
                    output_value = 92
                    output_value2 = 0
                elif input_char == key_list[3]:
                    output_value = 138
                    output_value2 = 0
                elif input_char == key_list[4]:
                    output_value = 184
                    output_value2 = 0
                elif input_char == key_list[5]:
                    output_value = 230
                    output_value2 = 0
                elif input_char == key_list[6]:
                    output_value = 276
                    output_value2 = 0
                elif input_char == key_list[7]:
                    output_value = 322
                    output_value2 = 0
                elif input_char == key_list[8]:
                    output_value = 368
                    output_value2 = 0
                elif input_char == key_list[9]:
                    output_value = 414
                    output_value2 = 0
                elif input_char == key_list[10]:
                    output_value = 460
                    output_value2 = 0
                elif input_char == key_list[11]:
                    output_value = 506
                    output_value2 = 0
                # 2nd columns
                elif input_char == key_list[12]:
                    output_value = 23
                    output_value2 = 128
                elif input_char == key_list[13]:
                    output_value = 69
                    output_value2 = 128
                elif input_char == key_list[14]:
                    output_value = 115
                    output_value2 = 128
                elif input_char == key_list[15]:
                    output_value = 161
                    output_value2 = 128
                elif input_char == key_list[16]:
                    output_value = 207
                    output_value2 = 128
                elif input_char == key_list[17]:
                    output_value = 253
                    output_value2 = 128
                elif input_char == key_list[18]:
                    output_value = 299
                    output_value2 = 128
                elif input_char == key_list[19]:
                    output_value = 345
                    output_value2 = 128
                elif input_char == key_list[20]:
                    output_value = 391
                    output_value2 = 128
                elif input_char == key_list[21]:
                    output_value = 437
                    output_value2 = 128
                elif input_char == key_list[22]:
                    output_value = 483
                    output_value2 = 128
                elif input_char == key_list[23]:
                    output_value = 512
                    output_value2 = 128
                # 3rd columns
                elif input_char == key_list[24]:
                    output_value = 23
                    output_value2 = 256
                elif input_char == key_list[25]:
                    output_value = 69
                    output_value2 = 256
                elif input_char == key_list[26]:
                    output_value = 115
                    output_value2 = 256
                elif input_char == key_list[27]:
                    output_value = 161
                    output_value2 = 256
                elif input_char == key_list[28]:
                    output_value = 207
                    output_value2 = 256
                elif input_char == key_list[29]:
                    output_value = 253
                    output_value2 = 256
                elif input_char == key_list[30]:
                    output_value = 299
                    output_value2 = 256
                elif input_char == key_list[31]:
                    output_value = 345
                    output_value2 = 256
                elif input_char == key_list[32]:
                    output_value = 391
                    output_value2 = 256
                elif input_char == key_list[33]:
                    output_value = 437
                    output_value2 = 256
                elif input_char == key_list[34]:
                    output_value = 483
                    output_value2 = 256
                # 4th columns
                elif input_char == key_list[35]:
                    output_value = 46
                    output_value2 = 384
                elif input_char == key_list[36]:
                    output_value = 92
                    output_value2 = 384
                elif input_char == key_list[37]:
                    output_value = 138
                    output_value2 = 384
                elif input_char == key_list[38]:
                    output_value = 184
                    output_value2 = 384
                elif input_char == key_list[39]:
                    output_value = 230
                    output_value2 = 384
                elif input_char == key_list[40]:
                    output_value = 276
                    output_value2 = 384
                elif input_char == key_list[41]:
                    output_value = 322
                    output_value2 = 384
                elif input_char == key_list[42]:
                    output_value = 368
                    output_value2 = 384
                elif input_char == key_list[43]:
                    output_value = 414
                    output_value2 = 384
                elif input_char == key_list[44]:
                    output_value = 460
                    output_value2 = 384
                if input_char!=key_list[45]:
                    print(f"{output_value},{output_value2},{a},1,0,0:0:0:0:")
                if input_char==key_list[45]:
                    print(f"256,192,{a},12,0,{a+s},0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_17KF5():
    b = False
    prev_time = win32api.GetTickCount()
    
    key_list = list("1234567890")
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    # Adjusting the spinner length
    s_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        s = int(s_input)
    except ValueError:
        s = 5000

    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 0
                    output_value2 = 384
                elif input_char == key_list[1]:
                    output_value = 256
                    output_value2 = 384
                elif input_char == key_list[2]:
                    output_value = 512
                    output_value2 = 384
                elif input_char == key_list[3]:
                    output_value = 0
                    output_value2 = 192
                elif input_char == key_list[4]:
                    output_value = 256
                    output_value2 = 192
                elif input_char == key_list[5]:
                    output_value = 512
                    output_value2 = 192
                elif input_char == key_list[6]:
                    output_value = 0
                    output_value2 = 0
                elif input_char == key_list[7]:
                    output_value = 256
                    output_value2 = 0
                elif input_char == key_list[8]:
                    output_value = 512
                    output_value2 = 0
                if input_char!=key_list[9]:
                    print(f"{output_value},{output_value2},{a},1,0,0:0:0:0:")
                if input_char==key_list[9]:
                    print(f"256,192,{a},12,0,{a+s},0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_17KF6():
    b = False
    prev_time = win32api.GetTickCount()
    
    key_list = list("234567890-wertyuiop[asdfghjkl;zxcvbnm,./1")
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    # Adjusting the spinner length
    s_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        s = int(s_input)
    except ValueError:
        s = 5000
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                # 1st columns
                if input_char == key_list[0]:
                    output_value = 0
                    output_value2 = 0
                elif input_char == key_list[1]:
                    output_value = 57
                    output_value2 = 0
                elif input_char == key_list[2]:
                    output_value = 114
                    output_value2 = 0
                elif input_char == key_list[3]:
                    output_value = 171
                    output_value2 = 0
                elif input_char == key_list[4]:
                    output_value = 228
                    output_value2 = 0
                elif input_char == key_list[5]:
                    output_value = 285
                    output_value2 = 0
                elif input_char == key_list[6]:
                    output_value = 342
                    output_value2 = 0
                elif input_char == key_list[7]:
                    output_value = 399
                    output_value2 = 0
                elif input_char == key_list[8]:
                    output_value = 456
                    output_value2 = 0
                elif input_char == key_list[9]:
                    output_value = 512
                    output_value2 = 0
                # 2nd columns
                if input_char == key_list[10]:
                    output_value = 0
                    output_value2 = 128
                elif input_char == key_list[11]:
                    output_value = 57
                    output_value2 = 128
                elif input_char == key_list[12]:
                    output_value = 114
                    output_value2 = 128
                elif input_char == key_list[13]:
                    output_value = 171
                    output_value2 = 128
                elif input_char == key_list[14]:
                    output_value = 228
                    output_value2 = 128
                elif input_char == key_list[15]:
                    output_value = 285
                    output_value2 = 128
                elif input_char == key_list[16]:
                    output_value = 342
                    output_value2 = 128
                elif input_char == key_list[17]:
                    output_value = 399
                    output_value2 = 128
                elif input_char == key_list[18]:
                    output_value = 456
                    output_value2 = 128
                elif input_char == key_list[19]:
                    output_value = 512
                    output_value2 = 128
                # 3rd columns
                if input_char == key_list[20]:
                    output_value = 0
                    output_value2 = 256
                elif input_char == key_list[21]:
                    output_value = 57
                    output_value2 = 256
                elif input_char == key_list[22]:
                    output_value = 114
                    output_value2 = 256
                elif input_char == key_list[23]:
                    output_value = 171
                    output_value2 = 256
                elif input_char == key_list[24]:
                    output_value = 228
                    output_value2 = 256
                elif input_char == key_list[25]:
                    output_value = 285
                    output_value2 = 256
                elif input_char == key_list[26]:
                    output_value = 342
                    output_value2 = 256
                elif input_char == key_list[27]:
                    output_value = 399
                    output_value2 = 256
                elif input_char == key_list[28]:
                    output_value = 456
                    output_value2 = 256
                elif input_char == key_list[29]:
                    output_value = 512
                    output_value2 = 256
                # 4th columns
                if input_char == key_list[30]:
                    output_value = 0
                    output_value2 = 384
                elif input_char == key_list[31]:
                    output_value = 57
                    output_value2 = 384
                elif input_char == key_list[32]:
                    output_value = 114
                    output_value2 = 384
                elif input_char == key_list[33]:
                    output_value = 171
                    output_value2 = 384
                elif input_char == key_list[34]:
                    output_value = 228
                    output_value2 = 384
                elif input_char == key_list[35]:
                    output_value = 285
                    output_value2 = 384
                elif input_char == key_list[36]:
                    output_value = 342
                    output_value2 = 384
                elif input_char == key_list[37]:
                    output_value = 399
                    output_value2 = 384
                elif input_char == key_list[38]:
                    output_value = 456
                    output_value2 = 384
                elif input_char == key_list[39]:
                    output_value = 512
                    output_value2 = 384
                if input_char!=key_list[40]:
                    print(f"{output_value},{output_value2},{a},1,0,0:0:0:0:")
                if input_char==key_list[40]:
                    print(f"256,192,{a},12,0,{a+s},0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

def START_17KF7():
    b = False
    prev_time = win32api.GetTickCount()

    key_list = list("1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./`")
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    # Adjusting the spinner length
    s_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        s = int(s_input)
    except ValueError:
        s = 5000
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                # 1st columns
                if input_char == key_list[0]:
                    output_value = 0
                    output_value2 = 0
                elif input_char == key_list[1]:
                    output_value = 46
                    output_value2 = 0
                elif input_char == key_list[2]:
                    output_value = 92
                    output_value2 = 0
                elif input_char == key_list[3]:
                    output_value = 138
                    output_value2 = 0
                elif input_char == key_list[4]:
                    output_value = 184
                    output_value2 = 0
                elif input_char == key_list[5]:
                    output_value = 230
                    output_value2 = 0
                elif input_char == key_list[6]:
                    output_value = 276
                    output_value2 = 0
                elif input_char == key_list[7]:
                    output_value = 322
                    output_value2 = 0
                elif input_char == key_list[8]:
                    output_value = 368
                    output_value2 = 0
                elif input_char == key_list[9]:
                    output_value = 414
                    output_value2 = 0
                elif input_char == key_list[10]:
                    output_value = 460
                    output_value2 = 0
                elif input_char == key_list[11]:
                    output_value = 506
                    output_value2 = 0
                # 2nd columns
                elif input_char == key_list[12]:
                    output_value = 23
                    output_value2 = 128
                elif input_char == key_list[13]:
                    output_value = 69
                    output_value2 = 128
                elif input_char == key_list[14]:
                    output_value = 115
                    output_value2 = 128
                elif input_char == key_list[15]:
                    output_value = 161
                    output_value2 = 128
                elif input_char == key_list[16]:
                    output_value = 207
                    output_value2 = 128
                elif input_char == key_list[17]:
                    output_value = 253
                    output_value2 = 128
                elif input_char == key_list[18]:
                    output_value = 299
                    output_value2 = 128
                elif input_char == key_list[19]:
                    output_value = 345
                    output_value2 = 128
                elif input_char == key_list[20]:
                    output_value = 391
                    output_value2 = 128
                elif input_char == key_list[21]:
                    output_value = 437
                    output_value2 = 128
                elif input_char == key_list[22]:
                    output_value = 483
                    output_value2 = 128
                elif input_char == key_list[23]:
                    output_value = 512
                    output_value2 = 128
                # 3rd columns
                elif input_char == key_list[24]:
                    output_value = 23
                    output_value2 = 256
                elif input_char == key_list[25]:
                    output_value = 69
                    output_value2 = 256
                elif input_char == key_list[26]:
                    output_value = 115
                    output_value2 = 256
                elif input_char == key_list[27]:
                    output_value = 161
                    output_value2 = 256
                elif input_char == key_list[28]:
                    output_value = 207
                    output_value2 = 256
                elif input_char == key_list[29]:
                    output_value = 253
                    output_value2 = 256
                elif input_char == key_list[30]:
                    output_value = 299
                    output_value2 = 256
                elif input_char == key_list[31]:
                    output_value = 345
                    output_value2 = 256
                elif input_char == key_list[32]:
                    output_value = 391
                    output_value2 = 256
                elif input_char == key_list[33]:
                    output_value = 437
                    output_value2 = 256
                elif input_char == key_list[34]:
                    output_value = 483
                    output_value2 = 256
                # 4th columns
                elif input_char == key_list[35]:
                    output_value = 46
                    output_value2 = 384
                elif input_char == key_list[36]:
                    output_value = 92
                    output_value2 = 384
                elif input_char == key_list[37]:
                    output_value = 138
                    output_value2 = 384
                elif input_char == key_list[38]:
                    output_value = 184
                    output_value2 = 384
                elif input_char == key_list[39]:
                    output_value = 230
                    output_value2 = 384
                elif input_char == key_list[40]:
                    output_value = 276
                    output_value2 = 384
                elif input_char == key_list[41]:
                    output_value = 322
                    output_value2 = 384
                elif input_char == key_list[42]:
                    output_value = 368
                    output_value2 = 384
                elif input_char == key_list[43]:
                    output_value = 414
                    output_value2 = 384
                elif input_char == key_list[44]:
                    output_value = 460
                    output_value2 = 384
                if input_char!=key_list[45]:
                    print(f"{output_value},{output_value2},{a},1,0,0:0:0:0:")
                if input_char==key_list[45]:
                    print(f"256,192,{a},12,0,{a+s},0:0:0:0:")
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass

pygame.mixer.init(buffer=2)
sound_file = "sound.mp3"
sound_effect=pygame.mixer.Sound(sound_file)
os.system('cls' if os.name == 'nt' else 'clear')
START_MAIN()
mode_input=input(f"\n\nPlease enter numbers only.\n\n")
os.system('cls' if os.name == 'nt' else 'clear')
START_SEL_KF()