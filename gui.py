import tkinter as tk
from tkinter import messagebox
import  mapman
import io,sys

class logger(io.StringIO) :
     pass

#out,err = sys.stdout  , sys.stderr
#log = sys.stdout = sys.stderror= logger()

class gui( mapman.maper):
       root = tk.Tk()
       
       def run( self ):      
            self.root.protocol("WM_DELETE_WINDOW", self.stop)
            super().run()
            self.root.mainloop()
            
       def  stop( self ):           
                  super().stop()
                  self.root.destroy()


if __name__=="__main__":
       gui().run()
