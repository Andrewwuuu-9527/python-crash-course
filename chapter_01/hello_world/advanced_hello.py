#!/usr/bin/env python3
"""
Advanced Hello World Program
Demonstrates basic Python syntax, docstrings, and best practices.
Designed for UC Berkeley CS/Math students.
"""

import sys
import platform
from datetime import datetime
from typing import NoReturn, List, Dict, Any
import math


def display_system_info() -> None:
    """
    Display system information including Python version and platform details.
    
    Returns:
        None: Prints system information to console.
    """
    print("=" * 60)
    print("SYSTEM INFORMATION")
    print("=" * 60)
    print(f"Python Version: {platform.python_version()}")
    print(f"Platform: {platform.platform()}")
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print(f"Machine: {platform.machine()}")
    print(f"Architecture: {platform.architecture()[0]}")
    print("=" * 60)


def generate_greeting(name: str = "World") -> str:
    """
    Generate a personalized greeting message based on time of day.
    
    Args:
        name (str): Name to greet. Defaults to "World".
        
    Returns:
        str: Formatted greeting message.
        
    Raises:
        TypeError: If name is not a string.
        ValueError: If name is empty or contains only whitespace.
    """
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    
    if not name.strip():
        raise ValueError("Name cannot be empty or whitespace only")
    
    current_hour = datetime.now().hour
    
    # Determine time-based greeting
    if 5 <= current_hour < 12:
        time_greeting = "Good morning"
    elif 12 <= current_hour < 18:
        time_greeting = "Good afternoon"
    elif 18 <= current_hour < 22:
        time_greeting = "Good evening"
    else:
        time_greeting = "Good night"
    
    return f"{time_greeting}, {name}! 👋"


def display_ascii_art() -> None:
    """
    Display UC Berkeley and Python-themed ASCII art.
    """
    art = r"""
     ____        _   _                 ____            _       _       
    |  _ \ _   _| |_| |__   ___  _ __ | __ ) _ __ ___ | | __ _| |_ ___ 
    | |_) | | | | __| '_ \ / _ \| '_ \|  _ \| '__/ _ \| |/ _` | __/ _ \
    |  __/| |_| | |_| | | | (_) | | | | |_) | | | (_) | | (_| | |_  __/
    |_|    \__, |\__|_| |_|\___/|_| |_|____/|_|  \___/|_|\__,_|\__\___|
           |___/                                                       
    
    University of California, Berkeley
    College of Engineering
    Department of Computer Science & Applied Mathematics
    
    Python Crash Course - Professional Implementation
    """
    print(art)


