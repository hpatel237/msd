# Fixes Report

## 1. divide_numbers
**Bug:** No handling of division by zero.  
**How I found it:** Test `test_divide_zero_divisor()` raised an unhandled ZeroDivisionError.  
**Fix:** Added a check `if b == 0: raise ZeroDivisionError`.

## 2. reverse_string
**Bug:** Crashed if non-string input (e.g., int) was given.  
**How I found it:** Test `test_reverse_non_string()` failed.  
**Fix:** Added `if not isinstance(s, str): raise TypeError`.

## 3. get_list_element
**Bug:** `if index < len(lst)` didn’t handle negative indices or out-of-bounds properly.  
**How I found it:** Test `test_get_element_negative_index()` returned wrong value; `test_get_element_out_of_range()` didn’t raise error.  
**Fix:** Let the built-in index behavior raise `IndexError`. Removed manual check.
