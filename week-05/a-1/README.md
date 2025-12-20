 # Chain Restaurant: Ingredient Ordering Subsystem

 ## Use Case Diagram (Ingredient Ordering)
 The **use case diagram** shows the main actors and their interactions within the ordering subsystem.
 
 - **Kitchen Staff**
   - Check stock level of ingredients
   - Update stock level
   - Check ingredient quality
   - Request order to manager
 - **Manager**
   - Approve order
   - Buy ingredients
   - Make payment *(included as part of buying ingredients)*
 - **Supplier**
   - Confirm order
   - Deliver order
 
 It also captures relationships between use cases:
 
 - **Buy Ingredients** `<<include>>` **Make Payment**
 - **Buy Ingredients** `<<include>>` **Report Quality Issue to Supplier**
 - **Return goods to supplier** `<<extend>>` **Report Quality Issue to Supplier** (only happens if a quality issue is confirmed)
 
 ## Activity Diagram (Ingredient Ordering Flow)
 The **activity diagram** describes the step-by-step workflow, focusing on decision points and the order of actions.
 
 Typical flow:
 
 - **Kitchen Staff** checks ingredient stock and quality.
 - If stock is low, staff **requests an order**.
 - **Manager** reviews and **approves** the order.
 - The restaurant **buys ingredients** and **makes payment**.
 - **Supplier** **confirms** and **delivers** the order.
 - After delivery, staff checks quality.
 - If there is a quality issue, the restaurant **reports the issue to the supplier** and may **return goods**.
 