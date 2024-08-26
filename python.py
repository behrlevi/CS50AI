class Ticket:
    def __init__(self, ticket_id, description, status):
        self.ticket_id = ticket_id
        self.description = description
        self.status = status

class TicketingSystem:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, ticket_id, description):
        ticket = Ticket(ticket_id, description, "Open")
        self.tickets.append(ticket)

    def close_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.status = "Closed"
                break

    def get_open_tickets(self):
        open_tickets = []
        for ticket in self.tickets:
            if ticket.status == "Open":
                open_tickets.append(ticket)
        return open_tickets

# Example usage
ticketing_system = TicketingSystem()
ticketing_system.create_ticket(1, "Fix bug in login page")
ticketing_system.create_ticket(2, "Update user profile page")
ticketing_system.close_ticket(1)

open_tickets = ticketing_system.get_open_tickets()
for ticket in open_tickets:
    print(f"Ticket ID: {ticket.ticket_id}, Description: {ticket.description}, Status: {ticket.status}")