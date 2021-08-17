from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for file in img_files:
            image_surf = pygame.image.load(path + '/' + file).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
