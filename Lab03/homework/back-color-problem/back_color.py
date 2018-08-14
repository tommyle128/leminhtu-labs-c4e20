from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes

def generate_quiz():
    text_list = []
    color_list = []

    for detail in shapes:
        text_list.append(detail['text'])
        color_list.append(detail['color'])
    
    quiz = [
        choice(text_list).upper(),
        choice(color_list),
        randint(0, 1)
    ]
    
    return quiz

    
def mouse_press(x, y, text, color, quiz_type):
    from inside import is_inside
    
    point = [x, y]
    rect_detail = []

    for detail in shapes:
        rect_detail = detail['rect']
        press = is_inside(point, rect_detail)
        if press:
            if quiz_type == 1:
                if detail['color'] == color:
                    return True
                else:
                    return False
            elif quiz_type == 0:
                if detail['text'].upper() == text:
                    return True
                else:
                    return False

    
    
    

    





    


