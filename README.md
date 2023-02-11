# Shopping Cart

This is a Flask web application for a shopping cart that enables customers to add items to the cart, checkout, and view order information.

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

* /add_to_cart - API to add items to the cart.
* /checkout - API to checkout and place an order.
* /admin/items_count - Admin API to retrieve the count of items purchased.
* /admin/total_purchase_amount - Admin API to retrieve the total purchase amount.
* /admin/discount_codes - Admin API to retrieve the list of discount codes.
* /admin/total_discount_amount - Admin API to retrieve the total discount amount.

