from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store
cart = {}
order_count = 0
discount_codes = []

@app.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    quantity = request.json['quantity']
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    return jsonify({'message': 'Item added to cart'})

@app.route('/checkout', methods=['POST'])
def checkout():
    global order_count, discount_codes
    order_count += 1
    if order_count % 10 == 0:
        discount_code = generate_discount_code()
        discount_codes.append(discount_code)
        return jsonify({'message': f'Order placed successfully. You have received a discount code: {discount_code}'})
    else:
        return jsonify({'message': 'Order placed successfully'})

@app.route('/apply-discount/<discount_code>', methods=['POST'])
def apply_discount(discount_code):
    if discount_code not in discount_codes:
        return jsonify({'message': 'Invalid discount code'})
    else:
        # Apply discount to cart
        return jsonify({'message': 'Discount applied successfully'})

@app.route('/admin/generate-discount-code', methods=['GET'])
def generate_discount_code():
    return 'ABCDEFGH'

@app.route('/admin/purchase-summary', methods=['GET'])
def purchase_summary():
    items_purchased = sum(cart.values())
    total_purchase_amount = items_purchased * 100 # assuming each item costs $100
    total_discount_amount = len(discount_codes) * 10 # assuming each discount code gives a 10% discount
    return jsonify({
        'items_purchased': items_purchased,
        'total_purchase_amount': total_purchase_amount,
        'discount_codes': discount_codes,
        'total_discount_amount': total_discount_amount
    })

if __name__ == '__main__':
    app.run()