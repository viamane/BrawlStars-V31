from Core.ConnectionHandler import Server

print("""
      

 ____   ____    ______    __    
|_  _| |_  _|  / ____ `. /  |   
  \ \   / /    `'  __) | `| |   
   \ \ / /     _  |__ '.  | |   
    \ ' /     | \____) | _| |_  
     \_/       \______.'|_____| 
                                

                          
   by Via.
                   
""")

server = Server('0.0.0.0', 9339) #Binding
server.start() #Starting