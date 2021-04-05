'''HOME WORK:
1. WINDOW TO EDIT PERSONAL INFORMATION    ----- DONE!
2. 2 DECIMALS MAX                         ----- DONE!
'''

# Import modules
from tkinter import *
import os
from PIL import ImageTk, Image
import pyttsx3

# Sound engine
engine = pyttsx3.init()

# Functions

def finish_reg():
    name = temp_name.get()
    age = int(temp_age.get())
    gender= temp_gender.get()
    password = temp_password.get()

    # Fields completion validation
    if name == '' or age == '' or gender == '' or password == '':
        register_notif.config(fg='red', text='All fields must be filled...')
        engine.say('All fields must be filled...')
        engine.runAndWait()
        return

    # Name Validation
    all_accounts = os.listdir()

    # Verify if the user already exists.
    if name in all_accounts:
        register_notif.config(fg='red', text='Account already exists.')
        engine.say('Account already exists.')
        engine.runAndWait()
        return
    else:
        new_file = open(name, 'w') # Create a new file in writting mode
        new_file.write(name+'\n')
        new_file.write(password+'\n')
        new_file.write(str(age)+'\n')
        new_file.write(gender+'\n')
        new_file.write('0')
        new_file.close()
        register_notif.config(fg='green', text='Account created!')
        engine.say('Account created!')
        engine.runAndWait()

def user_register():
    # Globalize variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global register_notif

    # Variable
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    register_screen = Toplevel(master)
    register_screen.title('Register')

    # Labels
    Label(register_screen, text= 'Please, enter your information:', font=('Calibri', 12)).grid(row=0, padx=20, sticky='N', columnspan = 2)
    Label(register_screen, text= 'Name:', font=('Calibri', 12)).grid(row=1, sticky='N')
    Label(register_screen, text= 'Age:', font=('Calibri', 12)).grid(row=2, sticky='N')
    Label(register_screen, text= 'Gender:', font=('Calibri', 12)).grid(row=3, sticky='N')
    Label(register_screen, text= 'password:', font=('Calibri', 12)).grid(row=4, sticky='N')
    register_notif = Label(register_screen, font=('Calibri', 12))
    register_notif.grid(row=6, sticky='N', pady=10, columnspan = 2)

    # Entries
    Entry(register_screen, textvariable=temp_name).grid(row=1, column=1)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=1)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=1)
    Entry(register_screen, textvariable=temp_password, show='*').grid(row=4, column=1)

    # Buttons
    Button(register_screen, text='Register', font=('Calibri', 12), width=20, command=finish_reg).grid(row=5,pady=20, columnspan = 2)

def finish_edit_info():
    new_password = temp_password.get()
    new_age = temp_age.get()
    new_gender= temp_gender.get()

    # Fields completion validation
    if new_age == '' or new_gender == '' or new_password == '':
        edit_notif.config(fg='red', text='All fields must be filled...')
        engine.say('All fields must be filled...')
        engine.runAndWait()
        return
    
    # Get balance and age
    file = open(login_name, 'r') # Read mode
    file_data = file.read()
    file.close()
    details = file_data.split('\n')
    balance_ = details[4]
    age_ = details[2]

    if int(new_age) < int(age_) or int(new_age) <= 0:
        edit_notif.config(fg='red', text='Invalid age')
        return
    
    # Delete file
    os.remove(login_name)

    # Update the file
    new_file = open(login_name, 'w') # Create a new file in writting mode
    new_file.write(login_name+'\n')
    new_file.write(new_password+'\n')
    new_file.write(str(new_age)+'\n')
    new_file.write(new_gender+'\n')
    new_file.write(balance_)
    new_file.close()

    # Success
    edit_notif.config(fg='green', text='Info updated!')
    engine.say('Info updated!')
    engine.runAndWait()

def edit_info():
    # Globalize variables
    global temp_age
    global temp_gender
    global temp_password
    global edit_notif

    # Variable
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    edit_info_screen = Toplevel(master)
    edit_info_screen.title('Edit Information')

    # Labels
    Label(edit_info_screen, text= 'Please, enter your new information:', font=('Calibri', 12)).grid(row=0, padx=20, sticky='N', columnspan = 2)
    Label(edit_info_screen, text= 'Name:', font=('Calibri', 12)).grid(row=1, sticky='N')
    Label(edit_info_screen, text= 'Age:', font=('Calibri', 12)).grid(row=2, sticky='N')
    Label(edit_info_screen, text= 'Gender:', font=('Calibri', 12)).grid(row=3, sticky='N')
    Label(edit_info_screen, text= 'password:', font=('Calibri', 12)).grid(row=4, sticky='N')
    edit_notif = Label(edit_info_screen, font=('Calibri', 12))
    edit_notif.grid(row=6, sticky='N', pady=10, columnspan = 2)

    # Entries
    Entry(edit_info_screen, text=login_name, state='disabled').grid(row=1, column=1)
    Entry(edit_info_screen, textvariable=temp_age).grid(row=2, column=1)
    Entry(edit_info_screen, textvariable=temp_gender).grid(row=3, column=1)
    Entry(edit_info_screen, textvariable=temp_password, show='*').grid(row=4, column=1)

    # Buttons
    Button(edit_info_screen, text='Apply', font=('Calibri', 12), width=20, command=finish_edit_info).grid(row=5,pady=20, columnspan = 2)

