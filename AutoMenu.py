# Auto Menu V 1.01
#
# Stuart Macintosh - 14/11/2015.

try:
    from msvcrt import getch
except:
    print "This module requires the module 'msvcrt' in order to run."

class Menu(object):

    def __init__(self, menu_options):
        """ Menu(menu_options)\n\n e.g. Menu(["opt 1", "opt 2"])"""

        # Initialise instance variables
        self.options = menu_options
        self.option = 0
        self.active = True

        self.__menu_left_arrow =   " --> "
        self.__menu_right_arrow =  " <-- "
        self.__menu_no_arrow =     "     "
        self.__menu_left_side = None
        self.__menu_right_side = None
        self.__max_str_size = 0
        self.__menu_padding = []
        self.__menu_pad = " "

        # Find the longest word in available options to make the menu symetrical.
        for option in self.options:
            if self.__max_str_size < len(option):
                self.__max_str_size = len(option)

        # Option padding = Length of longest option text - current option text. Stored in a list.
        for option in self.options:
            self.__menu_padding.append(self.__max_str_size - len(option))


    def draw(self):

        # Ensure menu_option stays within the range of available options.
        if self.option > (len(self.options) - 1):
            self.option = (len(self.options) - len(self.options)) # Makes menu_option 0.
        elif self.option < (len(self.options) - len(self.options)):
            self.option = (len(self.options) - 1)

        # Draw the menu.
        for menu in range(len(self.options)):

            # Append selection arrows to the currently highlighted option.
            if self.option == menu:
                self.__menu_left_side = self.__menu_left_arrow
                self.__menu_right_side = self.__menu_right_arrow
            else:
                self.__menu_left_side = self.__menu_no_arrow
                self.__menu_right_side = self.__menu_no_arrow

            # Draw menu line.
            print self.__menu_left_side + str(menu) + " - " + self.options[menu]\
             + (self.__menu_pad * self.__menu_padding[menu]) + self.__menu_right_side


    def get_key(self):
        """ Returns the detected keyboard input.\
        \n\nget_gey() -> "key" """

        while True: # Must run in a continous loop to monitor for keys.
            self.detected_key = ""
            self.key = ord(getch())

            if self.key == 72:
                self.detected_key = "Up"
                return self.detected_key

            elif self.key == 80:
                self.detected_key = "Down"
                return self.detected_key

            elif self.key == 27:
                self.detected_key = "Esc"
                return self.detected_key

            elif self.key == 13:
                self.detected_key = "Enter"
                return self.detected_key

if __name__ == '__main__':
    print "This script is designed to be imported as a module."
