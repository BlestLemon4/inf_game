pygame = None

current_img = 0
first = True

character_frames = []

img_to_load = None


def setup_characters(pygame_load):
    global pygame, img_to_load
    pygame = pygame_load
    load_character()
    return img_to_load


def load_character():
    global character_frames, img_to_load
    for i in range(4):
        img_path = "../resources/character/character_frame_" + str(i) + ".png"
        frame = pygame.image.load(img_path).convert_alpha()
        frame = pygame.transform.scale(frame, (300, 300))
        character_frames.append(frame)
    img_to_load = character_frames[0]


def get_character_frame():
    global character_frames, current_img, first
    if current_img == 0:
        if first:
            current_img = 2
        else:
            current_img = 1
            first = True
        return character_frames[0]
    elif current_img == 1:
        current_img = 0
        return character_frames[1]
    elif current_img == 2:
        if first:
            current_img = 3
            first = False
        else:
            current_img = 0
        return character_frames[2]
    elif current_img == 3:
        current_img = 0
        return character_frames[3]