def personal_details():
    file = open(login_name, 'r')
    file_data = file.read()
    file_data = file_data.split('\n')
    details_name = file_data[0]
    details_age = file_data[2]
    details_gender = file_data[3]
    details_balance = file_data[4]

    # PERSONAL DETAILS SCREEN
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Information')
    # Labels
    Label(personal_details_screen, text='Personal information and Balance', font=('Calibri', 14)).grid(row=0, pady=5)
    Label(personal_details_screen, text=f'Name: {details_name}', font=('Calibri', 12)).grid(row=1, pady=5)
    Label(personal_details_screen, text=f'Age: {details_age}', font=('Calibri', 12)).grid(row=2, pady=5)
    Label(personal_details_screen, text=f'Gender: {details_gender}', font=('Calibri', 12)).grid(row=3, pady=5)
    Label(personal_details_screen, text=f'Balance: ${float(details_balance):.2f}', font=('Calibri', 12)).grid(row=4, pady=5)

def deposit():
    # Global Variables
    global amount_deposit
    global deposit_notif
    global current_balance_label

    amount_deposit = StringVar()
    
    # Deposit windows
    deposit_window = Toplevel(master)
    deposit_window.title('Deposit')
    
    # Get current balance
    file = open(login_name, 'r')
    file_data = file.read()
    file_data = file_data.split('\n')
    current_balance = file_data[4]

    # Label
    Label(deposit_window, text='Deposit', font=('Calibri', 14)).grid(row=0, pady=5, columnspan=2, sticky='N')
    current_balance_label = Label(deposit_window, text=f'Current balance: {float(current_balance):.2f}')
    current_balance_label.grid(row=1, pady=5, columnspan=2, sticky='N')
    Label(deposit_window, text='Enter the amount to deposit: ').grid(row=2, pady=5)
    deposit_notif = Label(deposit_window, font=('Calibri', 12))
    deposit_notif.grid(row=3, columnspan=2, sticky='N')

    # Entry
    Entry(deposit_window, textvariable=amount_deposit, font=('Calibri', 12)).grid(row=2, column=1, pady=5, sticky='N')

    # Button
    Button(deposit_window, text='Deposit', font=('Calibri', 14), command=deposit_logic).grid(row=4, columnspan=2, sticky='N')
    
def deposit_logic():
    # Logic
    if amount_deposit.get() == '' or float(amount_deposit.get()) <= 0.0 :
        deposit_notif.config(fg='red', text='Amount not valid')
        return
    
    # Update the file
    # Copy data to memory
    file = open(login_name, 'r+') # Read and write mode
    file_data = file.read()
    # file.close()

    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = float(current_balance)
    updated_balance += float(amount_deposit.get())

    # New file
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate()
    file.write(file_data)
    file.close()
    # Source: https://stackoverflow.com/questions/13089234/replacing-text-in-a-file-with-python/13089373

    current_balance_label.config(fg='green', text=f'Current balance: {updated_balance:.2f}')
    deposit_notif.config(fg='green', text='Amount deposited! Thanks.')
        
def withdraw():
    # Global Variables
    global amount_withdraw
    global withdraw_notif
    global current_balance_label

    amount_withdraw = StringVar()
    
    # Deposit windows
    withdraw_window = Toplevel(master)
    withdraw_window.title('Withdraw')
    
    # Get current balance
    file = open(login_name, 'r')
    file_data = file.read()
    file_data = file_data.split('\n')
    current_balance = file_data[4]

    # Label
    Label(withdraw_window, text='Withdraw', font=('Calibri', 14)).grid(row=0, pady=5, columnspan=2, sticky='N')

    current_balance_label = Label(withdraw_window, text=f'Current balance: {float(current_balance):.2f}')
    current_balance_label.grid(row=1, pady=5, columnspan=2, sticky='N')

    Label(withdraw_window, text='Enter the amount to withdraw: ').grid(row=2, pady=5)

    withdraw_notif = Label(withdraw_window, font=('Calibri', 12))
    withdraw_notif.grid(row=3, columnspan=2, sticky='N')

    # Entry
    Entry(withdraw_window, textvariable=amount_withdraw, font=('Calibri', 12)).grid(row=2, column=1, pady=5, sticky='N')

    # Button
    Button(withdraw_window, text='Withdraw', font=('Calibri', 14), command=withdraw_logic).grid(row=4, columnspan=2, sticky='N')
    
