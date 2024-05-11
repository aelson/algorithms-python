from tech.aelson.algorithms.search.search_smallest import SearchSmallest
from tech.aelson.algorithms.model.product import Product

if __name__ == "__main__":
    products = [
        Product("Tesla Model 3", 50000),
        Product("Toyota Corolla", 20000),
        Product("Ford Escape", 30000),
        Product("Honda Civic", 30000),
        Product("Audi Q5", 45000)
    ]

    smallest = SearchSmallest.execute(products, 0, 4)
    print(smallest)
    print("The car", products[smallest].get_name(), "costs", products[smallest].get_price())
