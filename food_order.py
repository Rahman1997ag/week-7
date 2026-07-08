def food_order(price, quantity):
    """
    تحسب الإجمالي لطلب الطعام مع التحقق من صحة المدخلات.
    :param price: سعر الوحدة (رقم موجب)
    :param quantity: الكمية (عدد صحيح موجب)
    :return: الإجمالي (price * quantity) أو رسالة خطأ مناسبة
    """
    # التحقق من أن السعر رقم موجب
    if not isinstance(price, (int, float)) or price <= 0:
        return "invalid price"
    
    # التحقق من أن الكمية عدد صحيح موجب
    if not isinstance(quantity, int) or quantity <= 0:
        return "invalid quantity"
    
    # حساب الإجمالي
    total = price * quantity
    return total
