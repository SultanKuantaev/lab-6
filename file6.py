import os

def generate_files_in_directory(directory):
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    
    for i in range(65, 91):  
        filename = f"{chr(i)}.txt"  
        filepath = os.path.join(directory, filename)  
        with open(filepath, 'w') as file:  
            pass 


generate_files_in_directory('alphabet_files')
