#Created by: Margaret Venes
#Created for: ICS3U
#This program of my final project
#The program calculates the equivalent numerical grade when the level is inputted

import ui
import speech 


def calculate_button_touch_up_inside(sender):
  knowledge = str(view['knowledge_textfield'].text)
  if knowledge == "4+" or knowledge == "4" or knowledge == "4-" or knowledge == "3+" or knowledge == "3" or knowledge == "3-" or knowledge == "2+" or knowledge == "2" or knowledge == "2-" or knowledge == "1+" or knowledge == "1" or knowledge == "1-" or knowledge == "R" or knowledge == "NE":
	   	
	   	if knowledge == "4+":
	   		knowledge = 95
	   	elif knowledge == "4":
	   		knowledge = 87
	   	elif knowledge == "4-":
	   		knowledge = 80
	   	elif knowledge == "3+":
	   		knowledge = 77
	   	elif knowledge == "3":
	   		knowledge = 73
	   	elif knowledge == "3-":
	   		knowledge = 70
	   	elif knowledge == "2+":
	   	  knowledge = 65
	   	elif knowledge == "2":
	   	  knowledge = 63
	   	elif knowledge == "2-":
	   	  knowledge = 60
	   	elif knowledge == "1+":
	   	  knowledge = 57
	   	elif knowledge == "1":
	   	  knowledge = 53
	   	elif knowledge == "1-":
	   		knowledge == 50
	   	elif knowledge == "R":
	   		knowledge == 30
	   	elif knowledge == "NE":
	   	  knowledge = 0
  else:
  	speech.say("Please put proper values for knowledge")
  	view['knowledge_alert_label'].text = '?'
  	#Thinking process
  thinking = str(view['thinking_textfield'].text)
  if thinking == "4+" or thinking == "4" or thinking == "4-" or thinking == "3+" or thinking == "3" or thinking == "3-" or thinking == "2+" or thinking == "2" or thinking == "2-" or thinking == "1+" or thinking == "1" or thinking == "1-" or thinking == "R" or thinking == "NE":
	   	
	   	if thinking == "4+":
	   		thinking = 95
	   	elif thinking == "4":
	   		thinking = 87
	   	elif thinking == "4-":
	   		thinking = 80
	   	elif thinking == "3+":
	   		thinking = 77
	   	elif thinking == "3":
	   		thinking = 73
	   	elif thinking == "3-":
	   		thinking = 70
	   	elif thinking == "2+":
	   	  thinking = 65
	   	elif thinking == "2":
	   	  thinking = 63
	   	elif thinking == "2-":
	   	  thinking = 60
	   	elif thinking == "1+":
	   	  thinking = 57
	   	elif thinking == "1":
	   	  thinking = 53
	   	elif thinking == "1-":
	   		thinking = 50
	   	elif thinking == "R":
	   		thinking == 30
	   	elif thinking == "NE":
	   	  thinking = 0
  else:
  	speech.say("Please put proper values for thinking")
  	view['thinking_alert_label'].text = '?'
  #Application output
  application = str(view['application_textfield'].text)
  if application == "4+" or application == "4" or application == "4-" or application == "3+" or application == "3" or application == "3-" or application == "2+" or application == "2" or application == "2-" or application == "1+" or application == "1" or application == "1-" or application == "R" or application == "NE":
	
	   	if application == "4+":
	   		application = 95
	   	elif application == "4":
	   		application = 87
	   	elif application == "4-":
	   		application = 80
	   	elif application == "3+":
	   		application = 77
	   	elif application == "3":
	   		application = 73
	   	elif application == "3-":
	   		application = 70
	   	elif application == "2+":
	   	  application = 65
	   	elif application == "2":
	   	  application = 63
	   	elif application == "2-":
	   	  application = 60
	   	elif application == "1+":
	   	  application = 57
	   	elif application == "1":
	   	  application = 53
	   	elif application == "1-":
	   	  application = 50
	   	elif application == "R":
	   		application == 30
	   	elif application == "NE":
	   	  application = 0
  else:
  	speech.say("Please put proper values for application")
  	view['application_alert_label'].text = '?'
   #Comminication output
  communication = str(view['communication_textfield'].text)
  if communication == "4+" or communication == "4" or communication == "4-" or communication == "3+" or    communication == "3" or communication == "3-" or communication == "2+" or communication == "2" or communication == "2-" or communication == "1+" or communication == "1" or communication == "1-" or communication == "R" or communication == "NE":
	   	
	   	if communication == "4+":
	   		communication = 95
	   	elif communication == "4":
	   		communication = 87
	   	elif communication == "4-":
	   		communication = 80
	   	elif communication == "3+":
	   		communication = 77
	   	elif communication == "3":
	   		communication = 73
	   	elif communication == "3-":
	   		communication = 70
	   	elif communication == "2+":
	   	  communication = 65
	   	elif communication == "2":
	   	  communication = 63
	   	elif communication == "2-":
	   	  communication = 60
	   	elif communication == "1+":
	   	  communication = 57
	   	elif communication == "1":
	   	  communication = 53
	   	elif communication == "1-":
	   	  communication = 50
	   	elif communication == "R":
	   		communication == 30
	   	elif communication == "NE":
	   	  communication = 0
  else:
  	speech.say("Please put proper values for communication")
  	view['communication_alert_label'].text = '?'
    
  knowledge_average = (knowledge*0.25)
  thinking_average = (thinking*0.20)
  communication_average = (communication*0.10)
  application_average = (application*0.15) 	
  total = (knowledge_average + thinking_average + communication_average + application_average)/0.7
  view['average_label'].text = format(str(round(total,1)))
  
def clear_button_touch_up_inside(sender):
  view['knowledge_textfield'].text = ""
  view['communication_textfield'].text = ""
  view['thinking_textfield'].text = ""
  view['application_textfield'].text = ""
  view['average_label'].text = ""
  view['knowledge_alert_label'].text = ""
  view['thinking_alert_label'].text = ""
  view['communication_alert_label'].text = ""
  view['application_alert_label'].text = ""

view = ui.load_view()
ui.load_view('test_average').present(style = 'fullscreen', hide_title_bar = True)	   		   	  	   
