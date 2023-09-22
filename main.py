from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    snake_x = 0
    snake_y = 0
    point = 0
    initial_text = "0 points"
    
    goal_x = CANVAS_WIDTH
    goal_y = CANVAS_WIDTH
    
    snake = create_snake(canvas, snake_x, snake_y)
    goal = create_goal(canvas, goal_x, goal_y)
    text_object = create_text_on_canvas(canvas, initial_text)
    current_direction = None
    while True: 
        new_direction = update_current_direction(canvas)
        if new_direction is not None:
            current_direction = new_direction
        snake_x, snake_y = update_snake_position(snake_x, snake_y, current_direction)
        canvas.moveto(snake, snake_x, snake_y)
        if check_bordelines(canvas, snake):
            canvas.delete(snake)
            canvas.delete(goal)
            snake, goal, snake_x, snake_y, point, current_direction = initialize_game(canvas)
            text = str(point) + " points"
            text_object = update_text_on_canvas(canvas, text_object, text, x=5, y=380)
        elif check_collision(canvas, snake, goal):
            goal_x, goal_y = get_new_goal_position()
            canvas.moveto(goal, goal_x, goal_y)
            point = increasing_points(point)
            text = str(point) + " points"
            text_object = update_text_on_canvas(canvas, text_object, text, x=5, y=380)
        time.sleep(DELAY)

        
def create_snake(canvas, snake_x, snake_y):
    return canvas.create_rectangle(snake_x, snake_y, snake_x + SIZE, snake_y + SIZE, "blue")

def create_goal(canvas, goal_x, goal_y):
    return canvas.create_rectangle(goal_x-2*SIZE, goal_y-2*SIZE, goal_x-SIZE, goal_y-SIZE, "salmon")

# Move the goal to a random new position
def get_new_goal_position():
    goal_x = random.randrange(0, CANVAS_WIDTH - 20, 20)
    goal_y = random.randrange(0, CANVAS_HEIGHT - 20, 20)
    return goal_x, goal_y

# Check for collision with the goal    
def check_collision(canvas, snake, goal):
    return canvas.get_left_x(snake) == canvas.get_left_x(goal) and canvas.get_top_y(snake) == canvas.get_top_y(goal)

def check_bordelines(canvas, snake):
    return canvas.get_left_x(snake) < 0 or canvas.get_left_x(snake) > 400 or canvas.get_top_y(snake) < 0 or canvas.get_top_y(snake) > 400
    
# Update snake's position based on the current_direction
def update_snake_position(snake_x, snake_y, current_direction):
    if current_direction == 'left':
        snake_x -= 20
    elif current_direction == 'right':
        snake_x += 20
    elif current_direction == 'up':
        snake_y -= 20
    elif current_direction == 'down':
        snake_y += 20
    return snake_x, snake_y

def update_current_direction(canvas):
    current_direction = None
    key = canvas.get_last_key_press()
    # Check for key presses, update current_direction accordingly
    # You may also want to add conditions to prevent snake from moving in the opposite direction
    if key == 'ArrowLeft': 
        current_direction = 'left'
    elif key == 'ArrowRight':
        current_direction = 'right'
    elif key == 'ArrowUp':
        current_direction = 'up'
    elif key == 'ArrowDown':
        current_direction = 'down'
    return current_direction

def increasing_points(point):
    return point+1
    
def create_text_on_canvas(canvas, text):
    return canvas.create_text(5, 380, text=text, font='Tohamo', font_size=16, color="black")
    
def update_text_on_canvas(canvas, text_object, new_text, x=5, y=380, font='Arial', font_size=16, color='black'):
    canvas.delete(text_object)
    updated_text_object = canvas.create_text(x, y, text=new_text, font=font, font_size=font_size, color=color)
    return updated_text_object

def initialize_game(canvas):
    snake_x, snake_y = 0, 0
    goal_x, goal_y = CANVAS_WIDTH, CANVAS_HEIGHT

    snake = create_snake(canvas, snake_x, snake_y)
    goal = create_goal(canvas, goal_x, goal_y)
    current_direction = None
    point = 0

    return snake, goal, snake_x, snake_y, point, current_direction
if __name__ == '__main__':
    main()