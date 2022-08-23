def speeding(speed, birthday):
    limit = 60
    if birthday:
        limit += 5

    if speed <= limit:
        message = "No Ticket"
    elif speed <= limit+20:
        message = "Small Ticket"
    else:
        message = "Big Ticket"

    return message
