# azure_projects

To ensure the insert_azure_table.py can run properly, we need to install proper packages in Cloud CLI as below

- *pip install --user azurerm azure-cosmosdb-table azure-storage-queue packaging*

- *pip install --upgrade setuptools*

Based on the data provided in the project file, here is the detailed calculation for the Break-Even Point for the first quarter of 2024 before the disruption.
The Break-Even Point (BEP) for Q1 2024 is 21,070 units, which translates to AED 3,371,195 in sales revenue.
Below is the step-by-step breakdown of how these figures were derived.
1. Determine Sales Mix and Selling Prices
First, we establish the sales mix and selling prices based on the 2023 actuals provided in the case, as the forecast assumes the 2023 sales mix applies to 2024.
Total Units Sold (Q4 2023): 86,475
Sales Mix Ratio:
AG: $69,180 \div 86,475 = \mathbf{80\%}$
AGL: $17,295 \div 86,475 = \mathbf{20\%}$
Selling Prices (SP):
AG: AED 10,377,000 / 69,180 units = AED 150
AGL: AED 3,459,000 / 17,295 units = AED 200
2. Forecasted Volume for Q1 2024
To separate fixed and variable costs, we need the total forecasted units for Q1 2024.
Weighted Average Price: $(150 \times 0.80) + (200 \times 0.20) = \text{AED } 160$
Forecasted Revenue: AED 16,800,000
Forecasted Units: $16,800,000 \div 160 = \mathbf{105,000 \text{ units}}$
3. Separation of Fixed and Variable Costs
We must isolate the variable and fixed components for shipping and manufacturing overhead.
A. Shipping Costs (Mixed Cost)
Using the High-Low Method between Q4 2023 actuals and Q1 2024 forecasts:
High (Q1 2024): AED 539,400 cost for 105,000 units
Low (Q4 2023): AED 465,300 cost for 86,475 units
Variable Rate: $(539,400 - 465,300) \div (105,000 - 86,475) = \mathbf{\text{AED } 4 \text{ per unit}}$
Fixed Shipping Cost: $539,400 - (105,000 \times 4) = \mathbf{\text{AED } 119,400}$
B. Production Overhead (Mixed Cost)
The case specifies a Fixed Overhead (FOH) of AED 672,000 allocated equally among forecasted units.
Allocated FOH per unit: $672,000 \div 105,000 = \text{AED } 6.4 \text{ per unit}$
Variable Overhead (VOH): Subtract the allocated FOH from the total overhead given in the cost schedule.
AG VOH: $18 \text{ (Total)} - 6.4 \text{ (Fixed)} = \mathbf{\text{AED } 11.6}$
AGL VOH: $23 \text{ (Total)} - 6.4 \text{ (Fixed)} = \mathbf{\text{AED } 16.6}$
C. Sales Commission
Calculated as 3% of the selling price (AG: AED 4.5; AGL: AED 6.0).
4. Calculate Contribution Margins
We calculate the Unit Contribution Margin (CM) for each product by subtracting all variable costs from the selling price.
Cost Component
Product AG
Product AGL
Selling Price
AED 150.0
AED 200.0
Direct Material
32
60
Direct Labor
14.0
22.0
Variable Overhead
11.6
16.6
Variable Shipping
4.0
4.0
Sales Commission (3%)
4.5
6.0
Total Variable Cost
66.1
108.6
Unit Contribution Margin
AED 83.9
AED 91.4

Weighted Average Contribution Margin (WACM):
$$WACM = (83.9 \times 80\%) + (91.4 \times 20\%)$$
$$WACM = 67.12 + 18.28 = \mathbf{\text{AED } 85.4}$$
5. Calculate Total Fixed Costs
Summing all fixed costs identified for Q1 2024:
Admin Expenses: AED 610,000
Fixed Shipping: AED 119,400
Fixed Manufacturing Overhead: AED 672,000
Financial Expenses: AED 44,000
Total Fixed Costs: AED 1,445,400
6. Final Break-Even Calculation
$$Break\text{-}Even \text{ Point (Units)} = \frac{\text{Total Fixed Costs}}{\text{WACM}}$$
$$BEP = \frac{1,445,400}{85.4} \approx \mathbf{16925 \text{ units}}$$
$$Break\text{-}Even \text{ Revenue} = 16925 \text{ units} \times \text{AED } 160 \text{ (Avg Price)} \approx \mathbf{\text{AED } 2,708,000}$$

