# Simple Input Processing Output for hourly pay
def calculate_gross_pay(hourly_rate, hours_worked):
    return hourly_rate * hours_worked
    

# # tax calculation
# if grossPayPerAnnum <= 15600:
#     # 10.5% tax rate (10.5/100) 
#     tax = grossPayPerAnnum * 0.105
# elif grossPayPerAnnum <= 53500:
#     # first slab tax
#     firstSlabTax = 15600 * 0.105
#     # second with 17.5%
#     secondSlabTax = (grossPayPerAnnum - 15600) * 0.175
#     tax = firstSlabTax + secondSlabTax
# elif grossPayPerAnnum <= 78100:
    
#     # first slab
#     firstSlabTax = 15600 * 0.105
#     # second slab with 17.5% rate...
#     secondSlabTax = (53500 - 15600) * 0.175
#     # 3rd with 30%
#     thirdSlabTax = (grossPayPerAnnum - 53500) * 0.30
#     tax = firstSlabTax + secondSlabTax + thirdSlabTax
# elif grossPayPerAnnum <= 180000:
#     # 1st (10.5)
#     firstSlabTax = 15600 * 0.105
#     # 2nd (17.5)
#     secondSlabTax = (53500 - 15600) * 0.175
#     # 3rd (30%)
#     thirdSlabTax = (78100 - 53500) * 0.30
#     # 4th (33%)
#     fourthSlabTax = (grossPayPerAnnum - 78100) * 0.33
#     tax = firstSlabTax + secondSlabTax + thirdSlabTax + fourthSlabTax
# else:
#     # 1st (10-.5)
#     firstSlabTax = 15600 * 0.105
#     # 2nd (17.5)
#     secondSlabTax = (53500 - 15600) * 0.175
#     # 3rd (30)
#     thirdSlabTax = (78100 - 53500) * 0.30
#     # 4th (33%)
#     fourthSlabTax = (180000 - 78100) * 0.33
#     # 5th (39%)
#     fifthSlabTax = (grossPayPerAnnum - 180000) * 0.39
#     tax = firstSlabTax + secondSlabTax + thirdSlabTax + fourthSlabTax + fifthSlabTax

# netPayment = grossPayPerAnnum - tax
# print(f"Tax : ${tax}")
# print(f"Net pay after tax: ${netPayment}")


def calculate_tax(income):
    brackes = [
    (15600, 10.5),
    (53500, 17.5),
    (78100, 30),
    (180000, 33),
    (float("inf"), 0.39), 
    ]

    tax_total = 0
    previous_limit = 0

    for limit, rate in brackes:
        if income > previous_limit:
            taxable_amount = min(income, limit) - previous_limit
            tax_total += taxable_amount * rate/100
            previous_limit = limit
        else:
            break

    return tax_total

def main():
    hours_worked = float(input("Enter hours worked per annum (NZ$): "))
    hourly_rate = float(input("Enter hourly pay rate (NZ$): "))
    income = calculate_gross_pay(hourly_rate, hours_worked)
    tax_total = calculate_tax(income)
    net_pay = income - tax_total
    
    print("-" * 45)
    print(f"{'|'} {'Gross Pay':<15} {'| Tax':<15} {'| Net Pay |':<15}")
    print("-" * 45)
    print(f"{'|'} {income:<15} {'|'} {tax_total:<13} {'|'} {net_pay:<7} {'|'}")
    print("-" * 45)
    
    

if __name__ == "__main__":
    main()