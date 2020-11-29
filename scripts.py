import curses
import apis

class ApiAppScreen():

    def __init__(self, stdsrc):
        self.screen = stdsrc
        self.current_option = 0
        self.y, self.x = stdsrc.getmaxyx()
        self.options = {
            112: ('{:{}{}}'.format('BE PLENTIFUL', '^', self.x), apis.r_u_a_coach__q),
            110: ('{:{}{}}'.format('BE NICE TO YOUR CAT', '^', self.x), apis.cat_fcat),
            107: ('{:{}{}}'.format('BE KNOWLEDGEABLE', '^', self.x), apis.a_quote),
            114: ('{:{}{}}'.format('BE AWARE OF THE TIME', '^', self.x), apis.do_an_echo)
        }
        self.app()

    def run_command(self, bt_num):
        up_button = 259
        do_button = 258
        ex_button = 27
        en_buttons = [10, 112, 110, 107]

        if bt_num == up_button:
            self.current_option -= 1
        elif bt_num == do_button:
            self.current_option += 1
        elif bt_num in en_buttons:
            self.choice(bt_num)
        elif bt_num == ex_button:
            SystemExit()

        self.current_option %= len(self.options)

    def choice(self, bt_num):
        choice_made = list(self.options.values())[self.current_option][1]
        if bt_num != 10:
            choice_made = self.options[bt_num][1]
        text = choice_made()
        self.display(text)


    def app(self):
        while True:
            self.screen.clear()
            curses.noecho()
            curses.curs_set(False)

            self.menu()

            self.screen.refresh()
            command = self.screen.getch()
            self.run_command(command)

    def menu(self):
        for index, option in enumerate(self.options.values()):
            y_axis = (self.y//2)-(len(self.options)//2-index)
            x_axis = 0
            self.screen.addstr(y_axis, x_axis, option[0])
            if index == self.current_option:
                self.screen.addstr(y_axis, x_axis, option[0], curses.A_STANDOUT)
    
    def display(self, text):
        # text = text.encode(encoding='UTF-8',errors='strict')
        identation = [text[i:i+self.x] for i in range(0, len(text), self.x)]

        self.screen.clear()
        curses.noecho()
        curses.curs_set(False)

        for index, text in enumerate(identation):
            y_axis = (self.y//2)-(len(self.options)//2-index)
            self.screen.addstr(y_axis, 0, '{:{}{}}'.format(text, '^',self.x))

            self.screen.refresh()
        self.screen.getch()


if __name__ == "__main__":
    aas = curses.wrapper(ApiAppScreen)
