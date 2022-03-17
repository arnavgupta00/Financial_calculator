
from turtle import onrelease
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner




Window.clearcolor = (1,1,1,1)
f_text =''

class Sip_Calculator(App):

    def sip_calculator(self,obj):
        
        try:
            
            y  = int(self.year.text)
            x  = int(self.inv.text)
            z  = (int(self.roi.text))/100

            regular_inv = x
            
            text_m = ''
            start_txt = f'Regular Investment = {x}\n --------------------------------------- \n {1} Period  |  Profit {0}  |  Total Revenue {x}'
            
            for period in range (2,(y*compound_interval)+2):

                regular_inv += (z/compound_interval)*regular_inv + x
                
                mid_txt = f'\n {period} Period  |  Profit {round(regular_inv -(x*period),2)}  |  Total Revenue {round(regular_inv ,2)}'
                text_m += mid_txt
                
                
            
            global f_text
            f_text = start_txt + text_m    
            print(f_text)
            
            
        except:
            print('Try again!!!')  
    
    def compound_calc(self,obj):
        
        try:
            
            y  = int(self.year.text)
            x  = int(self.inv.text)
            z  = (int(self.roi.text))/100
            
            
            
            text_m = ''
            start_txt = f'Investment = {x}\n ---------------------------------------'

            global interest_type
            global compound_interval

            power = compound_interval*y

            res = round((x)*(1+ z/interest_type*compound_interval)**(power),2)

            text_m = f'Initial Balance = {x}  \n---------------------- \nFuture investment value = {res} \n---------------------- \nTotal interest earned = {round(res - x,2)} \n---------------------- \n' 

            global f_text
            f_text = text_m 

            print(f_text)
                       
            
        except:
            print('Try again!!!') 

    def simple_interest(self,obj):
        
        try:
            
            y  = int(self.year.text)
            x  = int(self.inv.text)
            z  = (int(self.roi.text))/100
            
            
            
            text_m = ''
            start_txt = f'Investment = {x}\n ---------------------------------------'

            global interest_type
            global compound_interval

            

            res = round((x)*(1+ (z*y)),2)

            text_m = f'Initial Balance = {x}  \n---------------------- \nFuture investment value = {res} \n---------------------- \nTotal interest earned = {round(res - x,2)} \n---------------------- \n' 

            global f_text
            f_text = text_m 

            print(f_text)
                       
            
        except:
            print('Try again!!!') 

    def header_credits(self,obj):
        try:
            bluff = 'hehehehe' + 12
        except:
            global f_text
            f_text = 'Created By Arnav Gupta \n--------------------------------\nFor Any Query Contact me on - arnavguptagg@gmail.com'
    
    
    def pop_cont(FloatLayout):
        l = Label(text=f_text)
        return l
    def show_popup(self,pop_cont):
        con = self.pop_cont()
        popup = Popup(title = 'Results', content= con,size_hint=(0.6,0.7))
        popup.open()

    def build(self):
        
        ####################################
        float_layout = FloatLayout()
        page_layout = PageLayout()
        #####################################
        self.inv_label = Label(text ='Initial / Regular Investment',
            pos_hint={'center_x':0.3,'center_y':0.8},
            color=(0.945, 0.298, 0.22),
            bold = True,
            font_size ='20px'
        )
        self.inv = TextInput(text='',
            pos_hint={'center_x':0.7,'center_y':0.8},
            size_hint= (0.3,0.05),
             
        )
        self.year_label = Label(text= 'Number of years',
            pos_hint={'center_x':0.3,'center_y':0.7},
            color=(0.945, 0.298, 0.22),
            bold = True,
            font_size ='20px'
        )
        self.year = TextInput(text='',
            pos_hint={'center_x':0.7,'center_y':0.7},
            size_hint= (0.3,0.05)       
        )
        self.roi_label = Label(text = 'Interest %',
            pos_hint={'center_x':0.3,'center_y':0.6},
            color=(0.945, 0.298, 0.22),
            bold = True,
            font_size ='20px'
        )
        self.roi = TextInput(text='',
            pos_hint={'center_x':0.7,'center_y':0.6}, 
            size_hint= (0.3,0.05)
        )
        self.i_ment_label = Label(text = 'Installment',
            pos_hint={'center_x':0.3,'center_y':0.5},
            color=(0.945, 0.298, 0.22),
            bold = True,
            font_size ='20px'
        )
        self.i_ment = TextInput(text='',
            pos_hint={'center_x':0.7,'center_y':0.5}, 
            size_hint= (0.3,0.05)
        )
        self.submit  = Button(
            text = 'Submit',
            on_press= self.sip_calculator,
            pos_hint={'center_x':0.83,'center_y':0.7}, 
            size_hint= (0.3,0.1),
            background_color =(0.945, 0.298, 0.22)
        )
        self.sip_calc  = Button(
            text = 'Sip Calculator',
            on_press= self.sip_calculator,
            bold = True,
            on_release = self.show_popup,
            pos_hint={'center_x':0.5,'center_y':0.1}, 
            size_hint= (0.3,0.07),
            #background_color =(0.945, 0.298, 0.22,1),
            color=(0.945, 0.298, 0.22)
        )
        self.simple_calc = Button(
            text = 'Simple interest',
            on_press= self.simple_interest,
            bold = True,
            on_release = self.show_popup,
            pos_hint={'center_x':0.3,'center_y':0.25}, 
            size_hint= (0.3,0.09),
            #background_color =(0.945, 0.298, 0.22,1),
            color=(0.945, 0.298, 0.22)
        )
        self.comp_calc = Button(
            text = 'Compound interest',
            on_press= self.compound_calc,
            bold = True,
            on_release = self.show_popup,
            pos_hint={'center_x':0.7,'center_y':0.25}, 
            size_hint= (0.3,0.09),
            #background_color =(0.945, 0.298, 0.22,1),
            color=(0.945, 0.298, 0.22)
        )
        interest_type =[]
        self.dropdown = Spinner(
            
            text = 'Interest Type',
            values = ['Yearly' , 'Monthly' ,'Weekly', 'Daily'],
            color=(0.945, 0.298, 0.22),
            pos_hint={'center_x':0.45,'center_y':0.6}, 
            size_hint= (0.15,0.05),
            
        )
        def dropdown_return(spinner,text):
            global interest_type
            
            if text == 'Yearly':
                interest_type =1 
            elif text == 'Monthly':
                interest_type =12
            elif text == 'Weekly':
                interest_type = 52
            elif text == 'Daily':
                interest_type = 365

        self.dropdown.bind(text = dropdown_return)

        self.compound_interval = Spinner(
            
            text = 'Inverval',
            values = ['Yearly' , 'Monthly' ,'Weekly', 'Daily'],
            color=(0.945, 0.298, 0.22),
            pos_hint={'center_x':0.5,'center_y':0.45}, 
            size_hint= (0.2,0.05),
        )

        def interval_return(spinner,text):
            global compound_interval
            
            if text == 'Yearly':
                compound_interval = 1 
            elif text == 'Monthly':
                compound_interval = 12
            elif text == 'Weekly':
                compound_interval = 52
            elif text == 'Daily':
                compound_interval = 365
            

        self.compound_interval.bind(text = interval_return)

        


        self.header = Button(text = 'Financial Calculator',
            bold = True,
            font_size ='40px',
            pos_hint={'center_x':0.5,'center_y':0.95},
            size_hint= (1.1,0.1),
            color=(0.945, 0.298, 0.22),
            on_press = self.header_credits,
            on_release = self.show_popup
        )
        


        ##################################################
        float_layout.add_widget(self.inv)
        float_layout.add_widget(self.inv_label)
        float_layout.add_widget(self.year)
        float_layout.add_widget(self.year_label)
        float_layout.add_widget(self.roi)
        float_layout.add_widget(self.roi_label)
        #float_layout.add_widget(self.submit)
        float_layout.add_widget(self.sip_calc)
        float_layout.add_widget(self.simple_calc)
        float_layout.add_widget(self.comp_calc)
        float_layout.add_widget(self.header)
        #float_layout.add_widget(self.i_ment_label)
        #float_layout.add_widget(self.i_ment)
        float_layout.add_widget(self.dropdown)
        float_layout.add_widget(self.compound_interval)
        
        ###################################################
        

        
        return float_layout 
        
    



if __name__ =="__main__":
    Sip_Calculator().run()
