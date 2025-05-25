from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.geometry(f"{width}x{height}")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, Line, fill_color):
        Line.draw(self.canvas, fill_color)
        

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = -1
        self.x2 = -1
        self.y1 = -1
        self.y2 = -1
        self.__win = Window

    def draw(self, x, y):
        self.x1 = x
        self.y1 = y
        self.x2 = x+30
        self.y2 = y+30
        if self.has_left_wall:
            left_line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.__win.draw_line(left_line, "black")
        if self.has_right_wall:
            right_line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.__win.draw_line(right_line, "black")
        if self.has_top_wall:
            top_line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.__win.draw_line(top_line, "black")
        if self.has_bottom_wall:
            bottom_line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.__win.draw_line(bottom_line, "black")


def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(100, 100)
    cell.draw(200, 100)
    cell.draw(300, 100)
    cell.draw(400, 100)
    win.wait_for_close()

if __name__ == "__main__":
    main()
    print("Window closed.")
            