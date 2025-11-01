"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

import re

def count_characters(text):
    """Count non-space characters in a string."""
    return len(text.replace(" ", ""))

def count_words(text):
    """Count number of words in a string."""
    return len(text.split())

def extract_numbers(text):
    """Return list of integers found in text."""
    return [int(num) for num in re.findall(r'\d+', text)]

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    char_count = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)

    total = sum(numbers) if numbers else 0
    average = total / len(numbers) if numbers else 0

    return {
        "characters": char_count,
        "words": word_count,
        "numbers": numbers,
        "sum": total,
        "average": average
    }

if __name__ == "__main__":
    text = input("Enter some text: ")
    result = analyze_text(text)

    print("\n--- Text Analysis ---")
    print(f"Non-space characters: {result['characters']}")
    print(f"Word count: {result['words']}")
    print(f"Numbers found: {result['numbers']}")
    print(f"Sum of numbers: {result['sum']}")
    print(f"Average of numbers: {result['average']:.2f}")
