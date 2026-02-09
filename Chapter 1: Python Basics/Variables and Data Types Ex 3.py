# Exercise 3: Decision with Booleans and Type Conversion
#product status
is_ready=input("Enter if the product is ready (True/False): ").strip().lower()
#product weight
product_weight=float(input("Enter the weight (in kg): "))
#display the input
print(f"\nProduct packed status: {is_ready}")
print(f"Product weight: {product_weight}")
#conditions and output
if is_ready == "true" and product_weight > 0:
    print("Product is ready for shipment.")
else:
    print("Product is not ready for shipment.")