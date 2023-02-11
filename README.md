# Shopping Cart

This code implements a simple e-commerce website with a shopping cart and checkout functionality, as well as several administrative APIs for retrieving information about the orders, items, and discounts. The code uses the Flask framework to handle HTTP requests and responses.

The shopping cart and discount code information are stored in-memory using Python lists. A helper function, `generate_discount_code`, is provided to generate new discount codes.

The main APIs include:

* `/add_to_cart`: Adds an item to the cart. This API expects a JSON request with the fields "name" and "price" representing the name and price of the item.

* `/checkout`: Checks out the items in the cart and places an order. This API expects an optional JSON request with the field "discount_code". If the order is the nth order (where n is a multiple of 3), a new discount code is generated and returned in the response. If a discount code is provided, it will be checked for validity and the order will be placed with a discount if the code is valid.

The administrative APIs include:

* `/admin/items_count`: Retrieves the count of items in the cart.

* `/admin/total_purchase_amount`: Retrieves the total purchase amount of all items in the cart.

* `/admin/discount_codes`: Retrieves the list of all generated discount codes.

* `/admin/total_discount_amount`: Retrieves the total amount of discounts applied to all items in the cart.

Error handling has been added to validate the input data in several of the APIs and to check if the cart is empty before calculating certain values. However, additional error handling and edge case testing may be necessary to ensure the robustness and reliability of the code in a real-world scenario.

## Features

* Add items to the cart
* Checkout and place order
* Generate discount code for every 3rd order
* Admin APIs to retrieve information about items purchased, total purchase amount, discount codes, and total discount amount.

## Requirements

* Flask
* Python3

## How to run

1. Clone the repository:

```
git clone https://github.com/Khushwanthkumar/shopping-cart.git
```

2. Navigate to the directory:

```
cd shopping-cart
```

3. Install the dependencies:

```
pip install flask
```

4. Run the application:

```
python main.py
```

## Endpoints

The following endpoints are available:

* `/add_to_cart` - API to add item to the cart.
* `/checkout` - API to checkout and place an order.
* `/admin/items_count` - Admin API to retrieve the count of items purchased.
* `/admin/total_purchase_amount` - Admin API to retrieve the total purchase amount.
* `/admin/discount_codes` - Admin API to retrieve the list of discount codes.
* `/admin/total_discount_amount` - Admin API to retrieve the total discount amount.

 ## Examples

 ### Adding items to the cart

 To add an item to the cart, make a POST request to /add_to_cart endpoint with a JSON payload:

 ```
{
    "name": <item name>,
    "price": <item price>
}
```

### Checking out and placing an order

To checkout and place an order, make a POST request to /checkout endpoint with a JSON payload:

```
{
    "discount_code": <discount code>
}
```

### Admin APIs

To retrieve information using the admin APIs, make a GET request to the respective endpoint. For example, to retrieve the count of items purchased, make a GET request to `/admin/items_count`.

Note: The admin APIs are protected and can only be accessed by authorized users in real-life sceanrio you can implement the jwt authorization at the end of main.py for implementation by updating the keys.

## Conclusion

This shopping cart application can be used as a starting point for building a full-fledged e-commerce platform. The application can be extended by adding more features like payment gateways, security, and scalability.