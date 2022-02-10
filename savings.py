annual_savings = 6000
interest = 0.05

def calculate_savings(number_of_years):
    total = 0
    history = []
    for year in range(number_of_years):
        print(year)
        total = total + annual_savings
        total = total + total*interest
        history.append(total)
        print(total)
    return history

if __name__ == "__main__":
    print(calculate_savings(3))