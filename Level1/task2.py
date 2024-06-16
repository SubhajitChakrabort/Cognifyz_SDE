def generate_pyramid_pattern(rows):
   
    for i in range(1, rows + 1):
      
        for j in range(rows - i):
            print(" ", end="")
        
       
        for j in range(1, i + 1):
            print(j, end=" ")
        
      
        print()

if __name__ == "__main__":
    number_of_rows = 5 
    generate_pyramid_pattern(number_of_rows)
