def get_positive_float(prompt):
    """Prompts user for input and ensures it is a positive float."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Value must be greater than zero. please try again.")
            else:
                return value
        except ValueError:
            print("Error:Invalid input. Please try a valid number.")
            
def calculate_bmi(weight, height):
    """Calculates BMI using the formula: weight / (height)^2."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Classify BMI into standard health categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"
    
def main():
    print("=== BMI Calculator ===")
    
    # Get input with validation
    weight = get_positive_float("Enter your weight in kg: ")
    height = get_positive_float("Enter your height in m: ")
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Get BMI category
    category = get_bmi_category(bmi)
    
    # Display result rounded to 2 decimal places
    print("\n=== BMI Result ===")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")
    
if __name__ == "__main__":
    main()