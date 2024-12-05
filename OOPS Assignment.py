#!/usr/bin/env python
# coding: utf-8

# ###Problem 1: Bank Account Create a class representing a bank account with attributes like account number,
# account holder name, and balance. Implement methods to deposit and withdraw money from the account.

# In[15]:


class bankaccount:
    
    def __init__(self, acc_num, acc_name, initial_balance=0):
        self.acc_num = acc_num
        self.acc_name = acc_name
        self.balance = initial_balance
        
    def deposit(self,amount):
        
        if amount > 0:
            self.balance += amount
            
            print(f"Deposited Amount {amount}. New Balance {self.balance}")
            
        else:
            
            print("Invalid Amount")
            
    def withdraw(self, amount):
        
        if 0 < amount < self.balance:
            
            self.balance -= amount
            
            print(f"Withdrawal Amount {amount}. New Balance {self.balance}")
        
        else:
            
            print("Insufficient funds. Available Balance {self.balance}")
            
priyesh = bankaccount(123,'Priyesh',500)

priyesh.deposit(200)

priyesh.withdraw(100)
        


# Problem 2: Employee Management Create a class representing an employee with attributes like employee ID, name, and salary. Implement methods to calculate the yearly bonus and display employee details.

# In[18]:


class employee:
    
    def __init__(self, employee_ID, employee_name, salary):
        self.employee_ID = employee_ID
        self.employee_name = employee_name
        self.salary = salary
        
    def bonus(self, bonus_percentage):
        if bonus_percentage > 0:
            bonus = self.salary * bonus_percentage
            print(f"Employee's Bonus {bonus}")
            
        else:
            print("Invalid Bonus Percentage")
            
    def employee_details(self):
        print(f"Employee_Name = {self.employee_name}, Employee_ID = {self.employee_ID}, Employee_Salary = {self.salary}")
        
Pooja = employee(123,'Pooja',150)
Pooja.bonus(0.10)
Pooja.employee_details()


# Problem 3: Vehicle Rental Create a class representing a vehicle rental system. Implement methods to rent a vehicle, return a vehicle, and display available vehicles.

# In[58]:


class vehicle:
    
    def __init__(self, vehicle_id, vehicle_type, is_available = True):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.is_available = is_available
    
class rental_system:
    
    def __init__(self):
        self.vehicles = []
        
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        
    def rent_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id and vehicle.is_available:
                vehicle.is_available = False
                print("Vehicle Rented Successfully")
                return
            else:
                (f"{vehicle_id} vehicle is not available")
                
    def return_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id and not vehicle.is_available:
                vehicle.is_availble = True
                print("Vehicle Returned Successfully")
                return
            else:
                print(f"Vehicle {vehicle_id} not found or already available.")
                
    def display_available(self):
        print("Available Vehicles: ")
        for vehicle in self.vehicles:
            if vehicle.is_available:
                print(f"Vehicle_ID = {vehicle.vehicle_id} and Vehicle_Type = {vehicle.vehicle_type}")
                
Enterprise = rental_system()

Enterprise.add_vehicle(vehicle("V001", "Car"))
Enterprise.add_vehicle(vehicle("V002", "Truck"))
Enterprise.add_vehicle(vehicle("V003", "Motorcycle"))

Enterprise.display_available()
Enterprise.rent_vehicle('V001')
Enterprise.display_available()
Enterprise.return_vehicle('V001')


# Problem 4: Library Catalog Create classes representing a library and a book. Implement methods to add books to the library, borrow books, and display available books.

# In[8]:


class book_details:
    
    def __init__(self,book_id,book_type,is_available = True):
        self.book_id = book_id
        self.book_type = book_type
        self.is_available = is_available
        
