# Create Invoice for Purchase and Purchase-Return

Source: https://taxone.vyapar.com/help/articles/create-invoice-for-purchase-and-purchase-return

[All Collection](/help)[Purchase and Purchase Return](/help/collections/purchase-and-purchase-return)[Create Invoice for Purchase and Purchase-Return](/help/articles/create-invoice-for-purchase-and-purchase-return)

[Follow these simple steps to create a purchase bill:](#follow-these-simple-steps-to-create-a-purchase-bill-)[Step 1: Dashboard.](#step-1-dashboard-)[Step 2: Create Bill.](#step-2-create-bill-)[Step 3: Invoice Details](#step-3-invoice-details)[You may find this useful :](#you-may-find-this-useful-)

# Create Invoice for Purchase and Purchase-Return

Learn how to create Purchase and Purchase Return bills in Suvit. This guide ensures accurate entry and smooth syncing with Tally for efficient processing.

### Follow these simple steps to create a purchase bill:

#### Step 1: Dashboard.

![1.webp](https://strapi.suvit.io/uploads/1_8aba0c190d.webp)

* Click on **Data Entry Automation** -> **Transaction** -> **Purchase/Purchase Return**

#### Step 2: Create Bill.

![2.webp](https://strapi.suvit.io/uploads/2_a8ed3e1ecc.webp)

* Click the **Create Bill**.
* Choose between Purchase or Purchase Return.

#### Step 3: Invoice Details

![4 invoice.png](https://strapi.suvit.io/uploads/4_invoice_4521782957.png)

##### **1. Item Invoice:**

* Toggle between accounting invoice or item invoice based on your invoice.

**A. Voucher Details**
Type: Choose transaction type (Purchase/Return)

* Invoice No.: Enter invoice number
* Date: Select purchase date
* Party & GST: Enter supplier name and GST
* Ledger: Choose purchase account

**B. Item Details**

* Sr. No., Item Name, Qty, Rate, Amount, Action: Fields to list and calculate item details.

**C. Ledger Details:**

* Sr. No., Ledger Name, Amount, Action: Fields for ledger entries.

##### **2. Customer Details:**

* Includes customer information such as **name, phone, email, and address.** Displays outstanding receivables, credit terms, and recent related invoices.

\*\*Configuration Options\*\*

- Use the \*\*Configuration Window\*\* to select the fields displayed during voucher entry.

- such as \*\*Voucher Date\*\*, \*\*Supplier Invoice No.\*\*, \*\*Item Narration\*\*, etc. Save the changes once done.

![4.1 con.png](https://strapi.suvit.io/uploads/4\_1\_con\_d05990b1df.png)

![5 invoice.png](https://strapi.suvit.io/uploads/5_invoice_f30eb39e95.png)

**D. Tax, Narration, and Totals:** Add taxes, notes, and final amounts.

**E. Save the Bill:**

* Click S**ave & Close** to save and exit.
* Click **Save & Sync** to save and sync the bill directly with Tally.

```
If the transaction fails, check the tally.imp file in the Tally installation folder.
Fields marked with "*" are mandatory.
```

#### You may find this useful :

* How to Upload Purchase/Purchase Return Images & Pdf using OCR [Learn more](https://help.suvit.io/articles/ocr-purchase)