
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import hangman



class Launcher(App):
    def __init__(self):
        super(Launcher,self).__init__()
    #create all the buttons in within this insatnce
        self.game1= Button(text="Hangman")
        self.game2= Button(text="Game 2")
        self.game3= Button(text="Game 3")



    #this definition is used to bind the buttons created to commands
    def build(self):
        self.game1.bind(on_press = self.launchHangman)
        self.game2.bind(on_press= self.launchGame2)
        self.game3.bind(on_press= self.launchGame3)


        #creae the layout within the build(this layout is a vertical window with the buttons stacked on top of one another)
        layout = BoxLayout()
        layout.orientation='vertical'

        #after the layout is created, we are adding the buttons above into the layout and returning the layout variable
        layout.add_widget(self.game1)
        layout.add_widget(self.game2)
        layout.add_widget(self.game3)


        return layout

    def launchHangman(self,arg):
        hangman.main()
        exit()


    def launchGame2(self,arg):
        pass


    def launchGame3(self,arg):
        pass




window=Launcher()

window.run()
