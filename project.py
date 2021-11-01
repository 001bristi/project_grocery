print("      Hello Friends! ")
print("   What Item do you want to buy???????")
print("   You may Check our Product_List")
product=["Soap","Shampoo","Biscuit","Chips"]
catagory=(

{
  "Dettol":206,
  "Pears":192,
  "Dove":312,
  },
{"Dove":390,
  "Loreal":424,
  "Tresemme":325,
  "kesh_king":135,
  },
{"Little heart":13,
  "Parle g gold":100,
  "Horlicks":90,
  "Britannia":30,
  "Hide & Seek":50,
  "Jim jam":32,

},{"Lays":40,
  "Kurkure":45,
  "jolochip":199,
  "maxx":10
})
cart=[]
price=[]
while(1):
  x=input("Any Item do you want to buy? Press- yes /  Press- no to exit")
  if x=="no":
    #print("     Thank You   ")
    break
  if x=="yes":
    print("Available products are :")
    for i in product:
      print(i)
    p=input("What product do you want?")
    indx=product.index(p)
    for i,j in catagory[indx].items():
      print(i,":",j)
    item=input("Which type do you want?")
    qnty=int(input("How many product??"))
    cart.append(item)
    price.append(catagory[indx][item]*qnty)
#if x=="yes":
print(cart,price)

total=sum(price)
print("The Total Price is :" ,total)
print("""Go to Cart and Checkout....
      Thank You For Shopping With Us!""")
