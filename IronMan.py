import os
from random import shuffle

# Import libraries of interest
while True:
    try:
        from PIL import Image, ImageDraw
        break
    except:
        import sys
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
        continue


def imageGrid(imgs, rows, cols):
    '''
    Function to generate a grid of images given an image list, row number, and column number
    '''

    # Find size and establish grid
    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    
    # Paste images into correctly sized grid
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))

    return grid


def getPlayerList():
    '''
    Generate a list of players from a list
    '''

    # Get number of players
    while True:
        try:
            n = int(input('\nHow many players?\n> '))
            break
        except:
            print("Please enter a valid player count...")
            continue

    # Generate a list of player names
    count = 0
    players = []
    for _ in range(n):
        while True:
            if count > 0:
                p = input('\nWho else is playing?\n> ')
            else:
                p = input('\nWho is playing?\n> ')

            # Check that name is correct
            chk = input(f"Is the name {p} ok? (n if not)\n> ")  
            if chk.lower().startswith('n'):
                continue
            else:
                players.append(p)
                count += 1
                break
    
    return players


def startScreen():
    '''
    Start screen and determine if you want to use default names
    '''
    # Print main screen and get input for if there will be several players
    print("\nWelcome to the Melee Iron Man Generator!\n")
    while True:
        print("Would you like to enter player names? (Y/N)")
        q = input("NOTE: If not, defaults to two players...\n> ")
        if q.lower().startswith('y'):
            query = True
            break
        elif q.lower().startswith('n'):
            query = False
            break
        else:
            print('Enter a valid input...\n')
            continue
    
    return query


def main():
    '''
    Main iron man generation code
    '''
    query = startScreen()
    # Get list of players
    if query: 
        players = getPlayerList()
    else:
        players = ['Player 1', 'Player 2']

    # Make a new board for each player
    for player in players:
        # Pull all images and shuffle
        dir = r'images\\'
        imgs = [Image.open(dir+ii) for ii in os.listdir(dir)]
        shuffle(imgs)

        # Define size of grid, create, and show
        rows = 3
        cols = round(len(imgs)/rows)
        grid = imageGrid(imgs, rows, cols)

        # Write player name into empty grid space
        draw = ImageDraw.Draw(grid)
        w, h = grid.size
        draw.text((w-85,h-70), player, (255, 255, 255))
        grid.show()


if __name__ == "__main__":
    main()