def count_down(count):
    if count == 0:            
        print('Go!')                  
    else:                        
        print(count)             
        count_down(count-1)        
            
count_down(992)