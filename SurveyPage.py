from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.animation import Animation

Builder.load_string('''
<LinePlayground>:
    
    Label:
        text: 'Please slide the sliders based on the emotions you are feeling currently.'
    
    GridLayout:
        cols: 2
        size_hint: 0.81, None
        height: 44 * 5

        GridLayout:
            cols: 2

            Label:
                text: 'Anger'
            Slider:
                value: root.anger
                on_value: root.anger = float(args[1])
                min: 0.
                max: 10.
            Label:
                text: 'Calmness'
            Slider:
                value: root.calmness
                on_value: root.calmness = float(args[1])
                min: 0.
                max: 10.
            Label:
                text: 'Happiness'
            Slider:
                value: root.happiness
                on_value: root.happiness = float(args[1])
                min: 0.
                max: 10.
            Label:
                text: 'Fear'
            Slider:
                value: root.fear
                on_value: root.fear = float(args[1])
                min: 0.
                max: 10.

''')


class LinePlayground(FloatLayout):

    anger, calmness, happiness, fear = 0, 0, 0, 0
    clicked = False


class SurveyPage(App):

    def build(self):
        return LinePlayground()


'''
class Button(App):
    def animate(self, instance):
        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(200, 100), t='out_bounce')
        animation &= Animation(size=(500, 500))
        animation += Animation(size=(100, 50))
        animation.start(instance)

    def build(self):
        button = Button(size_hint=(None, None), text='plop',
                        on_press=self.animate)
        return button
'''

if __name__ == '__main__':
    SurveyPage().run()
