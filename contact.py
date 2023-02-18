''' from pymongo import MongoClient

connection_uri = 'mongodb+srv://<username>:<password>@<cluster-url>/<database-name>?retryWrites=true&w=majority'
client = MongoClient(connection_uri)
db = client['<database-name>']
 '''


names=[]
phone_numbers=[]
num=int (input("enter number you want to save: "))
for i in range(num):
    name=input("name")
    phone_number=input("phone numbers")
    names.append(name)
    phone_numbers.append(phone_number)
    print("\nName\t\t\tPhone number\n")
    for i in range(num):
        print("{}\t\t\t{}".format(names[i],phone_numbers[i]))
        search_term=input("\nSearch..........: ")
        print("search result")
        if search_term in names:
            index=names.index(search_term)
            phone_number=phone_numbers[index]
            print(("name: {},phone number:{}".format(search_term,phone_number)))
        else:
            print("name not found")
        

