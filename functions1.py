
def mean(value):
    if type(value) == dict:
        client_permonth = sum(value.values()) / len(value)
    else:
        client_permonth = sum(value) / len(value)
    return client_permonth

client_permonth = {"March": 3, "April": 4, "May": 6, "June": 3}
print(mean(client_permonth))