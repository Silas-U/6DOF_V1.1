from machine import Pin
from time import sleep
class KeyPad4x4:
    
    # CONSTANTS
    KEY_UP   = const(0)
    KEY_DOWN = const(1)
    
    keys = [['1', '4', '7', '*'], ['2', '5', '8', '0'], ['3', '6', '9', '#'], ['A', 'B', 'C', 'D']]
    
    #constructor set (row,col) pins for keypad
    def __init__(self, c1,c2,c3,c4,r1,r2,r3,r4):
        self.cols = [c1,c2,c3,c4]
        self.rows = [r1,r2,r3,r4]
    
    
    def row_pins(self):
        # set pins for rows as outputs
        row_pins = [Pin(pin_name, mode=Pin.OUT) for pin_name in self.rows]
        return row_pins
    
    def col_pins(self):
        # set pins for cols as inputs
        col_pins = [Pin(pin_name, mode=Pin.IN, pull=Pin.PULL_DOWN) for pin_name in self.cols]
        return col_pins

    def init(self):
        for row in range(0,4):
            for col in range(0,4):
                self.row_pins()[row].value(0)

    def scan(self, row, col):
        """ scan the keypad """
        # set the current column to high
        self.row_pins()[row].value(1)
        key = None
        # check for keypressed events
        if self.col_pins()[col].value() == self.KEY_DOWN:
            key = self.KEY_DOWN
        if self.col_pins()[col].value() == self.KEY_UP:
            key = self.KEY_UP
        self.row_pins()[row].value(0)
        # return the key state
        return key
    
    print("starting")

    def onPress(self):
        # set all the columns to low
        while True:
            for row in range(4):
                for col in range(4):
                    key = self.scan(row, col)
                    if key == self.KEY_DOWN:
                        last_key_press = self.keys[row][col]
                        return last_key_press
                        



