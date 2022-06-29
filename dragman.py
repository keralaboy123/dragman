
import pynput




#21/12/2019  

class  logicalAnalyser():
    " observe events  and save it then analyse logic by states "
    def is_something_true( STATE):
        pass 
    

class  logicalDragAnalyser():
    " if mouse moving while button pressed its dragging.. "

    class STATE :
        def __init__(self):        
           self.isholding = False
           self.mouseMoved = False
           
    def __init__(self):
        self.STATE = self.STATE()
        
    def mousemove( self):
        self.STATE.mouseMoved = True
        print ("button move  of  logicanalyser")
        
    def button_down( self):
        self.STATE.isholding = True
        print ("button down  of  logicanalyser")
        
    def button_up( self):
        self.STATE.isholding = False
        print ("button up  of  logicanalyser")
        
    def is_draging_happening( self ):
        print ("is draging  of  logicanalyser")
        if self.STATE.isholding:
             if self.STATE.mouseMoved:   #mouse moved before button up
                 self.STATE.mouseMoved = False
                 print ("keyisHolding  so draging true of LogicaldrageveMgr") 
                 return True
        print ("keyholding is false  not draging in logicalDragevnmgrr") 

class event:
        buttonDown = None
        buttonup =None
        moved= None

class eventManager(object):
    
    def __init__( self):
        self.__doc__= "handles all events "

    def notify(  self ,event ):
        pass

    def callback(  self, handle ):
        pass


    
class DragEventManager(eventManager):
        
    def __init__( self):
        self.__doc__= "handles drag events "
        self.logicalDragAnalyser = logicalDragAnalyser()        

    def on_click( self, x,y, button, notreleased):
                print ("onclick of drageveMgr")
                if notreleased :
                      print ("key   pressing  drageveMgr")
                      self.on_buttondown( )
                      
                      
                else:
                      print ("key released drageveMgr") 
                      self.on_buttonup( )                                           
                      
    def  on_buttonup( self):
             print (" on button up   of  DragEventManager ")
             self.logicalDragAnalyser.button_up()

    def  on_buttondown( self):
             print (" onButtonDown of DragEventManage  ")
             self.logicalDragAnalyser.button_down()

    def  on_move( self,x,y):
            print (" onMOve  of DragEventManage   ")
            self.logicalDragAnalyser.mousemove()
            print("checking  is drag happened  on DRageventmgr")
            if self.logicalDragAnalyser.is_draging_happening():
                       print("drag happened so calling handler  on DRageventmgr")
                       self.on_dragEvent()
            else:
                     print("no drag event  on DRageventmgr")
                     pass
                    
    def on_dragEvent( self):
               print ("on_DRAG  of   DragEventManager  drag happened   ")
               pass
        