class library_system:
    
    def __init__(self):
        self.books = []
    
    def add_books(self, book_details):
        self.books.append(book_details)
        
    def borrow_books(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.is_available:
                book.is_available = False
                print(f"Book_ID = {book_id} is borrowed")
                return 
            else:
                print(f"Book_ID = {book_id} is not available in library")
                
    def return_books(self, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.is_available:
                book.is_available = True
                print(f"Book_ID = {book_id} is returned")
                return   
            else:
                print(f"Book_ID = {book_id} is not available in library")
                
    def display_books(self):
        print("Available Books: ")
        for book in self.books:
            if book.is_available:
                print(f"Book_ID = {book.book_id} and Book_Type = {book.book_type}")

dallas_lib = library_system()

dallas_lib.add_books(book_details("1", "Book1"))
dallas_lib.add_books(book_details("2", "Book2"))
dallas_lib.add_books(book_details("3", "Book3"))


dallas_lib.display_books()
dallas_lib.borrow_books('1')
dallas_lib.display_books()
dallas_lib.return_books('1')
dallas_lib.display_books()
                


# Problem 5: Product Inventory Create classes representing a product and an inventory system. Implement methods to add products to the inventory, update product quantity, and display available products.

# In[12]:


class product:
    def __init__(self, sku_id, sku_name, quantity=0, is_available = True):
        self.sku_id = sku_id
        self.sku_name = sku_name
        self.quantity = int(quantity)
        self.is_available = is_available
        
class inventory_system:
    
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        
    def add_quantity(self, sku_id, quantity):
        for product in self.products:
            if product.sku_id == sku_id and product.is_available:
                product.quantity = product.quantity + quantity
                print(f"{product.sku_id} quantity is updated to {product.quantity}")
                return
            else:
                print(f"Such Product is not available or quantity is not valid")
                
    def display_products(self):
        print("Available Products: ")
        for product in self.products:
            if product.is_available:
                print(f"SKU = {product.sku_id}, SKU_Name: {product.sku_name}, Quantity: {product.quantity}")
                
storeA = inventory_system()

storeA.add_product(product("1", "TV",5))
storeA.add_product(product("2", "Mobile",3))
storeA.add_product(product("3", "Cable",10))

storeA.display_products()
storeA.add_quantity('1',10)
storeA.display_products()
        


# Problem 6: Shape Calculation Create a class representing a shape with attributes like length, width, and height. Implement methods to calculate the area and perimeter of the shape.

# In[22]:


class shape_calculate:
    
    def __init__(self, length, width, height=None):
        self.length = length
        self.width = width
        self.height = height
        
    def area(self):
        if self.height:
            return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
        else:
            return self.length * self.width
            
    def perimeter(self):
        if self.height:
            return None
        else:
            return 2 * (self.length + self.width)            

shape_2D = shape_calculate(3,4)
print(f"Perimeter of 2D Shape is {shape_2D.perimeter()}")
print(f"Area of 2D Shape is {shape_2D.area()}")

shape_3D = shape_calculate(3,4,5)
print(f"Perimeter of 3D Shape is {shape_3D.perimeter()}")
print(f"Area of 3D Shape is {shape_3D.area()}")


# Problem 7: Student Management Create a class representing a student with attributes like student ID, name, and grades. Implement methods to calculate the average grade and display student details.

# In[24]:


class student_management:
    
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades
        
    def average_grade(self):
        if not self.grades:
            return None
        else:
            return sum(self.grades) / len(self.grades)
    
    def student_details(self):
        
        average_grade = self.average_grade()
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Grades: {', '.join(map(str, self.grades))}")
        
        if average_grade is not None:
            print(f"Average Grade: {average_grade}")
        else:
            print(f"Students Grades is not available")
        
student = student_management("S001", "Alice Johnson", [85, 92, 78, 88])
student.student_details()            
    


# Problem 8: Email Management Create a class representing an email with attributes like sender, recipient, and subject. Implement methods to send an email and display email details.

# In[26]:


class email_tool:
    
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        
    def send_email(self):
        
        print(f"sending email.....\nFrom: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\nBody: {self.body}")
        print("Email Sent Successfully")
        
    def email_details(self):
        
        print("Email Details:")
        print(f"From: {self.sender}")
        print(f"To: {self.recipient}")
        print(f"Subject: {self.subject}")
        print(f"Body:\n{self.body}")
        
email = email_tool(
    sender="alice@example.com",
    recipient="bob@example.com",
    subject="Meeting Reminder",
    body="Hi Bob,\n\nJust a reminder about our meeting tomorrow at 10 AM.\n\nBest regards,\nAlice"
)

email.email_details()

email.send_email()


# Problem 9: Social Media Profile Create a class representing a social media profile with attributes like username and posts. Implement methods to add posts, display posts, and search for posts by keyword.

# In[30]:


class social_media:
    
    def __init__(self, username, posts):
        self.username = username
        self.posts = posts
    
    def add_post(self, post):
        self.posts.append(post)
        print(f"Post Added Successfully")
        
    def display_posts(self):
        print(f"posts from {self.username}: {self.posts}")
        return
        
    def search_posts(self, keyword):
        for post in self.posts:
            if keyword not in post:
                pass
            else:
                print(f"Similar to post to this keyword is {post}")
                
                
priyesh = social_media('Priyesh', ['About SEO and AI', 'Personal branding'])

priyesh.add_post('data analytics')
priyesh.display_posts()
priyesh.search_posts('analytics')


# Problem 10: ToDo List Create a class representing a ToDo list with attributes like tasks and due dates. Implement methods to add tasks, mark tasks as completed, and display pending tasks.

# In[51]:


class tasks:
    
    def __init__(self, tasks, due_dates, status):
        self.tasks = tasks
        self.due_dates = due_dates
        self.status = status

class todo_list:
    
    def __init__(self):
        self.tasks = []
        
    def add_tasks(self, task):
        self.tasks.append(task)
        
    def update_status(self, task_name, status):
        for task in self.tasks:
            if task.tasks == task_name and task.status == 'pending':
                task.status = status
                print(f"{task.tasks} status changed to {status}")
                return
            
    def pending_tasks(self):
        print("Pending Tasks: ")
        for task in self.tasks:
            if task.status == 'pending':
                print(f"task: {task.tasks}, due_date: {task.due_dates}, status: {task.status}")
                

My_List = todo_list()

My_List.add_tasks(tasks('laundry','10/05','pending'))
My_List.add_tasks(tasks('vacuum','11/05','pending'))  
My_List.add_tasks(tasks('cooking','12/05','pending'))

My_List.update_status('vacuum','completed')
My_List.pending_tasks()
            
        
        

