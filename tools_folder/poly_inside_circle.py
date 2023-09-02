import cv2
import numpy as np

def polygon_inside_circle(
        img,
        vertex_count,
        center,
        radius,
        color,
        thickness
    ):
    imgtodraw = img.copy()
    step_angle = 360 / vertex_count
    current_angle = 0
    points = []
    for i in range(vertex_count):
        x = radius * np.cos(np.deg2rad(current_angle))
        y = radius * np.sin(np.deg2rad(current_angle))
        current_angle += step_angle 
        points.append(
            [
                int(round(x + center[0], 0)),
                int(round(y + center[1], 0)),
            ]
        )
    points = np.array(points, np.int32)
    print(points)
    cv2.polylines(
        imgtodraw,
        [points],
        True,
        color,
        thickness
    )
    return imgtodraw

image_path = 'test_data\jeezus.jpg'
image = cv2.imread(image_path)
print(image.shape)
imgtodraw = image.copy()
imgtodraw = cv2.resize(
    imgtodraw, 
    dsize=None,
    fx=0.7,
    fy=0.7
)
for n_angle in range(3, 360):
    
    imgtodraw_with_poly = polygon_inside_circle(
        imgtodraw, 
        vertex_count=n_angle,
        center=(250, 250),
        radius=20*n_angle,
        color=(250, 30, 100),
        thickness=3
    )
    # imgtodraw = polygon_inside_circle(
    #     imgtodraw, 
    #     vertex_count=n_angle,
    #     center=(400, 200),
    #     radius=20*n_angle,
    #     color=(250, 30, 100),
    #     thickness=3
    # )
    cv2.imshow('poly',imgtodraw_with_poly)
    cv2.waitKey(150)
