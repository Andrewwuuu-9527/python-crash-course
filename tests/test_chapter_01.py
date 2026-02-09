#!/usr/bin/env python3
"""
Unit tests for Chapter 01: Advanced Hello World Program
Uses pytest framework for comprehensive testing.
Designed for UC Berkeley CS/Math curriculum.
"""

import pytest
import sys
from datetime import datetime
from unittest.mock import patch
from io import StringIO

# Import functions from chapter 1
sys.path.insert(0, 'chapter_01/hello_world')
from advanced_hello import (
    generate_greeting,
    calculate_fibonacci,
    display_system_info,
    analyze_fibonacci_properties,
    get_user_input
)


class TestGreetingFunctions:
    """Test suite for greeting-related functions."""
    
    def test_generate_greeting_default(self) -> None:
        """Test greeting generation with default parameter."""
        # Arrange & Act
        result = generate_greeting()
        
        # Assert
        assert isinstance(result, str)
        assert "World" in result
        assert result.endswith("👋")
    
    def test_generate_greeting_custom_name(self) -> None:
        """Test greeting generation with custom name."""
        # Arrange
        test_name = "Alice"
        
        # Act
        result = generate_greeting(test_name)
        
        # Assert
        assert test_name in result
        assert result.startswith(("Good morning", "Good afternoon", 
                                "Good evening", "Good night"))
    
    def test_generate_greeting_with_whitespace(self) -> None:
        """Test greeting generation with name containing whitespace."""
        # Arrange
        test_name = "  John Doe  "
        
        # Act
        result = generate_greeting(test_name)
        
        # Assert
        assert "John Doe" in result
    
    def test_generate_greeting_type_error(self) -> None:
        """Test that non-string input raises TypeError."""
        # Arrange
        invalid_inputs = [123, 45.67, None, [], {}]
        
        # Act & Assert
        for invalid_input in invalid_inputs:
            with pytest.raises(TypeError, match="Name must be a string"):
                generate_greeting(invalid_input)
    
    def test_generate_greeting_value_error(self) -> None:
        """Test that empty or whitespace-only name raises ValueError."""
        # Arrange
        invalid_names = ["", "   ", "\t\n", " " * 10]
        
        # Act & Assert
        for name in invalid_names:
            with pytest.raises(ValueError, match="Name cannot be empty"):
                generate_greeting(name)


class TestFibonacciFunctions:
    """Test suite for Fibonacci sequence functions."""
    
    def test_calculate_fibonacci_base_cases(self) -> None:
        """Test Fibonacci calculation with small n values."""
        # Test n = 1
        assert calculate_fibonacci(1) == [0]
        
        # Test n = 2
        assert calculate_fibonacci(2) == [0, 1]
        
        # Test n = 3
        assert calculate_fibonacci(3) == [0, 1, 1]
    
    def test_calculate_fibonacci_standard(self) -> None:
        """Test Fibonacci calculation with standard input."""
        # Arrange
        n = 10
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        
        # Act
        result = calculate_fibonacci(n)
        
        # Assert
        assert result == expected
        assert len(result) == n
    
    def test_calculate_fibonacci_large_n(self) -> None:
        """Test Fibonacci calculation with larger n value."""
        # Arrange
        n = 20
        
        # Act
        result = calculate_fibonacci(n)
        
        # Assert
        assert len(result) == n
        assert result[0] == 0
        assert result[1] == 1
        
        # Verify Fibonacci property: F_n = F_{n-1} + F_{n-2}
        for i in range(2, n):
            assert result[i] == result[i-1] + result[i-2]
    
    def test_calculate_fibonacci_negative_input(self) -> None:
        """Test that negative input raises ValueError."""
        # Arrange
        negative_values = [-1, -5, -100]
        
        # Act & Assert
        for n in negative_values:
            with pytest.raises(ValueError, match="must be a positive integer"):
                calculate_fibonacci(n)
    
    def test_calculate_fibonacci_zero_input(self) -> None:
        """Test that zero input raises ValueError."""
        with pytest.raises(ValueError, match="must be a positive integer"):
            calculate_fibonacci(0)