def calculate_fibonacci(n: int = 10) -> List[int]:
    """
    Calculate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of terms to calculate. Defaults to 10.
        
    Returns:
        List[int]: List of Fibonacci numbers.
        
    Raises:
        ValueError: If n is not positive.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence


def analyze_fibonacci_properties(fib_sequence: List[int]) -> Dict[str, Any]:
    """
    Analyze mathematical properties of a Fibonacci sequence.
    
    Args:
        fib_sequence (List[int]): List of Fibonacci numbers.
        
    Returns:
        Dict[str, Any]: Dictionary containing analysis results.
    """
    if len(fib_sequence) < 2:
        return {"error": "Sequence too short for analysis"}
    
    properties = {
        "sequence_length": len(fib_sequence),
        "sum": sum(fib_sequence),
        "max": max(fib_sequence),
        "min": min(fib_sequence),
        "average": sum(fib_sequence) / len(fib_sequence),
        "ratios": [],
        "golden_ratio_approximations": []
    }
    
    # Calculate consecutive ratios
    for i in range(1, len(fib_sequence)):
        if fib_sequence[i-1] != 0:
            ratio = fib_sequence[i] / fib_sequence[i-1]
            properties["ratios"].append(ratio)
    
    # Calculate golden ratio approximations
    golden_ratio = (1 + math.sqrt(5)) / 2
    if len(properties["ratios"]) > 0:
        properties["golden_ratio_approximations"] = [
            abs(ratio - golden_ratio) for ratio in properties["ratios"]
        ]
        properties["best_approximation"] = min(properties["golden_ratio_approximations"])
        properties["best_approximation_index"] = properties["golden_ratio_approximations"].index(
            properties["best_approximation"]
        )
    
    return properties


def display_mathematical_demo(fib_sequence: List[int]) -> None:
    """
    Display mathematical demonstration of Fibonacci properties.
    
    Args:
        fib_sequence (List[int]): Fibonacci sequence to analyze.
    """
    print("\n" + "=" * 60)
    print("MATHEMATICAL DEMONSTRATION")
    print("=" * 60)
    
    # Display Fibonacci sequence
    print(f"Fibonacci Sequence (first {len(fib_sequence)} terms):")
    for i, num in enumerate(fib_sequence):
        print(f"  F_{i}: {num:,}")
    
    # Analyze properties
    properties = analyze_fibonacci_properties(fib_sequence)
    
    print(f"\nMathematical Properties:")
    print(f"  Sum of sequence: {properties['sum']:,}")
    print(f"  Maximum value: {properties['max']:,}")
    print(f"  Minimum value: {properties['min']:,}")
    print(f"  Average value: {properties['average']:.2f}")
    
    if properties["ratios"]:
        print(f"\nConsecutive Ratios (F_n/F_{{n-1}}):")
        for i, ratio in enumerate(properties["ratios"], 1):
            print(f"  Ratio {i}: {ratio:.8f}")
        
        golden_ratio = (1 + math.sqrt(5)) / 2
        print(f"\nGolden Ratio (φ): {golden_ratio:.8f}")
        print(f"Best approximation: {properties['ratios'][properties['best_approximation_index']]:.8f}")
        print(f"Difference: {properties['best_approximation']:.10f}")


def get_user_input(prompt: str, default: str = "") -> str:
    """
    Get user input with validation and default value support.
    
    Args:
        prompt (str): Prompt to display to user.
        default (str): Default value if user enters nothing.
        
    Returns:
        str: User input or default value.
    """
    try:
        if default:
            user_input = input(f"{prompt} [{default}]: ").strip()
        else:
            user_input = input(f"{prompt}: ").strip()
        
        return user_input if user_input else default
    except (EOFError, KeyboardInterrupt):
        print("\n\nInput cancelled by user.")
        return default


def main() -> NoReturn:
    """
    Main program entry point.
    
    Returns:
        NoReturn: Program exits after execution.
    """
    try:
        # Display ASCII art
        display_ascii_art()
        
        # Show system information
        display_system_info()
        
        # Get user input with validation
        print("\n" + "=" * 60)
        print("USER INPUT SECTION")
        print("=" * 60)
        
        user_name = get_user_input("Please enter your name", "World")
        
        # Generate and display greeting
        greeting = generate_greeting(user_name)
        print(f"\n{greeting}")
        
        # Get Fibonacci sequence length
        fib_length_str = get_user_input("Enter number of Fibonacci terms to calculate", "15")
        
        try:
            fib_length = int(fib_length_str)
            if fib_length <= 0:
                print("Invalid input. Using default value (15).")
                fib_length = 15
        except ValueError:
            print("Invalid number. Using default value (15).")
            fib_length = 15
        
        # Limit to reasonable size for display
        fib_length = min(fib_length, 50)
        
        # Calculate and display Fibonacci sequence
        fib_numbers = calculate_fibonacci(fib_length)
        display_mathematical_demo(fib_numbers)
        
        # Display completion message
        print("\n" + "=" * 60)
        print("PROGRAM COMPLETED SUCCESSFULLY! ✅")
        print("=" * 60)
        print("\nSummary:")
        print(f"  - Greeted: {user_name}")
        print(f"  - Calculated: {fib_length} Fibonacci terms")
        print(f"  - Max Fibonacci value: {max(fib_numbers):,}")
        print("=" * 60)
        
        sys.exit(0)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user.")
        sys.exit(130)  # Standard exit code for Ctrl+C
    except Exception as e:
        print(f"\n❌ Error: {type(e).__name__}: {e}")
        print("\nPlease report this issue or check your inputs.")
        sys.exit(1)


if __name__ == "__main__":
    # This ensures the script can be imported without running main()
    main()