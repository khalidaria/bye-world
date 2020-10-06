#Khalid Aria
#Programming Excercise: 6
#Date Written: 08/29/2020
#Calculating state and county tax of a purchase

#User Input
purchaseInputAmount = round(float(input('Enter purchase amount: ')), 2)

# --- I am rounding the answers because it is currency ---
# --- I didn't use the format('.2f'), because calculations need to occur for state and county tax ---

#Variables
stateTaxRate = 0.05
countyTaxRate = 0.025
stateTaxAmount = round((purchaseInputAmount * stateTaxRate), 2)
countyTaxAmount = round((purchaseInputAmount * countyTaxRate), 2)
totalTaxAmount = stateTaxAmount + countyTaxAmount
totalSalesAmount = purchaseInputAmount + totalTaxAmount

#Output
print('Purchase Amount: $', purchaseInputAmount, sep='')
print('State Tax: $', stateTaxAmount, sep='')
print('County Tax: $', countyTaxAmount, sep='')
print('Total Sales Tax: $', totalTaxAmount, sep='')
print('Total Sales Amount: $', totalSalesAmount, sep='')
