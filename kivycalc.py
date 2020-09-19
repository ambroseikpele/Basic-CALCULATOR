from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Sire(BoxLayout):
    def __init__(self, **kwargs):
        super(Sire, self).__init__(**kwargs)
        self.num1=str()
        self.orientation='vertical'
        self.lbl=Label(text=self.num1, color=(1,1,1,1))
        self.add_widget(self.lbl)
        self.grid=GridLayout()
        self.grid.cols=4
        self.add_widget(self.grid)
        self.grid.add_widget(Button(text="9", on_press=self.nine))
        self.grid.add_widget(Button(text="8", on_press=self.eight))
        self.grid.add_widget(Button(text="7", on_press=self.seven))
        self.grid.add_widget(Button(text="/", on_press=self.divide))
        self.grid.add_widget(Button(text="6", on_press=self.six))
        self.grid.add_widget(Button(text="5", on_press=self.five))
        self.grid.add_widget(Button(text="4", on_press=self.four))
        self.grid.add_widget(Button(text="*", on_press=self.times))
        self.grid.add_widget(Button(text="3", on_press=self.three))
        self.grid.add_widget(Button(text="2", on_press=self.two))
        self.grid.add_widget(Button(text="1", on_press=self.one))
        self.grid.add_widget(Button(text="-", on_press=self.minus))
        self.grid.add_widget(Button(text="0", on_press=self.zero))
        self.grid.add_widget(Button(text=".", on_press=self.dot))
        self.grid.add_widget(Button(text="=", on_press=self.equal))
        self.grid.add_widget(Button(text="+", on_press=self.add))

    def nine(self, instance):
        self.num1=self.num1+'9'
        self.lbl.text=self.num1
    def eight(self, instance):
        self.num1=self.num1+'8'
        self.lbl.text=self.num1
    def seven(self, instance):
        self.num1=self.num1+'7'
        self.lbl.text=self.num1
    def divide(self, instance):
        self.num1=self.num1+' / '
        self.lbl.text=self.num1
    def six(self, instance):
        self.num1=self.num1+'6'
        self.lbl.text=self.num1
    def five(self, instance):
        self.num1=self.num1+'5'
        self.lbl.text=self.num1
    def four(self, instance):
        self.num1=self.num1+'4'
        self.lbl.text=self.num1
    def times(self, instance):
        self.num1=self.num1+' * '
        self.lbl.text=self.num1
    def three(self, instance):
        self.num1=self.num1+'3'
        self.lbl.text=self.num1
    def two(self, instance):
        self.num1=self.num1+'2'
        self.lbl.text=self.num1
    def one(self, instance):
        self.num1=self.num1+'1'
        self.lbl.text=self.num1
    def minus(self, instance):
        self.num1=self.num1+' - '
        self.lbl.text=self.num1
    def zero(self, instance):
        self.num1=self.num1+'0'
        self.lbl.text=self.num1
    def dot(self, instance):
        self.num1=self.num1+'.'
        self.lbl.text=self.num1
    def equal(self, instance):
        try:
            self.lbl.text=(str(eval(f'{self.num1}')))
        except :
            self.lbl.text=('Invalid')
        
        self.num1=""
    def add(self, instance):
        self.num1=self.num1+' + '
        self.lbl.text=self.num1

class Sire_Ambrose(App):
    def build(self):
        return Sire()

if __name__ == '__main__':
    Sire_Ambrose().run()
