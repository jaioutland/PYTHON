print("Real Estate Property Estimator, based on a sales prices of 395000, 4 bedroom, 3.5 bathroom home and 2750 square feet.\nThe annual taxes are 4500 dollars and the annual insurance premium is 2000 dollars.", end= "-")

# Literals Property Information
sale_price = 395000
bedrooms = 4
bathrooms = 3.5
annual_taxes = 4500
square_footage = 2750
property_insurance = 2000
print()

# Addition Total Property Cost
total_cost = sale_price + annual_taxes + property_insurance
print("\nAddition: ")
print(total_cost)
print()

# Subtraction
diff = sale_price - property_insurance
print("\nSubtraction: ")
print(diff)
print()

# Multiplication (Note: This is not cost per sqft, it's just multiplication example)
product = sale_price * square_footage
print("\nMultiplication: ")
print(product)
print()

# Division Price per Sqft.
price_per_sqft = sale_price / square_footage
print("\nDivision: ")
print(price_per_sqft)
print()

# Integer Division Price per Sqft.
integer_division = sale_price // square_footage
print("\nInteger Division: ")
print(integer_division)
print()

# Modulus Price per Sqft.
remainder = sale_price % square_footage
print("\nModulus: ")
print(remainder)
print()

# Exponentiation (Example: Square footage squared)
square_of_sqft = square_footage ** 2
print("\nExponentiation: ")
print(square_of_sqft)
print()

# Final Concatenation
print("The total cost of the property is " + str(sum) + ", with a price per square foot of " + str(product) + " and a squared footage of " + str(square_of_sqft) + " sqft².")