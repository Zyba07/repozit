import os 
import numpy as np 
import cv2
from typing import List, Dict
from varname.helpers import debug
import random

def load_gt(dataset_path: str): 
    gt_path = None
    gt_data= None
    gt_objects = {}
    for root, dirs, files in os.walk(dataset_path):
        for file_name in files:
            if 'gt.txt' == file_name: 
                gt_path = os.path.join(root, file_name)
    if not gt_path: 
        return None
    with open(gt_path, 'r') as f:
        gt_data = f.readlines()
    for gt_object in gt_data: 
        gt_object = gt_object.replace('\n', '').split(', ')
        for i in range(len(gt_object)):
            gt_object[i] = int(gt_object[i])
        frame_number, player_id, top_left_x, top_left_y, width, height, _, _, _ = gt_object 
        if frame_number not in gt_objects.keys(): 
            gt_objects[frame_number] = {}
        gt_objects[frame_number][player_id] = (top_left_x, top_left_y, width, height)
    return gt_objects

def load_img_paths(dataset_path: str) -> Dict[int, str]: 
    img_paths = {}
    for root, dirs, files in os.walk(dataset_path):
        for file_name in files:
            if '.jpg' in file_name and len(file_name) == 10: 
                frame_number = int(file_name[:-4])
                img_paths[frame_number] = os.path.join(root, file_name)
    return img_paths;


def run_dataset(dataset_path:str , outdir: str): 
    img_paths = load_img_paths(dataset_path)
    gt_objects = load_gt(dataset_path)
    max_player_id = 0
    for players in gt_objects.values():
        if max(players.keys()) > max_player_id:
            max_player_id = max(players.keys())
    players_colors_dict = random_players_colors(max_player_id)

    for frame_number, frame_objects in gt_objects.items():
        try: 
            img_path = img_paths[frame_number]
        except KeyError:
            continue
        img = cv2.imread(img_path)
        img2draw = img.copy() 
        for player_id, player_bbox in frame_objects.items():
            cv_bbox = xywh2x1y1x2y2(player_bbox)
            cv2.rectangle(
                    img2draw, 
                    #top left 
                    pt1=(cv_bbox[0], cv_bbox[1]),
                    #bottom rigth
                    pt2=(cv_bbox[2], cv_bbox[3]),
                    # color=(0,0,0),
                    color=players_colors_dict[player_id],
                    thickness=2)

        os.makedirs(outdir, exist_ok=True)
        img_out_path = os.path.join(outdir, os.path.basename(img_path))
        cv2.imwrite(img_out_path, img2draw)
        print('out written to', os.path.abspath(img_out_path))

def random_players_colors(max_player_id):
    players_colors = {}

    for i in range(max_player_id + 1):
        players_colors[i] = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    return players_colors


def xywh2x1y1x2y2(xywh_bbox: tuple):
    return (
            xywh_bbox[0],
            xywh_bbox[1],
            xywh_bbox[0] + xywh_bbox[2],
            xywh_bbox[1] + xywh_bbox[3]
        )
if __name__ == '__main__' :
    outdir = 'output'
    run_dataset('c:\cod\datasets', outdir);