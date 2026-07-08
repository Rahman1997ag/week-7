from food_order import food_order

def main():
    print("=== نظام طلب الطعام FoodExpress ===")
    try:
        # طلب إدخال السعر
        price_input = input("أدخل سعر الوجبة: ")
        price = float(price_input)  # قد يرمي ValueError
        
        # طلب إدخال الكمية
        quantity_input = input("أدخل الكمية: ")
        quantity = int(quantity_input)  # قد يرمي ValueError
        
        # استدعاء الدالة
        result = food_order(price, quantity)
        
        # عرض النتيجة أو رسالة الخطأ
        if isinstance(result, str):
            print(f"خطأ: {result}")
        else:
            print(f"الإجمالي: {result} ريال")
    
    except ValueError:
        print("خطأ: يرجى إدخال أرقام صحيحة (السعر عدد عشري، الكمية عدد صحيح)")

if __name__ == "__main__":
    main()
