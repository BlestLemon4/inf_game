pygame = None

current_img = 0
first = True

dr_magnus_blackthorn_0 = None
dr_magnus_blackthorn_1 = None
dr_magnus_blackthorn_2 = None
dr_magnus_blackthorn_3 = None

selected_character = 0

img_to_load = None


def setup_characters(pygame_load):
    global pygame, img_to_load
    pygame = pygame_load
    if selected_character == 0:
        setup_dr_magnus_blackthorn()
    elif selected_character == 1:
        pass
    elif selected_character == 2:
        pass
    elif selected_character == 3:
        pass
    return img_to_load

def setup_dr_magnus_blackthorn():
    global dr_magnus_blackthorn_0, dr_magnus_blackthorn_1, dr_magnus_blackthorn_2, dr_magnus_blackthorn_3, img_to_load
    dr_magnus_blackthorn_0 = pygame.image.load("../img\characters\dr_magnus_blackthorne\dr_magnus_blackthorne-0.png").convert_alpha()
    dr_magnus_blackthorn_0 = pygame.transform.scale(dr_magnus_blackthorn_0, (300, 300))
    img_to_load = dr_magnus_blackthorn_0

    dr_magnus_blackthorn_1 = pygame.image.load("../img\characters\dr_magnus_blackthorne\dr_magnus_blackthorne-1.png").convert_alpha()
    dr_magnus_blackthorn_1 = pygame.transform.scale(dr_magnus_blackthorn_1, (300, 300))

    dr_magnus_blackthorn_2 = pygame.image.load("../img\characters\dr_magnus_blackthorne\dr_magnus_blackthorne-2.png").convert_alpha()
    dr_magnus_blackthorn_2 = pygame.transform.scale(dr_magnus_blackthorn_2, (300, 300))

    dr_magnus_blackthorn_3 = pygame.image.load("../img\characters\dr_magnus_blackthorne\dr_magnus_blackthorne-3.png").convert_alpha()
    dr_magnus_blackthorn_3 = pygame.transform.scale(dr_magnus_blackthorn_3, (300, 300))


def get_character():
    global dr_magnus_blackthorn_0, dr_magnus_blackthorn_1, dr_magnus_blackthorn_2, dr_magnus_blackthorn_3, current_img, first
    if selected_character == 0:
        if current_img == 0:
            if first:
                current_img = 2
            else:
                current_img = 1
                first = True
            return dr_magnus_blackthorn_0
        elif current_img == 1:
            current_img = 0
            return dr_magnus_blackthorn_1
        elif current_img == 2:
            if first:
                current_img = 3
                first = False
            else:
                current_img = 0
            return dr_magnus_blackthorn_2
        elif current_img == 3:
            current_img = 0
            return dr_magnus_blackthorn_3

