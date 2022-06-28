from  dragman  import  DragEventManager,pynput

emu = pynput.mouse.Controller()

# print removed by commenting 
class maper (DragEventManager):
        listener = None
        draged = False
        skipque= []
       

        def  isDragedLast(self): 
           if self.draged:
               self.draged = False
               return True

        def  __init__(self):
            super().__init__()

        def   shouldskip(self  ):          
              if   self.skipque :
                   self.skipque.pop()
                   return  True
 
        def stop(  self):
                self.listener.stop()

        def run(  self ):            
                
                self.listener = pynput.mouse.Listener( on_move=self.on_move, on_click=self.on_click) 
                self.listener.start()
               
            
        def on_click( self, x,y, button, buttonpressing  ):
             if   self.shouldskip(): # these clicks are emulated echo  so skip it.
                     self.listener.suppress_event()
                     return True
                
             if  button == pynput.mouse.Button.left:
                     
                     return 
                     
             elif  button == pynput.mouse.Button.right:

                     #print ("onclick of   of  maper") 
                     super().on_click( x,y, button, buttonpressing )
                     
                     if  buttonpressing is False:  # handsup
                             #print(" button released on maper checking for  lastdrag event")

                             if self.isDragedLast():
                                     #print("there was a drag so this button release have nothing to handle")
                                     pass

                             else:                            
                                      #print("no drag happened  its a right  clickRelease so emulating   RIGHT button")
                                      
                                      self.skipque.append( pynput.mouse.Button.right)
                                      self.skipque.append( pynput.mouse.Button.right)
                                      emu.click(pynput.mouse.Button.right)   # if there was no mouse movement between press and release then it was jus a click
                                     
                                      
                             
                                                           
                     
             self.listener.suppress_event()  # just  stop event here
                                
        def  on_dragEvent(self):                           
                    self.draged = True                    
                    emu.scroll(0, -4)
                    
                    

if __name__ =="__main__"   :        
     a=maper()
     import time; time.sleep(4); a.run()


