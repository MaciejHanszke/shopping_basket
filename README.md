# Shopping Basket
## Table of contents
* [General info](#general-info)
* [Configurations](#Configurations)
* [Setup](#setup)

## General info
This project is an implementation of [Shopping basket interview assignment](https://github.com/ecs-cx/cx-interview-questions/blob/master/shopping_basket/assignment.md).
	
## Configurations
Currently, there is a possibility to configure the products and discounts available in the system, by modifying corresponding file:\
	offers.json - for modifying discounts\
	product_list.json - for modifying products

### Offers
Each offer should consist of:
```
"beans_3_for_2":{  -- Name of the promo
  "qualification_item_ids":[1],  -- the array of product id's that will count toward triggering this promotion
  "qualifying_no":3,  -- number of items, that will trigger this promo, in this case, every 3rd item will trigger that promotion
  "discount_size":100  -- discount value for the triggered product, in this case, every 3rd item will be free
}
```

### Product List
Each product should consist of:
```
"Sardines": {  -- Name of the product
  "price": 1.89, -- Price of the product
  "id": 3  -- The ID of the product. Used for promotions
}
```
	
## Setup
To run this project, run the following command in the root folder:
```
$ python main.py
```