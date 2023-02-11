from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store for cart items
cart = []

# In-memory store for discount codes
discount_codes = []

# Counter for nth order
order_counter = 0


# Helper function to generate discount code
def generate_discount_code():
    return "DISCOUNT" + str(len(discount_codes) + 1)


# API to add items to cart
@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    """
    API to add item to the cart.
    Expects a JSON request with the following format:
        {
            "name": <item name>,
            "price": <item price>
        }
    """
    # Get the item information from the request
    item = request.get_json()

    # Validate that the request has all the required fields
    if "name" not in item or "price" not in item:
        return (
            jsonify(
                {
                    "message": "Bad Request: Missing required fields 'name' and/or 'price'"
                }
            ),
            400,
        )

    # Validate the price of the item
    try:
        item_price = float(item.get("price"))
    except ValueError:
        return jsonify({"message": "Bad Request: Invalid value for 'price'"}), 400

    # Add the item to the cart
    cart.append({"name": item.get("name"), "price": item_price})
    return jsonify({"message": "Item added to cart successfully"})


# API to checkout and place order
@app.route("/checkout", methods=["POST"])
def checkout():
    """
    API to checkout and place an order.
    Expects a JSON request with the following format (optional):
        {
            "discount_code": <discount code>
        }
    """
    global order_counter
    order_counter += 1

    # Check if order is nth order and generate discount code
    if order_counter % 3 == 0:
        discount_code = generate_discount_code()
        discount_codes.append(discount_code)
        return jsonify(
            {"message": "Order placed successfully with discount code " + discount_code}
        )

    # Validate if discount code is valid
    discount_code = request.get_json().get("discount_code")
    if discount_code and discount_code in discount_codes:
        return jsonify({"message": "Order placed successfully with discount"})

    # Return success message if no discount code is provided or provided discount code is invalid
    return jsonify({"message": "Order placed successfully"})


# Admin API to list count of items purchased
@app.route("/admin/items_count", methods=["GET"])
def items_count():
    """
    Admin API to retrieve the count of items purchased.
    """
    return jsonify({"count": len(cart)})


# Admin API to list total purchase amount
@app.route("/admin/total_purchase_amount", methods=["GET"])
def total_purchase_amount():
    """
    Admin API to retrieve the total purchase amount.
    """
    if len(cart) == 0:  # checking the cart items before computing the total discount
        return jsonify({"Cart is empty!!"}), 400

    total = sum([item.get("price") for item in cart])
    return jsonify({"amount": total})


# Admin API to list discount codes
@app.route("/admin/discount_codes", methods=["GET"])
def discount_codes_list():
    """
    Admin API to retrieve the list of discount codes.
    """
    return jsonify({"codes": discount_codes})


# Admin API to list total discount amount
@app.route("/admin/total_discount_amount", methods=["GET"])
def total_discount_amount():
    """
    Admin API to retrieve the total discount amount.
    """
    if len(cart) == 0:  # checking the cart items before computing the total discount
        return jsonify({"Cart is empty!!"}), 400

    total = sum(
        [
            item.get("price") * 0.1
            for item in cart
            if item.get("discount_code") in discount_codes
        ]
    )
    return jsonify({"amount": total})


if __name__ == "__main__":
    app.run(debug=True)


# To improve the code to cover edge cases, we can add the following:

# Validate the discount code input in the checkout API and return an error message if it's invalid. -- done
# Add error handling for the case where the price of the item in the add_to_cart API is not a valid number. -- done
# Check if the cart is empty before calculating the total purchase amount and total discount amount. -- done
# Add authentication and authorization for the admin APIs to prevent unauthorized access. -- jwt authorization can be used as below to keep in check the of unauthorized users as below

    # app.config['SECRET_KEY'] = 'secret-key'  # Change this to your own secret key

    # @app.route('/login', methods=['POST'])
    # def login():
    #     # Authenticate the user and return a JWT token if the authentication is successful
    #     # In a real-world scenario, this should be replaced with your own authentication logic
    #     auth = request.authorization
    #     if auth and auth.username == 'admin' and auth.password == 'password':
    #         token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
    #                           app.config['SECRET_KEY'])
    #         return jsonify({'token': token.decode('UTF-8')})
    #     return jsonify({'message': 'Invalid credentials'}), 401

    # def check_for_token(func):
    #     def wrapper(*args, **kwargs):
    #         token = request.args.get('token') or request.headers.get('Authorization')
    #         if not token:
    #             return jsonify({'message': 'Token is missing'}), 401
    #         try:
    #             data = jwt.decode(token, app.config['SECRET_KEY'])
    #         except:
    #             return jsonify({'message': 'Token is invalid'}), 401
    #         return func(*args, **kwargs)
    #     return wrapper

# To use this decorator, we added it to each of the admin end

# "nth order" refers to an order that is the nth order placed by a customer. For example, if a customer places 10 orders, the 10th order would be referred to as the "10th order." In the above code, the variable "order_counter" is being used to track the number of orders that have been placed and the value of "order_counter" is incremented each time a customer places an order. If the value of "order_counter" is divisible by 3, a discount code is generated for the customer and added to the list of discount codes.

#we can even add a opentracing to the above each api for jeager tracing based on the requriements as below.
    # from flask_opentracing import FlaskTracer
    # from jaeger_client import Config
    # # Initializing the Jaeger tracer
    # config = Config(
    #     config={
    #         'sampler': {
    #             'type': 'const',
    #             'param': 1,
    #         },
    #         'logging': True,
    #     },
    #     service_name='cart-service'
    # )
    # jaeger_tracer = config.initialize_tracer()
    # opentracing.tracer = jaeger_tracer

    # # Flask tracer to integrate Flask with OpenTracing
    # flask_tracer = FlaskTracer(jaeger_tracer, app)

    # # Admin API to list count of items purchased
    # @app.route('/admin/items_count', methods=['GET'])
    # def items_count():
    #     """
    #     Admin API to retrieve the count of items purchased.
    #     """
    #     # Adding OpenTracing span to track the duration of the function
    #     with jaeger_tracer.start_active_span('items_count') as scope:
    #         count = len(cart)
    #         scope.span.log_kv({'event': 'items_count', 'count': count})
    #         return jsonify({"count": count})
