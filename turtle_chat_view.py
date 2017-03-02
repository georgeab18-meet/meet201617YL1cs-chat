#2016-2017 PERSONAL PROJECTS: TurtleChat!
#The Amazing george Abu Dauod (so modest...)

#####################################################################################
#                                   IMPORTS                                         #
#####################################################################################
#import the turtle module
#import the Client class from the turtle_chat_client module
#Finally, from the turtle_chat_widgets module, import two classes: Button and TextInput
#####################################################################################
#####################################################################################
import turtle
turtle.hideturtle()
turtle.penup()
from turtle_chat_client import Client
from turtle_chat_widgets import Button,TextInput
#####################################################################################
#                                   TextBox                                         #
#####################################################################################
#Make a class called TextBox, which will be a subclass of TextInput.
#Because TextInput is an abstract class, you must implement its abstract
#methods.  There are two:
#
#draw_box
#write_msg
#
#Hints:
#1. in draw_box, you will draw (or stamp) the space on which the user's input
#will appear.
#
#2. All TextInput objects have an internal turtle called writer (i.e. self will
#   have something called writer).  You can write new text with it using code like
#
#   self.writer.write(a_string_variable)
#
#   and you can erase that text using
#
#   self.writer.clear()
#
#3. If you want to make a newline character (i.e. go to the next line), just add
#   \r to your string.  Test it out at the Python shell for practice
#####################################################################################
#####################################################################################
class TextBox(TextInput):
    def draw_box(self):
        self.drawer = turtle.clone()
        self.drawer.hideturtle()
        self.drawer.penup()
        self.drawer.goto(self.pos)
        self.drawer.pendown()
        turtle.fillcolor("white")
        self.drawer.begin_fill()
        self.drawer.goto(self.drawer.xcor()+self.width,self.drawer.ycor())
        self.drawer.goto(self.drawer.xcor(),self.drawer.ycor()-self.height)
        self.drawer.goto(self.drawer.xcor()-self.width,self.drawer.ycor())
        self.drawer.goto(self.drawer.xcor(),self.drawer.ycor()+self.height)
        self.drawer.end_fill()
    def write_msg(self):
        '''self.drawer = turtle.clone()
        self.drawer.hideturtle()
        self.drawer.penup()
        self.drawer.goto(self.pos)
        self.drawer.pendown()
        self.drawer.color("black","white")
        self.drawer.begin_fill()
        self.drawer.goto(self.drawer.xcor()+self.width,self.drawer.ycor())
        self.drawer.goto(self.drawer.xcor(),self.drawer.ycor()-self.height)
        self.drawer.goto(self.drawer.xcor()-self.width,self.drawer.ycor())
        self.drawer.goto(self.drawer.xcor(),self.drawer.ycor()+self.height)
        self.drawer.end_fill()'''
        self.writer.clear()
        if self.new_msg.endswith(">"):
            if self.new_msg.endswith("<!>"):
                self.new_msg = self.new_msg.replace("<!>","")
                if self.lang == 'ENG':
                    self.lang = 'ARB'
                    self.setup_listeners()
                elif self.lang == 'ARB':
                    self.lang = 'BRL'
                    self.setup_listeners()
                elif self.lang == 'BRL':
                    self.lang = 'ENG'
                    self.setup_listeners()
            elif self.new_msg.endswith("<change_username>"):
                self.view.sending_mode = False
                prevu = self.view.user
                self.new_msg = self.new_msg.replace("<change_username>","")
                self.view.user = self.view.butt.fun()
                self.view.sending_mode = True
                if prevu != "Me":
                    self.view.client.send(prevu + " changed his name to " + self.view.user)
                else:
                    self.view.client.send("Partner changed his name to " + self.view.user)
                for msg in range(len(self.view.msg_queue)):
                    self.view.msg_queue[msg]=self.view.msg_queue[msg].replace(prevu,self.view.user)
                self.new_msg = ""
            #elif self.new_msg.endswith("<change_partnername>"):
             #   prevp = self.view.partner
              #  self.view.partner=input("Enter the new partner name: \r")
               # for msg in range(len(self.view.msg_queue)):
                #    self.view.msg_queue[msg]=self.view.msg_queue[msg].replace(prevp,self.view.partner)
                #self.new_msg = self.new_msg.replace("<change_partnername>","")
            elif self.new_msg.endswith("<help>"):
                self.new_msg = self.new_msg.replace("<help>","")
                for tur in self.view.msg_queue_turtles:
                    tur.clear()
                intro = "Welcome to TurtleChat, \r if you want to get back to the \r chat room type <chat>, \r \r for the emojis list type <emoji>, \r \r to change the language the language type <!>, \r \r if you want to change your username \r type the new user name \r and then <change_ username>, \r \r if you want to change the \r background, click left and right \r \r enjoy the chatting!"
                self.view.msg_queue_turtles[-4].write(intro)
            elif self.new_msg.endswith("<chat>"):
                self.view.display_msg()
                self.new_msg = self.new_msg.replace("<chat>","")
            elif self.new_msg.endswith("<emoji>"):
                self.new_msg = self.new_msg.replace("<emoji>","")
                for turt in self.view.msg_queue_turtles:
                    turt.clear()
                emoji_list = "<3"+str(chr(9829))+"\r :)"+str(chr(9786))+"\r :("+str(chr(9785))+"\r <flower1>"+str(chr(10047))+"\r <flower2>"+str(chr(10048))+"\r <flower3>"+str(chr(10049))+"\r <snow>"+str(chr(10052))+"\r <cross1>"+str(chr(10013))+"\r <cross2>"+str(chr(10014))+"\r <cross3>"+str(chr(10015))+"\r <star>"+str(chr(11088))+"\r <=>"+str(chr(10234))+"\r =>"+str(chr(10233))+"\r <="+str(chr(10232))+"\r <music1>"+str(chr(9833))+"\r <music2>"+str(chr(9834))+"\r <music3>"+str(chr(9835))+"\r <music4>"+str(chr(9836))
                self.view.msg_queue_turtles[-4].write(emoji_list)
            elif self.new_msg.endswith("<delete>"):
                self.new_msg = ""
                self.view.msg_queue.remove(self.view.msg_queue[0])
                self.view.client.send("<d>")
                self.view.display_msg(self.view.msg_ind)
            elif self.new_msg.endswith("<9009>"):
                self.view.client = self.view.client_9009
                self.new_msg = self.new_msg.replace("<9009>","")
            elif self.new_msg.endswith("<9010>"):
                self.view.client = self.view.client_9010
                self.new_msg = self.new_msg.replace("<9010>","")
            elif self.new_msg.endswith("<9011>"):
                self.view.client = self.view.client_9011
                self.new_msg = self.new_msg.replace("<9011>","")
            elif self.new_msg.endswith("<9012>"):
                self.view.client = self.view.client_9012
                self.new_msg = self.new_msg.replace("<9012>","")
        if len(self.new_msg) < self.letts:
            self.writer.write(self.new_msg, align = 'center')
        else:
            for l in range(int(len(self.new_msg)/self.letts)+1):
                if l < int(len(self.new_msg)/self.letts):
                    self.writer.goto(self.writer.xcor(),self.ax-(l*10))
                    self.writer.write(self.new_msg[(l*self.letts):((l+1)*self.letts)], align = 'center' )
                    
                else:
                    self.writer.goto(self.writer.xcor(),self.ax-(l*10))
                    self.writer.write(self.new_msg[(l*self.letts):len(self.new_msg)], align = 'center')
                
                              
