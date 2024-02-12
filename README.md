Point Quadrant Determination
This Python program prompts the user to input the coordinates of a point in the plane (x, y) and then determines and prints the quadrant in which the point is located.

Usage
Run the Python script (quadrant_determination.py).
Enter the x and y coordinates as prompted.
The program will output a message indicating the quadrant in which the point is located.
Code Explanation
The main functionality is encapsulated in the determine_quadrant function, which takes the x and y coordinates as parameters and returns a string indicating the quadrant. The program then takes user input, calls this function, and prints the result.

python
Copy code
def determine_quadrant(x, y):
    # ... (code to determine quadrant)

# Ask the user to input coordinates
try:
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))
    
    # Determine the quadrant
    result = determine_quadrant(x, y)
    
    # Print the result
    print(result)

except ValueError:
    print("Error: Enter valid integer values for x and y.")
Quadrant Definitions
First Quadrant: x > 0 and y > 0
Second Quadrant: x < 0 and y > 0
Third Quadrant: x < 0 and y < 0
Fourth Quadrant: x > 0 and y < 0
On Y-axis: x == 0 and y != 0
On X-axis: x != 0 and y == 0
At Origin: x == 0 and y == 0
Input Validation
The program includes basic input validation to ensure that the user enters valid integer values for x and y. If non-integer values are entered, an error message is displayed.

Feel free to use and modify this code as needed for your specific requirements.
