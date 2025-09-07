#!/usr/bin/env python3
"""
Main application file for shyam-development-proj
A simple Python project demonstrating basic functionality.
"""

def main():
    """Main function to run the application."""
    print("Welcome to Shyam Development Project!")
    print("This is a Python development project.")
    
    # Basic functionality demonstration
    name = input("Enter your name: ")
    print(f"Hello, {name}! Thanks for trying this project.")
    
    # Simple calculation example
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")
    
    print("Project is running successfully!")

if __name__ == "__main__":
    main()