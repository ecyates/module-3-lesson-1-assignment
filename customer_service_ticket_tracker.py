# Task 1: Customer Service Ticket Tracker
# Demonstrate your ability to use nested collections and 
# loops by creating a system to track customer service tickets.

# Develop a program that:
# - Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).

# Implement functions to:
# - Open a new service ticket.
# - Update the status of an existing ticket.
# - Display all tickets or filter by status.

# Initialize with some sample tickets and include functionality for additional ticket entry.

# Initial Service Tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "Open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "Closed"}
}

def open_ticket(uniqueID, name, issue, status="Open"):
    '''This function takes adds a new ticket to the service tickets list. It takes the unique ID, name, and issue description 
and will default the status to "Open" but it can also be given.'''
    try:
        # Raise an error if given an invalid status
        if status != "Open" and status != "Closed": 
            raise ValueError()
        # Check that the unique ID is not already in the list
        if uniqueID not in service_tickets:
            # Add the ticket to the list and alert user.
            service_tickets[uniqueID] = {"Customer": name, "Issue": issue, "Status": status}
            print(f"The following customer has been added with ticket# {uniqueID}: \nCustomer: {name}\nIssue: {issue}\nStatus: {status}")
        else: 
            print(f"Looks like the ticket#{uniqueID} already exists, try again!")
    except ValueError:
        print("Please input a valid status (Open/Closed).")

def update_status(uniqueID, status="Closed"):
    '''This function updates the status of a ticket. The default is to update the status to Closed, but the 
    user can also change it from "Closed" to "Open".'''
    try: 
        # Raise error if the unique ID is not in the list
        if uniqueID not in service_tickets:
            raise KeyError()
        # Raise error if the status is not one of the options.
        elif status != "Open" and status != "Closed":
            raise ValueError()
        # If the status is already the status for the ticket, alert the user. 
        elif service_tickets[uniqueID]["Status"] == status:
            print(f"The status for {uniqueID} was already {status}. No change was made.")
        # Else, update the status
        else:
            service_tickets[uniqueID]["Status"] = status
            print(f"The status for {uniqueID} was updated to {status}.")
    except KeyError:
        print(f"The ticket# {uniqueID} does not exists. Please try again.")
    except ValueError:
        print(f"Please input a valid status (Open/Closed).")

def display_tickets(status_filter="None"):
    '''This function displays the tickets given the status filter: 
    "None" = displays all the tickets
    "Open" = displays the open tickets
    "Closed" = displays the closed tickets'''
    try: 
        # Raise error if the status filter is not one of the options
        if status_filter != "Open" and status_filter!= "Closed" and status_filter != "None":
            raise ValueError()
        else:
            # Iterate over the tickets
            for uniqueID, data in service_tickets.items():
                # Check that the status is not being filtered out
                if status_filter == "None" or status_filter == service_tickets[uniqueID]["Status"]:
                    # Display the ticket information
                    print(f"\n{uniqueID}:")
                    for d in data.items():
                        print(f"{d[0]}: {d[1]}")
    except ValueError:
        print(f"Please input a valid status filter (None/Open/Closed).")


print("Checking Open Ticket Function:\n1) Check the default parameter")
open_ticket("Ticket003", "Mary", "Login problem")
print("\n2) Check a normal entry.")
open_ticket("Ticket004", "Chris", "Payment issue", "Closed")
print("\n3) Check a non-unique ID")
open_ticket("Ticket002", "David", "Shipment problem", "Open")
print("\n4) Check an invalid status input.")
open_ticket("Ticket006", "Unknown", "Unknown", "None")

print("\nChecking Update Status Function:\n1) Check a normal entry")
update_status("Ticket002", "Open")
print("\n2) Check when the status is already closed.")
update_status("Ticket004", "Closed")
print("\n3) Check when the ticket is not in the list")
update_status("Ticket006", "Open")
print("\n4) Check an invalid status")
update_status("Ticket002", "Nope")

print("\nChecking Display Tickets Function:\n1) Check the default parameter")
display_tickets()
print("\n2) Check status filter = Open")
display_tickets("Open")
print("\n3) Check status filter = Closed")
display_tickets("Closed")
print("\n4) Check status filter = None")
display_tickets("None")
print("\n5) Check an invalid status")
display_tickets("Nope")