def withdraw_logic():

    # Logic
    if amount_withdraw.get() == '' or float(amount_withdraw.get()) <= 0.0 :
        withdraw_notif.config(fg='red', text='Amount not valid')
        return

    file = open(login_name, 'r+') # Read and write mode
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    
    if float(current_balance) < float(amount_withdraw.get()):
        withdraw_notif.config(fg='red', text='Insufficient balance.')
        return
    
    # Update the file
    # Copy data to memory
    file = open(login_name, 'r+') # Read and write mode
    file_data = file.read()
    # file.close()

    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = float(current_balance)
    updated_balance -= float(amount_withdraw.get())

    # New file
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate()
    file.write(file_data)
    file.close()

    current_balance_label.config(fg='green', text=f'Current balance: {updated_balance:.2f}')
    withdraw_notif.config(fg='green', text='Amount withdrawed! Thanks.')

def login_session():
    # Global variables
    global login_name

    login_name = temp_login_username.get()
    login_password = temp_login_password.get()

    # Obtain name of files
    all_accounts = os.listdir()

    # Verify if the user already exists.
    if login_name in all_accounts:
        file = open(login_name, 'r')
        file_data = file.read()
        file_data = file_data.split('\n')
        password = file_data[1]

        # ACCOUNT DASHBOARD
        if login_password == password:
            # Destroy login screen
            login_screen.destroy()

            #DASHBOARD SCREEN
            dashboard_screen = Toplevel(master)
            dashboard_screen.title('Dashboard')

            # Labels
            Label(dashboard_screen, text='Dashboard Account', font=('Calibri', 14)).grid(row=0, pady=10)
            Label(dashboard_screen, text=f'Welcome back {login_name.capitalize()}!', font=('Calibri', 12)).grid(row=1, pady=5)

            # Buttons
            Button(dashboard_screen, text='Personal info', command=personal_details, font=('Calibri', 12)).grid(row=2,sticky='N')
            Button(dashboard_screen, text='Deposit', command=deposit, font=('Calibri', 12)).grid(row=3,sticky='N')
            Button(dashboard_screen, text='Withdraw', command=withdraw, font=('Calibri', 12)).grid(row=4,sticky='N')
            Button(dashboard_screen, text='Edit Info', command=edit_info, font=('Calibri', 12)).grid(row=5,sticky='N')

        else:
            login_notif.config(fg='red', text='Wrong password.')
    else:
        login_notif.config(fg='red', text='Account not found.')


    print('Login button')

def login():
    # Global variables
    global temp_login_username
    global temp_login_password
    global login_notif
    global login_screen

    temp_login_username = StringVar()
    temp_login_password = StringVar()

    # Create login screen
    login_screen = Toplevel(master)
    login_screen.title('Login')

    # Labels
    Label(login_screen, text='Enter your login information', font=('Calibri', 12)).grid(row=0, columnspan=2)
    Label(login_screen, text='Username:', font=('Calibri', 12)).grid(row=1,sticky='W')
    Label(login_screen, text='Password:', font=('Calibri', 12)).grid(row=2,sticky='W')
    login_notif = Label(login_screen, font=('Calibri', 12))
    login_notif.grid(row=6, sticky='N', pady=10, columnspan = 2)
    # Button
    Button(login_screen, text='Login', font=('Calibri', 12), command=login_session).grid(row=3,pady=5, columnspan=2)

    # Entries
    Entry(login_screen, textvariable=temp_login_username).grid(row=1, column=1)
    Entry(login_screen, textvariable=temp_login_password, show='*').grid(row=2, column=1)

# Main screen
master = Tk()
master.title('Banking App')

# Import and add logo image
img = Image.open('logo.png') # https://www.cleanpng.com/png-bank-vault-safe-deposit-box-clip-art-bank-safe-pas-248623/download-png.html
img = img.resize((250,250))
img = ImageTk.PhotoImage(img)

# Labels
Label(master, text='Banking App v0.1', font=('Calibri',14)).grid(row=0, sticky=N, pady=10)
Label(master, text='Add description here', font=('Calibri',10)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N, padx=0, pady=5)
master.resizable(0, 0) # https://www.geeksforgeeks.org/resizable-method-in-tkinter-python/

# Buttons
Button(master, text='Registration', font=('Calibri', 12), width=20, command=user_register).grid(row=3, sticky=N)
Button(master, text='Login', font=('Calibri', 12), width=20, command=login).grid(row=4, sticky=N, pady=10)





master.mainloop()