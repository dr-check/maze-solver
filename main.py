from tkinter import Tk, BOTH, Canvas
import time


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.geometry(f"{width}x{height}")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.position = ()
    
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
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        start = Point((self.position.x1 + self.position.x2) / 2, (self.position.y1 + self.position.y2) / 2)
        stop = Point((to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2)
        move = Line(start, stop)
        self.draw_line(move, fill_color)
        self.position = to_cell

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
    def __init__(self, Window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = -1
        self.x2 = -1
        self.y1 = -1
        self.y2 = -1
        self.__win = Window

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.has_left_wall:
            left_line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.__win.draw_line(left_line, "black")
        elif not self.has_left_wall:
            left_line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.__win.draw_line(left_line, "#d9d9d9")

        if self.has_right_wall:
            right_line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.__win.draw_line(right_line, "black")
        elif not self.has_right_wall:
            right_line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.__win.draw_line(right_line, "#d9d9d9")

        if self.has_top_wall:
            top_line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.__win.draw_line(top_line, "black")
        elif not self.has_top_wall:
            top_line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.__win.draw_line(top_line, "#d9d9d9")

        if self.has_bottom_wall:
            bottom_line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.__win.draw_line(bottom_line, "black")
        elif not self.has_bottom_wall:
            bottom_line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.__win.draw_line(bottom_line, "#d9d9d9")    

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.__cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        if self.__num_rows > 0 and self.__num_cols > 0:
            self.__cells[0][0].has_top_wall = False
            self.__draw_cell(0, 0)
            self.__cells[15][11].has_bottom_wall = False
            self.__draw_cell(15, 11)
            


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._Maze__break_entrance_and_exit()
    win.wait_for_close()

if __name__ == "__main__":
    main()
    print("Window closed.")
            