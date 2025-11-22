# Simple Input Processing Output for hourly pay
hoursWorkedPerAnnum = float(input("Enter hours worked per annum: "))
hourlyPayRate = float(input("Enter hourly pay rate: "))
grossPayPerAnnum = hoursWorkedPerAnnum * hourlyPayRate
print("Gross pay without tax: ", grossPayPerAnnum)

# separator
print("*" * 20)

# tax calculation
if grossPayPerAnnum <= 15600:
    # 10.5% tax rate (10.5/100) 
    tax = grossPayPerAnnum * 0.105
elif grossPayPerAnnum <= 53500:
    # first slab tax
    firstSlabTax = 15600 * 0.105
    # second with 17.5%
    secondSlabTax = (grossPayPerAnnum - 15600) * 0.175
    tax = firstSlabTax + secondSlabTax
elif grossPayPerAnnum <= 78100:
    
    # first slab
    firstSlabTax = 15600 * 0.105
    # second slab with 17.5% rate...
    secondSlabTax = (53500 - 15600) * 0.175
    # 3rd with 30%
    thirdSlabTax = (grossPayPerAnnum - 53500) * 0.30
    tax = firstSlabTax + secondSlabTax + thirdSlabTax
elif grossPayPerAnnum <= 180000:
    # 1st (10.5)
    firstSlabTax = 15600 * 0.105
    # 2nd (17.5)
    secondSlabTax = (53500 - 15600) * 0.175
    # 3rd (30%)
    thirdSlabTax = (78100 - 53500) * 0.30
    # 4th (33%)
    fourthSlabTax = (grossPayPerAnnum - 78100) * 0.33
    tax = firstSlabTax + secondSlabTax + thirdSlabTax + fourthSlabTax
else:
    # 1st (10-.5)
    firstSlabTax = 15600 * 0.105
    # 2nd (17.5)
    secondSlabTax = (53500 - 15600) * 0.175
    # 3rd (30)
    thirdSlabTax = (78100 - 53500) * 0.30
    # 4th (33%)
    fourthSlabTax = (180000 - 78100) * 0.33
    # 5th (39%)
    fifthSlabTax = (grossPayPerAnnum - 180000) * 0.39
    tax = firstSlabTax + secondSlabTax + thirdSlabTax + fourthSlabTax + fifthSlabTax

netPayment = grossPayPerAnnum - tax
print(f"Tax : ${tax}")
print(f"Net pay after tax: ${netPayment}")