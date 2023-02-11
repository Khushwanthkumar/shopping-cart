# Shopping Cart

This code implements a simple e-commerce website with a shopping cart and checkout functionality, as well as several administrative APIs for retrieving information about the orders, items, and discounts. The code uses the Flask framework to handle HTTP requests and responses.

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

* `/add_to_cart` - API to add items to the cart.
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
    "item_id": 1,
    "item_name": "item1",
    "price": 100
}
```

### Checking out and placing an order

To checkout and place an order, make a POST request to /checkout endpoint with a JSON payload:

```
{
    "customer_name": "John Doe",
    "email": "johndoe@example.com"
}
```

### Admin APIs

To retrieve information using the admin APIs, make a GET request to the respective endpoint. For example, to retrieve the count of items purchased, make a GET request to `/admin/items_count`.

Note: The admin APIs are protected and can only be accessed by authorized users.

## Conclusion

This shopping cart application can be used as a starting point for building a full-fledged e-commerce platform. The application can be extended by adding more features like payment gateways, security, and scalability.