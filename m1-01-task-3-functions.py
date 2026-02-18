### Task 3: Build small functions for cleaning and conversion
def to_float(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return None

def clean_text(s):
    if isinstance(s, str):
        return s.strip().lower()
    return s


test_inputs = ["  12.5 ", "abc", " 100", "", "  DATA  "]

cleaned_texts = [clean_text(x) for x in test_inputs]
float_values = [to_float(clean_text(x)) for x in test_inputs]

print("Cleaned:", cleaned_texts)
print("Floats: ", float_values)
