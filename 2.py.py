
def solve(): 
    l = int(input()) 
    n = int(input()) 
    obstacles = [] 
    for _ in range(n): 
        obstacles.append(list(map(int, input().split()))) 

    max_distance = 0 
    best_obstacle_to_remove = 0 

    for obstacle_to_remove_index in range(-1, n): 
        
        current_obstacles = [] 
        for i, obs in enumerate(obstacles): 
             if i != obstacle_to_remove_index: 
                 current_obstacles.append(obs) 
                
        current_obstacles.sort(key = lambda x: x[0]) 
        
        position = 0 
        
        
        
        
        
        
        
        
        while position < l: 
            
          
           
            
            
            
            
            
            
            obstacle_hit = None 
            
            for obs in current_obstacles: 
                if obs[0] > position and obs[0] <= position +4 : 
                   
                    obstacle_hit = obs 
                    break 
            
            
            if obstacle_hit != None: 
                
                
                
                if obstacle_hit[0] in [x[0] for x in current_obstacles]: 
                    
                  
                    
                    
                   
                    
                    
                    
                  
                    
                    
                    break 
            
                
            
            
            
            
            position+= 1 
                
        
        if position > max_distance: 
             max_distance = position 
             if obstacle_to_remove_index != -1: 
                 best_obstacle_to_remove = obstacles[obstacle_to_remove_]
solve()
