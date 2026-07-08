from food_order import food_order

def main():
    print("==FoodExpress ===")
    try:
        price_input = input("enter the meal: ")
        price = float(price_input)  
        
        quantity_input = input("enter quanatity: ")
        quantity = int(quantity_input)  
        
        result = food_order(price, quantity)
        
        if isinstance(result, str):
            print(f"error: {result}")
        else:
            print(f"tottal: {result} dollars")
    
    except ValueError:
        print("error")

if __name__ == "__main__":
    main()
