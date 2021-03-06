from medreminder import Medication
import cPickle as pickle

def menu():
	print """Please select an option:
	Main Menu
1 - Show all medications currently in the system
2 - Add a new medication to the protocol
3 - Change the information associated with a medication in the protocol
4 - Delete a medication from the protocol
5 - Exit 
	"""

def write_to_pkl(med_list):
	pkl_file = open("mymeds.pkl", "wb")
	pickle.dump(med_list, pkl_file)
	pkl_file.close()

def read_from_pkl():
	with open("mymeds.pkl", "rb") as pkl_file:
		return pickle.load(pkl_file)

med_list = read_from_pkl()

def check_med(med_name):
	for item in med_list:
		if item.med_name == med_name:
			return True
	return False

def show_meds():
	print "Your current medications are:"
	med_list = read_from_pkl()
	for item in med_list:
		print item.med_name

def change_info():
	show_meds()
	change = raw_input("Which medication would you like to change the information for? ").lower()
	if check_med(change):
		print "Your current info for this medication is:"
		for i in range(len(med_list)):
			if med_list[i].med_name == change:
				print "Medication name: " + med_list[i].med_name
				print "Days between orders: " + med_list[i].days_between_orders
				print "Shipping time for orders in days" + med_list[i].days_remind_before
				print "Dose (if specified): " + med_list[i].dose
		change_part = raw_input("""what part of this medication's information would you like to change?
Please enter 'name,' 'days between orders,' 'shipping days,' 'dose,' or 'exit' if you have decided not to change the listing.""").lower()
		if change_part == "name" or change_part == "name,":
			new_name = raw_input("What would you like the medication's new name to be? ")
			for i in range(len(med_list)):
				if med_list[i].med_name == change:
					med_list[i].med_name = new_name
			print "Your medication name has been changed"
		elif change_part == "days between orders" or change_part == "days between orders,":
			new_days = raw_input("What would you like to set as the number of days one shipment of this medication will last for? ")
			for i in range(len(med_list)):
				if med_list[i].med_name == change:
					med_list[i].days_between_orders = new_days
			print "The time one shipment of your medication covers has been changed."
		elif change_part == "shipping days" or change_part == "shipping days,":
			new_shipping = raw_input("What would you like to set as the new shipping time for this medication's orders? ")
			for i in range(len(med_list)):
				if med_list[i].med_name == change:
					med_list[i].days_remind_before = new_shipping
			print "Your shipping time for this medication has been changed." 
		elif change_part == "dose" or change_part == "dose,":
			new_dose = raw_input("What would you like to set as the new dose for this medication? ")
			for i in range(len(med_list)):
				if med_list[i].med_name == change:
					med_list[i].dose = new_dose
			print "Your medication dose has been changed."
		elif change_part == "exit":
			return
		write_to_pkl(med_list)
	else:
		print """That medication is not on your list of medications. Please make sure you 
are spelling the medication correctly."""

def add_new():
	new_med = raw_input("What is the name of the medication you would like to add? ").lower()
	if check_med(new_med):
		print "That medication is already on the list."
	else:
		new_days = raw_input("What would you like to set as the number of days one shipment of this medication will last for? ")
		new_shipping = raw_input("What would you like to set as the shipping time for this medication's orders? ")
		new_dose = raw_input("What would you like to set as the dose for this medication? You may leave this field blank. ")
		new_email = raw_input("What would you like to set as the email to receive messages about this medication at? You may leave this field blank. ")
		new_med_info = Medication(new_med, new_days, new_shipping, dose = new_dose, email = new_email)
		med_list.append(new_med_info)
		write_to_pkl(med_list)
	
def delete():
	show_meds()
	delete = raw_input("""Which medication would you like to remove (please type exit if you have decided 
to not delete a medication)? """).lower()
	if check_med(delete):
		for i in range(len(med_list)):
			if med_list[i].med_name == delete:
				med_list.remove(med_list[i])
				break
		print "Your medication has been deleted." 
		write_to_pkl(med_list)
	elif delete == "exit":
		return
	else:
		print """That medication is not on your list of medications. 
Please make sure you are spelling the medication correctly."""


def main():
	menu()
	while(True):
		choice = int(raw_input("Please choose any of the above menu items or enter 0 to see the main menu again: "))
		if choice == 5:
			break
		elif choice == 0:
			menu()
		elif choice == 1:
			show_meds()
		elif choice == 2:
			add_new()
		elif choice == 3:
			change_info()
		elif choice == 4:
			delete()
		else:
			print "Please enter a valid input. "

if __name__ == '__main__':
	main()