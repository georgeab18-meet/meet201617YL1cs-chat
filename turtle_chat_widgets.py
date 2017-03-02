import turtle
from abc import ABCMeta,abstractmethod

class Button(metaclass=ABCMeta):
    '''
    Abstract class wrapping a turtle object to be used as a clickable button.

    The abstract method, fun, is called when the button is clicked on.
    '''
    def __init__(self,my_turtle=None,shape=None,pos=(-200,0)):
        '''
        Initialize Button object.  The button will be given an onclick
        listener that triggers the implementation of the abstract method, fun.

        :param my_turtle: turtle object which, when clicked, will trigger
                            the action specified in the fun method.
                            Default value=None - with this input, a new
                            turtle is created.
        :param shape: shape for the turtle object.  Default=None, in which
                    case, the shape is the result of
                    turtle.shape('square'); turtle.shapesize(2,10)
        :param pos: tuple input, (x,y), specifying the location of the
                    turtle object.
        '''
        print('test')
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
            self.turtle.shape('square')
            self.turtle.shapesize(2,10)
        else:
            turtle.addshape(shape)
            self.turtle.shape(shape)
        self.turtle.showturtle()
        self.turtle.onclick(self.fun) #Link listener to button function
        turtle.listen() #Start listener


    @abstractmethod
    def fun(self,x=None,y=None):
        '''
        Abstract method whose implementation is called when
        button gets pressed.  Must be implemented in concrete subclasses.

        :param x: integer, horizontal coordinate of click in pixels (required for onclick)
                  Default=None
        :param y: integer, vertical coordinate of click in pixels (required for onclick)
                  Default=None
        '''
        pass

