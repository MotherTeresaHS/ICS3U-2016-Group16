#Created by: Margaret Venes
#Created for: ICS3U
#This program of my final project
#The program calculates the equivalent numerical grade when the level is inputted

import ui
import speech

def marks_equivalent(grade):
  if grade == "4+" or grade == "4" or grade == "4-" or grade == "3+" or grade == "3" or grade == "3-" or grade == "2+" or grade == "2" or grade == "2-" or grade == "1+" or grade == "1" or grade == "1-" or grade == "R" or grade == "NE":
  	
	   	if grade == "4+":
	   		grade = 95
	   	elif grade == "4":
	   		grade = 87
	   	elif grade == "4-":
	   		grade = 80
	   	elif grade == "3+":
	   		grade = 77
	   	elif grade == "3":
	   		grade = 73
	   	elif grade == "3-":
	   		grade = 70
	   	elif grade == "2+":
	   	  grade = 65
	   	elif grade == "2":
	   	  grade = 63
	   	elif grade == "2-":
	   	  grade = 60
	   	elif grade == "1+":
	   	  grade = 57
	   	elif grade == "1":
	   	  grade = 53
	   	elif grade == "1-":
	   		grade = 50
	   	elif grade == "R":
	   		grade = 30
	   	elif grade == "NE":
	   	  grade = 0
  else:
  	speech.say("Please put proper values")
  	view['wrong_label'].text = "Please put proper values"
  	
  return grade	

def calculate_button_touch_up_inside(sender):
	#input 
  knowledge = str(view['knowledge_textfield'].text)
  thinking = str(view['thinking_textfield'].text)
  communication = str(view['communication_textfield'].text)
  application = str(view['application_textfield'].text)
  
  knowledge = marks_equivalent(knowledge)
  thinking = marks_equivalent(thinking)
  communication = marks_equivalent(communication)
  application = marks_equivalent(application)
  
  knowledge = (knowledge*0.25)
  thinking = (thinking*0.20)
  communication = (communication*0.10)
  application = (application*0.15)
  total = (knowledge + thinking + communication + application)/0.7
  view['average_label'].text = format(str(round(total,1)))
  
def clear_button_touch_up_inside(sender):
	
    # clears the fields
    #print("CLEARED")
    view['knowledge_textfield'].text = ""
    view['communication_textfield'].text = ""
    view['thinking_textfield'].text = ""
    view['application_textfield'].text = ""
    view['average_label'].text = ""
    view['wrong_label'].text = ""

view = ui.load_view()
view.present(style = 'fullscreen', hide_title_bar = True)	 