class TestFibonacciAnalysis:
    """Test suite for Fibonacci analysis functions."""
    
    def test_analyze_fibonacci_properties_short_sequence(self) -> None:
        """Test analysis with short Fibonacci sequence."""
        # Arrange
        sequence = [0, 1, 1, 2, 3]
        
        # Act
        properties = analyze_fibonacci_properties(sequence)
        
        # Assert
        assert properties["sequence_length"] == 5
        assert properties["sum"] == 7
        assert properties["max"] == 3
        assert properties["min"] == 0
        assert properties["average"] == 1.4
        assert len(properties["ratios"]) == 4
    
    def test_analyze_fibonacci_properties_single_element(self) -> None:
        """Test analysis with single-element sequence."""
        # Arrange
        sequence = [0]
        
        # Act
        properties = analyze_fibonacci_properties(sequence)
        
        # Assert
        assert "error" in properties
        assert properties["error"] == "Sequence too short for analysis"
    
    def test_analyze_fibonacci_properties_empty_sequence(self) -> None:
        """Test analysis with empty sequence."""
        # Arrange
        sequence = []
        
        # Act
        properties = analyze_fibonacci_properties(sequence)
        
        # Assert
        assert "error" in properties
        assert properties["error"] == "Sequence too short for analysis"
    
    def test_analyze_fibonacci_properties_ratio_calculation(self) -> None:
        """Test ratio calculations in Fibonacci analysis."""
        # Arrange
        sequence = [0, 1, 1, 2, 3, 5]
        
        # Act
        properties = analyze_fibonacci_properties(sequence)
        
        # Assert
        expected_ratios = [1.0, 1.0, 2.0, 1.5, 5/3]
        assert len(properties["ratios"]) == len(expected_ratios)
        
        for actual, expected in zip(properties["ratios"], expected_ratios):
            assert abs(actual - expected) < 1e-10


class TestUtilityFunctions:
    """Test suite for utility functions."""
    
    @patch('builtins.input', return_value='Alice')
    def test_get_user_input_with_value(self, mock_input: object) -> None:
        """Test get_user_input when user provides a value."""
        # Act
        result = get_user_input("Enter name")
        
        # Assert
        assert result == 'Alice'
        mock_input.assert_called_once_with("Enter name: ")
    
    @patch('builtins.input', return_value='')
    def test_get_user_input_empty_with_default(self, mock_input: object) -> None:
        """Test get_user_input when user enters empty with default."""
        # Act
        result = get_user_input("Enter name", "DefaultName")
        
        # Assert
        assert result == 'DefaultName'
        mock_input.assert_called_once_with("Enter name [DefaultName]: ")
    
    @patch('builtins.input', return_value='')
    def test_get_user_input_empty_no_default(self, mock_input: object) -> None:
        """Test get_user_input when user enters empty without default."""
        # Act
        result = get_user_input("Enter name")
        
        # Assert
        assert result == ''
        mock_input.assert_called_once_with("Enter name: ")
    
    @patch('builtins.input', side_effect=KeyboardInterrupt)
    def test_get_user_input_keyboard_interrupt(self, mock_input: object) -> None:
        """Test get_user_input handling of KeyboardInterrupt."""
        # Act
        result = get_user_input("Enter name", "Default")
        
        # Assert
        assert result == 'Default'
    
    @patch('builtins.input', side_effect=EOFError)
    def test_get_user_input_eof_error(self, mock_input: object) -> None:
        """Test get_user_input handling of EOFError."""
        # Act
        result = get_user_input("Enter name", "Default")
        
        # Assert
        assert result == 'Default'


class TestSystemInfoFunction:
    """Test suite for system information display function."""
    
    def test_display_system_info_output(self, capsys: pytest.CaptureFixture) -> None:
        """Test that display_system_info prints expected information."""
        # Act
        display_system_info()
        captured = capsys.readouterr()
        
        # Assert
        assert "SYSTEM INFORMATION" in captured.out
        assert "Python Version" in captured.out
        assert "Platform" in captured.out
        assert "System" in captured.out
        assert "Processor" in captured.out
        assert "=" * 60 in captured.out


def test_module_importability() -> None:
    """Test that the advanced_hello module can be imported."""
    # This test ensures the module has no syntax errors
    try:
        import chapter_01.hello_world.advanced_hello as module
        assert module is not None
    except ImportError as e:
        pytest.fail(f"Failed to import module: {e}")


if __name__ == "__main__":
    # Allow running tests directly: python test_chapter_01.py
    pytest.main([__file__, "-v", "--tb=short"])