class TextInput(metaclass=ABCMeta):
    '''
    This class sets up a textbox to take live text input from
    the user via keyboard listeners.
    '''
    def __init__(self, width=200, height=100, pos=(-100,-100), background_gif=None, letters_per_line=25,view = None):
        '''
        Initialize TextInput object.

        Store message in instance attribute, new_msg.

        :param width: integer, width of box (pixels).  Default=200 pixels.
        :param height: integer, height of box (pixels).  Default=100 pixels.
        :param pos: tuple, (x,y) - textbox location on screen.  Default=(0,0)
        :param background_gif: string, name of background gif image for textbox
                               - can be used in draw_box, though not required.
                               Default=None.
        :param letters_per_line: integer, number of letters per line.
        '''
        self.lang = 'ARB'
        self.letts = letters_per_line
        if view == None:
            my_view = View("Me","Partner")
            self.view = my_view
        else:
            self.view = view
        self.width=width
        self.height=height
        self.letters_per_line=letters_per_line
        self.background_gif=background_gif
        self.new_msg='' #This string stores text stream going into text ox.
        self.pos=pos
        self.writer=turtle.clone()
        
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.speed(0)
        #Move writer to location where text starts.
        self.writer.goto(self.pos[0]+100,self.pos[1]-20)
        self.ax = self.writer.ycor()
        #Setup listeners
        self.setup_listeners()
        #Draw box to surround text field
        self.draw_box()

    @abstractmethod
    def draw_box(self):
        '''
        Abstract method; implementation in concrete class
        will draw textbox.  Can use instance attributes,
        pos, width, and height.
        '''
        pass

    @abstractmethod
    def write_msg(self):
        '''
        Method to write the message to the screen after every
        keypress.  Abstract method; must be implemented in
        concrete classes.

        Opportunity, also, to clean strings - add in newlines,
        '\r', for example, when needed, etc.

        Side effect method - no inputs or outputs, but
        new_msg may be changed.
        '''
        pass

    def clear_msg(self):
        '''
        Erase message in new_msg stream and update display.
        '''
        self.new_msg=''
        self.write_msg()

    def get_msg(self):
        '''
        :return: new_msg stream
        '''
        return self.new_msg

    def setup_listeners(self):
        '''
        Set up listeners for all of the buttons.
        '''

        #To find text key names, you can refer to
        #http://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
        turtle.onkeypress( self.go_up,"Up")
        turtle.onkeypress( self.go_down,"Down")
        turtle.onkeypress( self.change_bgp,"Left")
        turtle.onkeypress( self.change_bgn,"Right")
        turtle.onkeypress( self.view.butt.fun,"Return")
        turtle.onkeyrelease( self.view.butt.rel,"Return")
        #Numbers
        turtle.onkeypress( self.add_0, '0' )
        turtle.onkeypress( self.add_1, '1' )
        turtle.onkeypress( self.add_2, '2' )
        turtle.onkeypress( self.add_3, '3' )
        turtle.onkeypress( self.add_4, '4' )
        turtle.onkeypress( self.add_5, '5' )
        turtle.onkeypress( self.add_6, '6' )
        turtle.onkeypress( self.add_7, '7' )
        turtle.onkeypress( self.add_8, '8' )
        turtle.onkeypress( self.add_9, '9' )

        #Punctuation, etc.
        turtle.onkeypress( self.add_comma, 'comma' )
        turtle.onkeypress( self.add_period, 'period' )
        turtle.onkeypress( self.add_exclaim, 'exclam' ) #Yes, exclam
        turtle.onkeypress( self.add_colon, 'colon' )
        turtle.onkeypress( self.add_dollar, 'dollar' )
        turtle.onkeypress( self.add_dblquote,'quotedbl')
        turtle.onkeypress( self.add_quoteright,'quoteright')
        turtle.onkeypress( self.add_quoteleft,'quoteleft')
        turtle.onkeypress( self.add_parenleft,'parenleft')
        turtle.onkeypress( self.add_parenright,'parenright')
        turtle.onkeypress( self.add_minus,'minus')
        turtle.onkeypress( self.add_slash,'slash')
        turtle.onkeypress( self.add_plus,'plus')
        turtle.onkeypress( self.add_ampersand,'ampersand')
        turtle.onkeypress( self.add_pound,'numbersign')
        turtle.onkeypress( self.add_asterisk,'asterisk')
        turtle.onkeypress( self.add_percent, 'percent')
        turtle.onkeypress( self.add_space, 'space' )
        turtle.onkeypress( self.backspace, 'BackSpace' )
        #turtle.onkeypress( self.shift, 'Shift_L' )
        #turtle.onkeypress( self.shift, 'Shift_R' )
        #turtle.onkeypress( self.caps, 'Caps_Lock' )
        #turtle.onkeyrelease( self.shift_release, 'Shift_L' )
        #turtle.onkeyrelease( self.shift_release, 'Shift_R' )
        turtle.onkeypress( self.add_at, 'at')
        turtle.onkeypress( self.add_question,'question')
        turtle.onkeypress( self.add_equal,'equal')
        turtle.onkeypress( self.add_less,'less')
        turtle.onkeypress( self.add_greater,'greater')
        turtle.onkeypress( self.add_underscore,'underscore')
        turtle.onkeypress( self.add_backslash,'backslash')
        turtle.onkeypress( self.add_brackright,'bracketright')
        turtle.onkeypress( self.add_brackleft,'bracketleft')

        #Lower-case letters
        if self.lang == "BRL":
            turtle.onkeypress( self.add_bspace, 'space' )
            turtle.onkeypress( self.add_ba, 'a' )
            turtle.onkeypress( self.add_bb, 'b' )
            turtle.onkeypress( self.add_bc, 'c' )
            turtle.onkeypress( self.add_bd, 'd' )
            turtle.onkeypress( self.add_be, 'e' )
            turtle.onkeypress( self.add_bf, 'f' )
            turtle.onkeypress( self.add_bg, 'g' )
            turtle.onkeypress( self.add_bh, 'h' )
            turtle.onkeypress( self.add_bi, 'i' )
            turtle.onkeypress( self.add_bj, 'j' )
            turtle.onkeypress( self.add_bk, 'k' )
            turtle.onkeypress( self.add_bl, 'l' )
            turtle.onkeypress( self.add_bm, 'm' )
            turtle.onkeypress( self.add_bn, 'n' )
            turtle.onkeypress( self.add_bo, 'o' )
            turtle.onkeypress( self.add_bp, 'p' )
            turtle.onkeypress( self.add_bq, 'q' )
            turtle.onkeypress( self.add_br, 'r' )
            turtle.onkeypress( self.add_bs, 's' )
            turtle.onkeypress( self.add_bt, 't' )
            turtle.onkeypress( self.add_bu, 'u' )
            turtle.onkeypress( self.add_bv, 'v' )
            turtle.onkeypress( self.add_bw, 'w' )
            turtle.onkeypress( self.add_bx, 'x' )
            turtle.onkeypress( self.add_by, 'y' )
            turtle.onkeypress( self.add_bz, 'z' )
            turtle.onkeypress( self.add_ba, 'A' )
            turtle.onkeypress( self.add_bb, 'B' )
            turtle.onkeypress( self.add_bc, 'C' )
            turtle.onkeypress( self.add_bd, 'D' )
            turtle.onkeypress( self.add_be, 'E' )
            turtle.onkeypress( self.add_bf, 'F' )
            turtle.onkeypress( self.add_bg, 'G' )
            turtle.onkeypress( self.add_bh, 'H' )
            turtle.onkeypress( self.add_bi, 'I' )
            turtle.onkeypress( self.add_bj, 'J' )
            turtle.onkeypress( self.add_bk, 'K' )
            turtle.onkeypress( self.add_bl, 'L' )
            turtle.onkeypress( self.add_bm, 'M' )
            turtle.onkeypress( self.add_bn, 'N' )
            turtle.onkeypress( self.add_bo, 'O' )
            turtle.onkeypress( self.add_bp, 'P' )
            turtle.onkeypress( self.add_bq, 'Q' )
            turtle.onkeypress( self.add_br, 'R' )
            turtle.onkeypress( self.add_bs, 'S' )
            turtle.onkeypress( self.add_bt, 'T' )
            turtle.onkeypress( self.add_bu, 'U' )
            turtle.onkeypress( self.add_bv, 'V' )
            turtle.onkeypress( self.add_bw, 'W' )
            turtle.onkeypress( self.add_bx, 'X' )
            turtle.onkeypress( self.add_by, 'Y' )
            turtle.onkeypress( self.add_bz, 'Z' )
        if self.lang == "ENG":
            turtle.onkeypress( self.add_a, 'a' )
            turtle.onkeypress( self.add_b, 'b' )
            turtle.onkeypress( self.add_c, 'c' )
            turtle.onkeypress( self.add_d, 'd' )
            turtle.onkeypress( self.add_e, 'e' )
            turtle.onkeypress( self.add_f, 'f' )
            turtle.onkeypress( self.add_g, 'g' )
            turtle.onkeypress( self.add_h, 'h' )
            turtle.onkeypress( self.add_i, 'i' )
            turtle.onkeypress( self.add_j, 'j' )
            turtle.onkeypress( self.add_k, 'k' )
            turtle.onkeypress( self.add_l, 'l' )
            turtle.onkeypress( self.add_m, 'm' )
            turtle.onkeypress( self.add_n, 'n' )
            turtle.onkeypress( self.add_o, 'o' )
            turtle.onkeypress( self.add_p, 'p' )
            turtle.onkeypress( self.add_q, 'q' )
            turtle.onkeypress( self.add_r, 'r' )
            turtle.onkeypress( self.add_s, 's' )
            turtle.onkeypress( self.add_t, 't' )
            turtle.onkeypress( self.add_u, 'u' )
            turtle.onkeypress( self.add_v, 'v' )
            turtle.onkeypress( self.add_w, 'w' )
            turtle.onkeypress( self.add_x, 'x' )
            turtle.onkeypress( self.add_y, 'y' )
            turtle.onkeypress( self.add_z, 'z' )
    
            #Upper-case letters
            turtle.onkeypress( self.add_A, 'A' )
            turtle.onkeypress( self.add_B, 'B' )
            turtle.onkeypress( self.add_C, 'C' )
            turtle.onkeypress( self.add_D, 'D' )
            turtle.onkeypress( self.add_E, 'E' )
            turtle.onkeypress( self.add_F, 'F' )
            turtle.onkeypress( self.add_G, 'G' )
            turtle.onkeypress( self.add_H, 'H' )
            turtle.onkeypress( self.add_I, 'I' )
            turtle.onkeypress( self.add_J, 'J' )
            turtle.onkeypress( self.add_K, 'K' )
            turtle.onkeypress( self.add_L, 'L' )
            turtle.onkeypress( self.add_M, 'M' )
            turtle.onkeypress( self.add_N, 'N' )
            turtle.onkeypress( self.add_O, 'O' )
            turtle.onkeypress( self.add_P, 'P' )
            turtle.onkeypress( self.add_Q, 'Q' )
            turtle.onkeypress( self.add_R, 'R' )
            turtle.onkeypress( self.add_S, 'S' )
            turtle.onkeypress( self.add_T, 'T' )
            turtle.onkeypress( self.add_U, 'U' )
            turtle.onkeypress( self.add_V, 'V' )
            turtle.onkeypress( self.add_W, 'W' )
            turtle.onkeypress( self.add_X, 'X' )
            turtle.onkeypress( self.add_Y, 'Y' )
            turtle.onkeypress( self.add_Z, 'Z' )
        if self.lang == 'ARB':
            turtle.onkeypress( self.add_hmzea, 'H' )
            turtle.onkeypress( self.add_hmzem, 'Y' )
            turtle.onkeypress( self.add_za,'slash')
            turtle.onkeypress( self.add_6a,'quoteright')
            turtle.onkeypress( self.add_kaf, 'semicolon' )
            turtle.onkeypress( self.add_waw, 'comma' )
            turtle.onkeypress( self.add_zen, 'period' )
            turtle.onkeypress( self.add_thal,'quoteleft')
            turtle.onkeypress( self.add_dal,'bracketright')
            turtle.onkeypress( self.add_jim,'bracketleft')
            turtle.onkeypress( self.add_shin, 'a' )
            #turtle.onkeypress( self.add_la, 'b' )
            turtle.onkeypress( self.add_hmzew, 'c' )
            turtle.onkeypress( self.add_ya, 'd' )
            turtle.onkeypress( self.add_tha, 'e' )
            turtle.onkeypress( self.add_ba2, 'f' )
            turtle.onkeypress( self.add_lam, 'g' )
            turtle.onkeypress( self.add_alf, 'h' )
            turtle.onkeypress( self.add_ha, 'i' )
            turtle.onkeypress( self.add_ta, 'j' )
            turtle.onkeypress( self.add_non, 'k' )
            turtle.onkeypress( self.add_mim, 'l' )
            turtle.onkeypress( self.add_tam, 'm' )
            turtle.onkeypress( self.add_alfm, 'n' )
            turtle.onkeypress( self.add_5a, 'o' )
            turtle.onkeypress( self.add_7a, 'p' )
            turtle.onkeypress( self.add_dad, 'q' )
            turtle.onkeypress( self.add_qaf, 'r' )
            turtle.onkeypress( self.add_sin, 's' )
            turtle.onkeypress( self.add_fa, 't' )
            turtle.onkeypress( self.add_3en, 'u' )
            turtle.onkeypress( self.add_ra, 'v' )
            turtle.onkeypress( self.add_sad, 'w' )
            turtle.onkeypress( self.add_hmze, 'x' )
            turtle.onkeypress( self.add_4en, 'y' )
            turtle.onkeypress( self.add_hmzek, 'z' )
        #Start listeners
        turtle.listen()

    #All methods adding (or subtracting, in case of backspace)
    #letters from message.
    def add_space(self):
        self.new_msg+=' '
        self.write_msg()
        print(self.new_msg)
    def add_bspace(self):
        self.new_msg+=' '*2
        self.write_msg()
        print(self.new_msg)
    def add_a(self):
        self.new_msg+='a'
        self.write_msg()
        print(self.new_msg)    
    def add_A(self):
        self.new_msg+='A'
        self.write_msg()
        print(self.new_msg)
    def add_b(self):
        self.new_msg+='b'
        self.write_msg()
        print(self.new_msg)
    def add_B(self) :
        self.new_msg+='B'
        self.write_msg()
        print(self.new_msg)
    def add_c(self):
        self.new_msg+='c'
        self.write_msg()
        print(self.new_msg)
    def add_C(self):
        self.new_msg+='C'
        self.write_msg()
        print(self.new_msg)
    def add_d(self):
        self.new_msg+='d'
        self.write_msg()
        print(self.new_msg)
    def add_D(self):
        self.new_msg+='D'
        self.write_msg()
        print(self.new_msg)
    def add_e(self):
        self.new_msg+='e'
        self.write_msg()
        print(self.new_msg)
    def add_E(self):
        self.new_msg+='E'
        self.write_msg()
        print(self.new_msg)
    def add_f(self):
        self.new_msg+='f'
        self.write_msg()
        print(self.new_msg)
    def add_F(self):
        self.new_msg+='F'
        self.write_msg()
        print(self.new_msg)
    def add_g(self):
        self.new_msg+='g'
        self.write_msg()
        print(self.new_msg)
    def add_G(self):
        self.new_msg+='G'
        self.write_msg()
        print(self.new_msg)
    def add_h(self):
        self.new_msg+='h'
        self.write_msg()
        print(self.new_msg)
    def add_H(self):
        self.new_msg+='H'
        self.write_msg()
        print(self.new_msg)
    def add_i(self):
        self.new_msg+='i'
        self.write_msg()
        print(self.new_msg)
    def add_I(self):
        self.new_msg+='I'
        self.write_msg()
        print(self.new_msg)
    def add_j(self):
        self.new_msg+='j'
        self.write_msg()
        print(self.new_msg)
    def add_J(self):
        self.new_msg+='J'
        self.write_msg()
        print(self.new_msg)
    def add_k(self):
        self.new_msg+='k'
        self.write_msg()
        print(self.new_msg)
    def add_K(self):
        self.new_msg+='K'
        self.write_msg()
        print(self.new_msg)
    def add_l(self):
        self.new_msg+='l'
        self.write_msg()
        print(self.new_msg)
    def add_L(self):
        self.new_msg+='L'
        self.write_msg()
        print(self.new_msg)
    def add_m(self):
        self.new_msg+='m'
        self.write_msg()
        print(self.new_msg)
    def add_M(self):
        self.new_msg+='M'
        self.write_msg()
        print(self.new_msg)
    def add_n(self):
        self.new_msg+='n'
        self.write_msg()
        print(self.new_msg)
    def add_N(self):
        self.new_msg+='N'
        self.write_msg()
        print(self.new_msg)
    def add_o(self):
        self.new_msg+='o'
        self.write_msg()
        print(self.new_msg)
    def add_O(self):
        self.new_msg+='O'
        self.write_msg()
        print(self.new_msg)
    def add_p(self):
        self.new_msg+='p'
        self.write_msg()
        print(self.new_msg)
    def add_P(self):
        self.new_msg+='P'
        self.write_msg()
        print(self.new_msg)
    def add_q(self):
        self.new_msg+='q'
        self.write_msg()
        print(self.new_msg)
    def add_Q(self):
        self.new_msg+='Q'
        self.write_msg()
        print(self.new_msg)
    def add_r(self):
        self.new_msg+='r'
        self.write_msg()
        print(self.new_msg)
    def add_R(self):
        self.new_msg+='R'
        self.write_msg()
        print(self.new_msg)
    def add_s(self):
        self.new_msg+='s'
        self.write_msg()
        print(self.new_msg)
    def add_S(self):
        self.new_msg+='S'
        self.write_msg()
        print(self.new_msg)
    def add_t(self):
        self.new_msg+='t'
        self.write_msg()
        print(self.new_msg)
    def add_T(self):
        self.new_msg+='T'
        self.write_msg()
        print(self.new_msg)
    def add_u(self):
        self.new_msg+='u'
        self.write_msg()
        print(self.new_msg)
    def add_U(self):
        self.new_msg+='U'
        self.write_msg()
        print(self.new_msg)
    def add_v(self):
        self.new_msg+='v'
        self.write_msg()
        print(self.new_msg)
    def add_V(self):
        self.new_msg+='V'
        self.write_msg()
        print(self.new_msg)
    def add_w(self):
        self.new_msg+='w'
        self.write_msg()
        print(self.new_msg)
    def add_W(self):
        self.new_msg+='W'
        self.write_msg()
        print(self.new_msg)
    def add_x(self):
        self.new_msg+='x'
        self.write_msg()
        print(self.new_msg)
    def add_X(self):
        self.new_msg+='X'
        self.write_msg()
        print(self.new_msg)
    def add_y(self):
        self.new_msg+='y'
        self.write_msg()
        print(self.new_msg)
    def add_Y(self):
        self.new_msg+='Y'
        self.write_msg()
        print(self.new_msg)
    def add_z(self):
        self.new_msg+='z'
        self.write_msg()
        print(self.new_msg)
    def add_Z(self):
        self.new_msg+='Z'
        self.write_msg()
        print(self.new_msg)
    def backspace(self):
        self.new_msg=self.new_msg[0:-1] #Remove last character
        self.write_msg()
        print(self.new_msg)
    def add_dollar(self):
        self.new_msg+='$'
        self.write_msg()
        print(self.new_msg)
    def add_dblquote(self):
        self.new_msg+='"'
        self.write_msg()
        print(self.new_msg)
    def add_quoteright(self):
        self.new_msg+="'"
        self.write_msg()
        print(self.new_msg)
    def add_quoteleft(self):
        self.new_msg+="`"
        self.write_msg()
        print(self.new_msg)
    def add_parenleft(self):
        self.new_msg+="("
        self.write_msg()
        print(self.new_msg)
    def add_parenright(self):
        self.new_msg+=")"
        self.write_msg()
        print(self.new_msg)
    def add_minus(self):
        self.new_msg+="-"
        self.write_msg()
        print(self.new_msg)
    def add_slash(self):
        self.new_msg+="/"
        self.write_msg()
        print(self.new_msg)
    def add_plus(self):
        self.new_msg+="+"
        self.write_msg()
        print(self.new_msg)
    def add_ampersand(self):
        self.new_msg+="&"
        self.write_msg()
        print(self.new_msg)
    def add_pound(self):
        self.new_msg+="#"
        self.write_msg()
        print(self.new_msg)
    def add_asterisk(self):
        self.new_msg+="*"
        self.write_msg()
        print(self.new_msg)
    def add_percent(self):
        self.new_msg+="%"
        self.write_msg()
        print(self.new_msg)
    def add_comma(self):
        self.new_msg+=','
        self.write_msg()
        print(self.new_msg)
    def add_period(self):
        self.new_msg+='.'
        self.write_msg()
        print(self.new_msg)
    def add_exclaim(self):
        self.new_msg+='!'
        self.write_msg()
        print(self.new_msg)
    def add_colon(self):
        self.new_msg+=':'
        self.write_msg()
        print(self.new_msg)
    def add_at(self):
        self.new_msg+='@'
        self.write_msg()
        print(self.new_msg)
    def add_question(self):
        self.new_msg+='?'
        self.write_msg()
        print(self.new_msg)
    def add_equal(self):
        self.new_msg+='='
        self.write_msg()
        print(self.new_msg)
    def add_less(self):
        self.new_msg+='<'
        self.write_msg()
        print(self.new_msg)
    def add_greater(self):
        self.new_msg+='>'
        self.write_msg()
        print(self.new_msg)
    def add_underscore(self):
        self.new_msg+='_'
        self.write_msg()
        print(self.new_msg)
    def add_backslash(self):
        self.new_msg+='\\'
        self.write_msg()
        print(self.new_msg)
    def add_brackright(self):
        self.new_msg+=']'
        self.write_msg()
        print(self.new_msg)
    def add_brackleft(self):
        self.new_msg+='['
        self.write_msg()
        print(self.new_msg)

    def add_0(self):
        self.new_msg+='0'
        self.write_msg()
        print(self.new_msg)
    def add_1(self):
        self.new_msg+='1'
        self.write_msg()
        print(self.new_msg)
    def add_2(self):
        self.new_msg+='2'
        self.write_msg()
        print(self.new_msg)
    def add_3(self):
        self.new_msg+='3'
        self.write_msg()
        print(self.new_msg)
    def add_4(self):
        self.new_msg+='4'
        self.write_msg()
        print(self.new_msg)
    def add_5(self):
        self.new_msg+='5'
        self.write_msg()
        print(self.new_msg)
    def add_6(self):
        self.new_msg+='6'
        self.write_msg()
        print(self.new_msg)
    def add_7(self):
        self.new_msg+='7'
        self.write_msg()
        print(self.new_msg)
    def add_8(self):
        self.new_msg+='8'
        self.write_msg()
        print(self.new_msg)
    def add_9(self):
        self.new_msg+='9'
        self.write_msg()
        print(self.new_msg)
    def send(self):
        self.new_msg=self.new_msg.replace("<3",str(chr(9829)))
        self.new_msg=self.new_msg.replace(":)",str(chr(9786)))
        self.new_msg=self.new_msg.replace(":(",str(chr(9785)))
        self.new_msg=self.new_msg.replace("<flower1>",str(chr(10047)))
        self.new_msg=self.new_msg.replace("<flower2>",str(chr(10048)))
        self.new_msg=self.new_msg.replace("<flower3>",str(chr(10049)))
        self.new_msg=self.new_msg.replace("<snow>",str(chr(10052)))
        self.new_msg=self.new_msg.replace("<cross1>",str(chr(10013)))
        self.new_msg=self.new_msg.replace("<cross2>",str(chr(10014)))
        self.new_msg=self.new_msg.replace("<cross3>",str(chr(10015)))
        self.new_msg=self.new_msg.replace("<star>",str(chr(11088)))
        self.new_msg=self.new_msg.replace("<=>",str(chr(10234)))
        self.new_msg=self.new_msg.replace("=>",str(chr(10233)))
        self.new_msg=self.new_msg.replace("<=",str(chr(10232)))
        self.new_msg=self.new_msg.replace("<music1>",str(chr(9833)))
        self.new_msg=self.new_msg.replace("<music2>",str(chr(9834)))
        self.new_msg=self.new_msg.replace("<music3>",str(chr(9835)))
        self.new_msg=self.new_msg.replace("<music4>",str(chr(9836)))
        
        if len(self.view.textbox.new_msg) < self.view.textbox.letts:
            self.view.msg_queue.insert(0,self.view.user+": \r"+self.view.textbox.new_msg)
        else:
            to_insert = ' '
            for l in range(int(len(self.new_msg)/self.letts)+1):
                if l < int(len(self.new_msg)/self.letts):
            
                    to_insert+=self.new_msg[(l*40):((l+1)*40)] + " \r"
                    
                else:
                    
                    to_insert+=self.new_msg[(l*40):len(self.new_msg)]+ " \r"
            self.view.msg_queue.insert(0,self.view.user+": \r"+to_insert)
        self.view.send_msg()
        self.writer.clear()
    def add_alf(self):
        self.new_msg+=str(chr(1575))
        self.write_msg()
        print(self.new_msg)
    def add_ba2(self):
        self.new_msg+=str(chr(1576))
        self.write_msg()
        print(self.new_msg)
    def add_ta(self):
        self.new_msg+=str(chr(1578))
        self.write_msg()
        print(self.new_msg)
    def add_tha(self):
        self.new_msg+=str(chr(1579))
        self.write_msg()
        print(self.new_msg)
    def add_jim(self):
        self.new_msg+=str(chr(1580))
        self.write_msg()
        print(self.new_msg)
    def add_7a(self):
        self.new_msg+=str(chr(1581))
        self.write_msg()
        print(self.new_msg)
    def add_5a(self):
        self.new_msg+=str(chr(1582))
        self.write_msg()
        print(self.new_msg)
    def add_dal(self):
        self.new_msg+=str(chr(1583))
        self.write_msg()
        print(self.new_msg)
    def add_thal(self):
        self.new_msg+=str(chr(1584))
        self.write_msg()
        print(self.new_msg)
    def add_ra(self):
        self.new_msg+=str(chr(1585))
        self.write_msg()
        print(self.new_msg)
    def add_zen(self):
        self.new_msg+=str(chr(1586))
        self.write_msg()
        print(self.new_msg)
    def add_sin(self):
        self.new_msg+=str(chr(1587))
        self.write_msg()
        print(self.new_msg)
    def add_shin(self):
        self.new_msg+=str(chr(1588))
        self.write_msg()
        print(self.new_msg)
    def add_sad(self):
        self.new_msg+=str(chr(1589))
        self.write_msg()
        print(self.new_msg)
    def add_dad(self):
        self.new_msg+=str(chr(1590))
        self.write_msg()
        print(self.new_msg)
    def add_6a(self):
        self.new_msg+=str(chr(1591))
        self.write_msg()
        print(self.new_msg)
    def add_za(self):
        self.new_msg+=str(chr(1592))
        self.write_msg()
        print(self.new_msg)
    def add_3en(self):
        self.new_msg+=str(chr(1593))
        self.write_msg()
        print(self.new_msg)
    def add_4en(self):
        self.new_msg+=str(chr(1594))
        self.write_msg()
        print(self.new_msg)
    def add_fa(self):
        self.new_msg+=str(chr(1601))
        self.write_msg()
        print(self.new_msg)
    def add_qaf(self):
        self.new_msg+=str(chr(1602))
        self.write_msg()
        print(self.new_msg)
    def add_kaf(self):
        self.new_msg+=str(chr(1603))
        self.write_msg()
        print(self.new_msg)
    def add_lam(self):
        self.new_msg+=str(chr(1604))
        self.write_msg()
        print(self.new_msg)
    def add_mim(self):
        self.new_msg+=str(chr(1605))
        self.write_msg()
        print(self.new_msg)
    def add_non(self):
        self.new_msg+=str(chr(1606))
        self.write_msg()
        print(self.new_msg)
    def add_ha(self):
        self.new_msg+=str(chr(1607))
        self.write_msg()
        print(self.new_msg)
    def add_waw(self):
        self.new_msg+=str(chr(1608))
        self.write_msg()
        print(self.new_msg)
    def add_ya(self):
        self.new_msg+=str(chr(1610))
        self.write_msg()
        print(self.new_msg)
    def add_hmze(self):
        self.new_msg+=str(chr(1569))
        self.write_msg()
        print(self.new_msg)
    def add_hmzew(self):
        self.new_msg+=str(chr(1572))
        self.write_msg()
        print(self.new_msg)
    def add_hmzek(self):
        self.new_msg+=str(chr(1574))
        self.write_msg()
        print(self.new_msg)
    def add_alfm(self):
        self.new_msg+=str(chr(1609))
        self.write_msg()
        print(self.new_msg)
    def add_tam(self):
        self.new_msg+=str(chr(1577))
        self.write_msg()
        print(self.new_msg)
    def add_hmzea(self):
        self.new_msg+=str(chr(1571))
        self.write_msg()
        print(self.new_msg)
    def add_hmzem(self):
        self.new_msg+=str(chr(1573))
        self.write_msg()
        print(self.new_msg)
    def change_bgn(self):
        if self.view.bg_in < 3:
            self.view.bg_in = self.view.bg_in + 1
        else:
            self.view.bg_in = 0
        turtle.bgpic(self.view.bgs_list[self.view.bg_in])
    def change_bgp(self):
        if self.view.bg_in > 0:
            self.view.bg_in = self.view.bg_in - 1
        else:
            self.view.bg_in = 3
        turtle.bgpic(self.view.bgs_list[self.view.bg_in])
    def go_up(self):
        if self.view.msg_ind < len(self.view.msg_queue)-4:
            self.view.msg_ind = self.view.msg_ind+1
            self.view.display_msg(self.view.msg_ind)
    def go_down(self):
        if self.view.msg_ind > 0:
            self.view.msg_ind = self.view.msg_ind-1
            self.view.display_msg(self.view.msg_ind)
    def add_ba(self):
        self.new_msg+=str(chr(10241))
        self.write_msg()
        print(self.new_msg)
    def add_bb(self):
        self.new_msg+=str(chr(10243))
        self.write_msg()
        print(self.new_msg)
    def add_bc(self):
        self.new_msg+=str(chr(10249))
        self.write_msg()
        print(self.new_msg)
    def add_bd(self):
        self.new_msg+=str(chr(10265))
        self.write_msg()
        print(self.new_msg)
    def add_be(self):
        self.new_msg+=str(chr(10257))
        self.write_msg()
        print(self.new_msg)
    def add_bf(self):
        self.new_msg+=str(chr(10251))
        self.write_msg()
        print(self.new_msg)
    def add_bg(self):
        self.new_msg+=str(chr(10267))
        self.write_msg()
        print(self.new_msg)
    def add_bh(self):
        self.new_msg+=str(chr(10259))
        self.write_msg()
        print(self.new_msg)
    def add_bi(self):
        self.new_msg+=str(chr(10250))
        self.write_msg()
        print(self.new_msg)
    def add_bj(self):
        self.new_msg+=str(chr(10266))
        self.write_msg()
        print(self.new_msg)
    def add_bk(self):
        self.new_msg+=str(chr(10245))
        self.write_msg()
        print(self.new_msg)
    def add_bl(self):
        self.new_msg+=str(chr(10247))
        self.write_msg()
        print(self.new_msg)
    def add_bm(self):
        self.new_msg+=str(chr(10253))
        self.write_msg()
        print(self.new_msg)
    def add_bn(self):
        self.new_msg+=str(chr(10269))
        self.write_msg()
        print(self.new_msg)
    def add_bo(self):
        self.new_msg+=str(chr(10261))
        self.write_msg()
        print(self.new_msg)
    def add_bp(self):
        self.new_msg+=str(chr(10255))
        self.write_msg()
        print(self.new_msg)
    def add_bq(self):
        self.new_msg+=str(chr(10271))
        self.write_msg()
        print(self.new_msg)
    def add_br(self):
        self.new_msg+=str(chr(10263))
        self.write_msg()
        print(self.new_msg)
    def add_bs(self):
        self.new_msg+=str(chr(10254))
        self.write_msg()
        print(self.new_msg)
    def add_bt(self):
        self.new_msg+=str(chr(10270))
        self.write_msg()
        print(self.new_msg)
    def add_bu(self):
        self.new_msg+=str(chr(10277))
        self.write_msg()
        print(self.new_msg)
    def add_bv(self):
        self.new_msg+=str(chr(10279))
        self.write_msg()
        print(self.new_msg)
    def add_bw(self):
        self.new_msg+=str(chr(10298))
        self.write_msg()
        print(self.new_msg)
    def add_bx(self):
        self.new_msg+=str(chr(10285))
        self.write_msg()
        print(self.new_msg)
    def add_by(self):
        self.new_msg+=str(chr(10301))
        self.write_msg()
        print(self.new_msg)
    def add_bz(self):
        self.new_msg+=str(chr(10293))
        self.write_msg()
        print(self.new_msg)
