import json
import os
try:
   def create_product():
      filename=input('enter the file name')
      lists_product=[]
      total=int(input('enter the total numbers of products'))
      for product in range(total):
           product_data={'pro_name':input("enteer the product name "),
                        'pro_quantity':int(input("enteer the product quantity ")),
                         'pro_price':float(input("enteer the product price "))}
           lists_product.append(product_data)
      with open(f'{filename}.json','w') as file:
         json.dump(lists_product,file,indent=4)    
         print('product is created succesfully')
   def add_prodacut():
      filename=input('eter the file name')
      files=filename+'.json'
      lists_product=[]
      total=int(input('enter the total numbers of products'))
      for product in range(total):
           product_data={'pro_name':input("enteer the product name "),
                        'pro_quantity':int(input("enteer the product quantity ")),
                         'pro_price':float(input("enteer the product price "))}
           lists_product.append(product_data)  
      productData=lists_product         
      if os.path.exists(files) and os.path.getsize(files)>0:
         with open(f'{files}','r') as file:
           existing_pro= json.load(file)
      else:
         existing_pro=[]
      if isinstance(existing_pro,list):
         existing_pro.extend(productData)  
      else:
         existing_pro=[existing_pro,productData]    
      with open(f'{files}','w') as file:
         json.dump(existing_pro,file,indent=4)
      print('product is added sucessfully')     
              
   def veiws_prodacts():
      
      with open('gogle.json','r') as file:
         content=json.load(file)
      for product in content:
         print(f'-{product}')   
   def parches_products():
      product_name=input('welcome to my shop enter the products name you want to parchase:')
      with open('gogle.json','r') as file:
        content=json.load(file)
      for product in content:
        if product['pro_name'].lower()==product_name.lower():   
           quantity=int(input('enter the quantity'))
           if quantity<=product['pro_quantity']:
              prices=float(input('enter the price'))
              total_price=prices*quantity
              if total_price<=product['pro_price']:
                 remain_quantity=product['pro_quantity']-quantity
                 remain_price=product['pro_price']-total_price
                 print(f'purchased sucefully you bought {quantity} by {total_price}')
                 with open('gogle.json','w') as file:
                   json.dump(content,file,indent=4)
      
              else:
                 print('insuficient price')
           else:
              print('insufficient quantity')   
        else:
           print('there is no such product')   
   def delete_file():
      
         file_name=input('enter file name to delete')
         filename=file_name+'json'
         if os.path.exists(filename):
            os.remove(f'{filename}')
            print(f'file name {filename} is deleted succesfully')
         print('not such file')
   while True:
     print('1 to create product')
     print('2 to add product')
     print('3 to view product')
     print('4 to parchase')
     print('5 to delete file ')
     print('6 to exite')
     choice=int(input("enter choice(1--4)"))
     match choice:
        case 1:
            create_product()
        case 2:
            add_prodacut()
        case 3:
            veiws_prodacts()
        case 4:
            parches_products()

        case 5:
            delete_file()            
        case 6:
            print('Goodbye have a nice time')
            break
        case _:   
            print('incorrect input')

except json.JSONDecodeError:
   print("code your file correctly")              
except FileNotFoundError:
   print("there is no such file")
except Exception as e:
   print('unexpected error')        

