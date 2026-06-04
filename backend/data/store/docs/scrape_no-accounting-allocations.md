# No accounting allocations in Sales/Purchase

Source: https://taxone.vyapar.com/help/articles/no-accounting-allocations

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[No accounting allocations in Sales/Purchase](/help/articles/no-accounting-allocations)

[No Accounting Allocations](#no-accounting-allocations)[Issue:](#issue-)[Explanation:](#explanation-)[Solution:](#solution-)[Step 1](#step-1)[Step 2](#step-2)[Step 3](#step-3)[Step 4](#step-4)[Screenshots for Reference:](#screenshots-for-reference-)

# No accounting allocations in Sales/Purchase

This error message appears while splitting a data if bill-wise details in a transaction are not saved.

### No Accounting Allocations

### Issue:

After saving the entries in **Suvit**, when you send data to Tally, it gets failed. Upon checking the reason, it shows **"No Accounting Allocations"**. This error occurs because the **Inventory Values are Affected** option is disabled in your Sales ledger.

### Explanation:

**No Accounting Allocations** means that the **Inventory Values are Affected** option is disabled in the ledger master for the inventories that have already been allocated in the voucher.

### Solution:

Follow the steps below to resolve this issue:

#### Step 1

* Select the **Sales ledger** in Alter and press **Enter** to open the **Ledger Alteration** screen.

#### Step 2

* Enable the option **Inventory Values are Affected** by selecting **"Yes"**.

#### Step 3

* Press **Ctrl+A** to save the ledger master.

#### Step 4

* Repeat the above steps for all the Sales/Purchase ledgers for the ledger's inventories.

### Screenshots for Reference:

* **Error Indication**  
  ![1.png](https://strapi.suvit.io/uploads/1_7e701c8909.png)