#####################################################################################
#                                  SendButton                                       #
#####################################################################################
#Make a class called SendButton, which will be a subclass of Button.
#Button is an abstract class with one abstract method: fun.
#fun gets called whenever the button is clicked.  It's jobs will be to
#
# 1. send a message to the other chat participant - to do this,
#    you will need to call the send method of your Client instance
# 2. update the messages that you see on the screen
#
#HINT: You may want to override the __init__ method so that it takes one additional
#      input: view.  This will be an instance of the View class you will make next
#      That class will have methods inside of it to help
#      you send messages and update message displays.
#####################################################################################
#####################################################################################

class SendButton(Button):
    def __init__(self,my_turtle=None,shape=None,cshape=None,pos=(0,-250),view=None):
        if view == None:
            my_view = View("Me","Partner")
            self.view = my_view
        else:
            self.view = view
        if my_turtle is None :
            #If no turtle given, create new one
            self.turtle=turtle.clone()
        else:
            self.turtle=my_turtle

        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(pos)

        if shape is None:
            self.shape = 'square'
            self.turtle.shape('square')
            self.turtle.shapesize(2,10)
        else:
            self.shape = shape
            turtle.addshape(shape)
            self.turtle.shape(shape)
        if cshape is None:
            self.cshape = self.shape
        else:
            self.cshape = cshape
            turtle.addshape(cshape)
        self.turtle.showturtle()
        self.turtle.onclick(self.fun) #Link listener to button function
        self.turtle.onrelease(self.rel)
        turtle.listen() #Start listener
    def rel(self,x = None, y = None):
        self.turtle.shape(self.shape)
    def fun(self,x = None, y = None):
        self.turtle.shape(self.cshape)
        if self.view.sending_mode == True:
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<3",str(chr(9829)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace(":)",str(chr(9786)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace(":(",str(chr(9785)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<flower1>",str(chr(10047)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<flower2>",str(chr(10048)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<flower3>",str(chr(10049)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<snow>",str(chr(10052)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<cross1>",str(chr(10013)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<cross2>",str(chr(10014)))
            self.view.textbox.new_mskg=self.view.textbox.new_msg.replace("<cross3>",str(chr(10015)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<star>",str(chr(11088)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<=>",str(chr(10234)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("=>",str(chr(10233)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<=",str(chr(10232)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<music1>",str(chr(9833)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<music2>",str(chr(9834)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<music3>",str(chr(9835)))
            self.view.textbox.new_msg=self.view.textbox.new_msg.replace("<music4>",str(chr(9836)))
            if len(self.view.textbox.new_msg) < self.view.textbox.letts:
                self.view.msg_queue.insert(0,self.view.user+": \r"+self.view.textbox.new_msg)
            else:
                to_insert = ' '
                for l in range(int(len(self.view.textbox.new_msg)/self.view.textbox.letts)+1):
                    if l < int(len(self.view.textbox.new_msg)/self.view.textbox.letts):
            
                        to_insert+=self.view.textbox.new_msg[(l*self.view.textbox.letts):((l+1)*self.view.textbox.letts)] + " \r"
                    
                    else:
                    
                        to_insert+=self.view.textbox.new_msg[(l*self.view.textbox.letts):len(self.view.textbox.new_msg)]+ " \r"
                self.view.msg_queue.insert(0,self.view.user+": \r"+to_insert)
        
            self.view.send_msg()
            self.view.textbox.writer.clear()
        else:
            return(self.view.textbox.new_msg)
        
        
##################################################################
#                             View                               #
##################################################################
#Make a new class called View.  It does not need to have a parent
#class mentioned explicitly.
#
#Read the comments below for hints and directions.
##################################################################
##################################################################
class View:
    

    def __init__(self,username='Me',partner_name='Partner',client_port=None):
        _MSG_LOG_LENGTH=2 #Number of messages to retain in view
        _SCREEN_WIDTH=300
        _SCREEN_HEIGHT=600
        _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))
        '''
        :param username: the name of this chat user
        :param partner_name: the name of the user you are chatting with
        '''
        ###
        #Store the username and partner_name into the instance.
        ###
        self.user = username
        self.partner = partner_name
        self.sending_mode = True
        ###
        #Make a new client object and store it in this instance of View
        #(i.e. self).  The name of the instance should be my_client
        ###
        self.client_9009 = Client()
        #self.client_9010 = Client(port=9010)
        #self.client_9011 = Client(port=9011)
        #self.client_9012 = Client(port=9012)
        self.client = self.client_9009
        ###
        #Set screen dimensions using turtle.setup
        #You can get help on this function, as with other turtle functions,
        #by typing
        #
        #   import turtle
        #   help(turtle.setup)
        #
        #at the Python shell.
        ###
        turtle.setup(300,600)
        turtle.title("TurtleChat")
        ###
        #This list will store all of the messages.
        #You can add strings to the front of the list using
        #   self.msg_queue.insert(0,a_msg_string)
        #or at the end of the list using
        #   self.msg_queue.append(a_msg_string)
        self.butt = SendButton(shape = "6.gif",cshape = "7.gif",view = self)
        self.textbox = TextBox(view = self)
        self.bg_in = 0
        self.msg_ind = 0
        self.bgs_list = ["1.gif","2.gif","3.gif","4.gif"]
        self.textbox.draw_box()
        self.textbox.lang = 'ENG'
        self.textbox.setup_listeners()
        self.msg_queue=[]
        self.msg_queue.insert(0,"if you need help type: \r <help>")
        ###
        
        ###
        #Create one turtle object for each message to display.
        #You can use the clear() and write() methods to erase
        #and write messages for each
        ###
        self.msg_queue_turtles = list()
        for i in range(4):
            self.msg_queue.append("")
            self.msg_queue_turtles.append(turtle.clone())
        for tutu in range(4):
            self.msg_queue_turtles[tutu].hideturtle()
            self.msg_queue_turtles[tutu].penup()
            self.msg_queue_turtles[tutu].goto(-100,tutu*(_LINE_SPACING))
        self.msg_queue_turtles[-3].write("Welcome to TurtleChat, \r if you’d like to discuss Music enter <9010>, \r if you’d like to discuss Sports enter <9011>, \r if you’d like to to discuss Science enter <9012>, \r if you’d like to discuss Anything enter <9009>")
        ###
        #Create a TextBox instance and a SendButton instance and
        #Store them inside of this instance
        ###

        ###
        #Call your setup_listeners() function, if you have one,
        #and any other remaining setup functions you have invented.
        ###

    def send_msg(self):
        '''
        You should implement this method.  It should call the
        send() method of the Client object stored in this View
        instance.  It should also update the list of messages,
        self.msg_queue, to include this message.  It should
        clear the textbox text display (hint: use the clear_msg method).
        It should call self.display_msg() to cause the message
        display to be updated.
        '''
        if self.user != "Me":
            self.client.send(self.user+": \r"+self.textbox.new_msg)
        else:
            self.client.send("Partner:"+"\r"+self.textbox.new_msg)
        self.display_msg()
        self.textbox.clear_msg()

    def get_msg(self):
        return self.textbox.get_msg()

    

    def setup_listeners(self):
        '''
        Set up send button - additional listener, in addition to click,
        so that return button will send a message.
        To do this, you will use the turtle.onkeypress function.
        The function that it will take is
        self.send_btn.fun
        where send_btn is the name of your button instance

        Then, it can call turtle.listen()
        '''
        turtle.listen()

    def msg_received(self,msg):
        '''
        This method is called when a new message is received.
        It should update the log (queue) of messages, and cause
        the view of the messages to be updated in the display.

        :param msg: a string containing the message received
                    - this should be displayed on the screen
        '''
        if not msg.endswith("<d>"):
        #print(msg) #Debug - print message
            self.msg_queue.insert(0,msg)
        #Add the message to the queue either using insert (to put at the beginning)
        #or append (to put at the end).
            self.display_msg()
        #print(self.msg_queue[0]+"!")
        #Then, call the display_msg method to update the display
        else:
            self.msg_queue.remove(self.msg_queue[0])
            self.display_msg()
    def display_msg(self,n=0):
        '''
        This method should update the messages displayed in the screen.
        You can get the messages you want from self.msg_queue
        '''
        for i in range(4):
            self.msg_queue_turtles[i].clear()
        for t in range(4):
            if self.msg_queue[t+n].startswith(self.user):
                self.msg_queue_turtles[t].pencolor("red")
            else:
                self.msg_queue_turtles[t].pencolor("green")
            self.msg_queue_turtles[t].write(self.msg_queue[t+n],font=('Arial',10,'normal'))

    def get_client(self):
        return self.client
##############################################################
##############################################################


#########################################################
#Leave the code below for now - you can play around with#
#it once you have a working view, trying to run you chat#
#view in different ways.                                #
#########################################################

#m
_WAIT_TIME=200 #Time between check for new message, ms
if __name__=="__main__":
    my_view=View()
    def check() :
        msg_in=my_view.client.receive()
        #msg_in=my_view.get_client().receive()
        if not(msg_in is None):
            if msg_in==Client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) #Check recursively
    check()
    turtle.mainloop()
