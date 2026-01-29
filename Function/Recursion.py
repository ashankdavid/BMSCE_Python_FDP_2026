def function(count):
    count += 1
    print("Hii")
    if count<15: # Base Case
        function(count)  # Recursive Case
    else:
        return


function(10)
