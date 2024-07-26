from tkinter import Tk, Canvas
import datetime
from ed import ED

class CC(Tk):
    """A class to represent the cc window"""

    def __init__(self, fc1, fc2, f):
        super().__init__()
        # Set window title:
        self.title('SS - Countdown Calander')
        # Set class vars:
        self.FONT = f.replace(' ', '')
        self.ERROR = '{ERROR: DATE SHOULD BE IN THE FUTURE NOT IN THE PAST OR PRESENT}'
        self.FONT_COL1 = fc1
        self.FONT_COL2 = fc2
        self.events = self.get_events()
        self.today = datetime.date.today()
        self.vertical_space = 100
        # Set thecanvas:
        self.c = Canvas(self, width=800, height=800, bg=self.FONT_COL1)
        # Display the canvas:
        self.c.pack()
        # Set the title:
        self.c.create_text(100, 50, anchor='w', fill=self.FONT_COL2, font=f'{self.FONT} 28 underline', text=\
            'Countdown Calander')
        # Display the results:
        for event in self.events:
            event_name = event[0]
            day_until = self.days_bet_dates(event[1], self.today)
            if int(day_until) > 0:
                display = 'It is %s days until %s' % (day_until, event_name)
                self.c.create_text(100, self.vertical_space, anchor='w', fill=self.FONT_COL2, font=f'{self.FONT} 20', text=display)

            self.vertical_space += 30

    def get_events(self) -> list:
        """Gets the events from events.txt."""
        # Make a list for the extracted events:
        list_events = []
        d = datetime.date.today()
        with open('Txt_files\events.txt') as f:
            file_text = ED().decrypt(f.read())
        lines = file_text.split('\n')
        for l in lines:
            if not l == '':
                name = l.split(' on ')[0]
                str_date = l.split(' on ')[1]
                date_ = datetime.datetime.strptime(str_date, '%d/%m/%y').date()
                list_events.append([name, date_])
        # Return the final list:
        return list_events
    
    def days_bet_dates(self, date1:datetime.date, date2:datetime.date) -> int:
        """Return the days between date1 and date2"""
        time_between = str(date1 - date2)
        number_of_days = time_between.split(' ')
        return int(number_of_days[0])

if __name__ == '__main__':
    cc = CC('black', 'orange', 'Segoe Script')
    cc.mainloop()
