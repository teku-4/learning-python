import json
#cretes products file
def create_product_file(products):
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)  # Added indent for better readability
        print(f"File of products: {products} created successfully.")

#adding products data
def adds_products_data(products):
    with open("products.json", "a") as file:
        json.dump(products, file, indent=4)  
        print(f"Products {products} added successfully.")

#displays products data        

def display_product_data():
    try:
        with open("products.json", "r") as file:
            if file.read(1)=="":
                print("this file is empty")
                return
            #resets to the starts of file
            file.seek(0) 
            products = json.load(file)
            print("The products are listed:")
            print(json.dumps(products, indent=4))  # Pretty print the JSON data
    except FileNotFoundError:
        print("There is no such file.")
    except json.JSONDecodeError:
        print("This raise an error as JSON file is not correct.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:   
        print("press 1: to create pruducts file")
        print("press 2: to add pruducts file")
        print("press 3: to display pruducts file")
        print("press 0: to exits the program")
        option=int(input("enter your option from the above main menu"))
        match option:
            case 1:
                product_total_quantity = int(input("Enter the total products quantity you want to store: "))   
                lists_of_products = []
                
                for _ in range(product_total_quantity):
                    product_data = {
                        "product_id": int(input("Enter the product's ID: ")),
                        "product_name": input("Enter the product's name: "),
                        "product_price": float(input("Enter the price of the product: ")),
                        "product_quantity": int(input("Enter the quantity of products: "))
                    }
                    lists_of_products.append(product_data) 

                create_product_file(lists_of_products)
            case 2:


                total_quantity = int(input("Enter the total number of products you want to add: "))
                lists_added_product = []
                
                for _ in range(total_quantity):
                    added_products = {
                        "product_id": int(input("Enter the product ID: ")),
                        "product_name": input("Enter the product name: "),
                        "product_quantity": int(input("Enter the products quantity: ")),                  
                        "product_price": float(input("Enter the product price: "))
                    }
                    lists_added_product.append(added_products)
                adds_products_data(lists_added_product)     
            case 3:

                display_product_data()   
            case 0:
                print("Goodby have a nice time")
                break
            case _:
                print("invlid input please enter the valid input")    
# if __name__ == "__main__":
main()
