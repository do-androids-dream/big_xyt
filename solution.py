import json


class ExchangeStock:
    id = 0

    def __init__(self):
        ExchangeStock.id += 1
        self.id = ExchangeStock.id
        self.order_list = []
        with open(f"orders{self.id}.json", "w") as file:
            json.dump(self.order_list, file)

    def add_order(self, order: dict):
        """
        assuming that task required to operate with only provided list of orders
        there is no need for orders data validation
        """
        with open(f"orders{self.id}.json") as file:
            self.order_list = json.load(file)

        if order["type"] == "Add":
            self.order_list.append(order)
            print(f"order {order} has been added")
        else:
            for i in range(len(self.order_list)):
                if self.order_list[i]["id"] == order["id"]:
                    print(f"order {self.order_list.pop(i)} has been removed")
                    break

        with open(f"orders{self.id}.json", "w") as file:
            json.dump(self.order_list, file, indent=4)

        self.show_best_sum()

    def show_best_sum(self):
        best_buy = [0]
        best_sell = [0]
        for ex_order in self.order_list:
            if ex_order["order"] == "Buy":
                best_buy.append(ex_order["price"] * ex_order["quantity"])
            else:
                best_sell.append(ex_order["price"] * ex_order["quantity"])
        print(f"best buy sum: {max(best_buy)}\nbest sell sum: {max(best_sell)}\n")


ORDERS = [
    {
          "id": 1,
          "order": "Buy",
          "type": "Add",
          "price": 20.0,
          "quantity": 100
    },
    {
          "id": 2,
          "order": "Sell",
          "type": "Add",
          "price": 22.0,
          "quantity": 200
    },
    {
          "id": 3,
          "order": "Buy",
          "type": "Add",
          "price": 23.0,
          "quantity": 50
    },
    {
          "id": 4,
          "order": "Buy",
          "type": "Add",
          "price": 23.0,
          "quantity": 70
    },
    {
          "id": 3,
          "order": "Buy",
          "type": "Remove",
          "price": 23.0,
          "quantity": 50
    },
    {
          "id": 5,
          "order": "Sell",
          "type": "Add",
          "price": 28.0,
          "quantity": 100
    }
]


store_obj_1 = ExchangeStock()
for order in ORDERS:
    store_obj_1.add_order(order)

print(store_obj_1.order_list)
