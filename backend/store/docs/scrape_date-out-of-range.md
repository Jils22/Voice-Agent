# Date out of Range error

Source: https://taxone.vyapar.com/help/articles/date-out-of-range

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Date out of Range error](/help/articles/date-out-of-range)

[Error Details in the Tally.imp File](#error-details-in-the-tally-imp-file)[For tally version 3 and above check All Exception for Error reason](#for-tally-version-3-and-above-check-all-exception-for-error-reason)[Common Error: "Date is Out of Range"](#common-error-date-is-out-of-range-)[Possible Causes](#possible-causes)[Solutions](#solutions)[Step 1: Verify Date Format in Excel](#step-1-verify-date-format-in-excel)[Step 2 : Update Book Beginning Date in Tally](#step-2-update-book-beginning-date-in-tally)[Step 3 : Re-save and Resend Data in Suvit](#step-3-re-save-and-resend-data-in-suvit)

# Date out of Range error

Identify and resolve failed entries in Suvit, including “Date is Out of Range” errors. Follow step-by-step solutions with visuals for smooth Tally sync.

**Below image indicates that an entry has failed:**

![1 entry fail in banking.png](https://strapi.suvit.io/uploads/1_entry_fail_in_banking_140e479d6a.png)

**1.** **Red color** indicates the number of entries that have failed.
**2.** From here, you can cross-check the error type by visiting [click here](https://help.suvit.io/articles/transaction-are-getting-fail-while-pushing-data-from-suvit-to-tally#how-to-check-tally-imp-file-for-errors).

### Error Details in the Tally.imp File

* If you need to locate the **Tally.imp** file [click here](https://help.suvit.io/articles/transaction-are-getting-fail-while-pushing-data-from-suvit-to-tally#how-to-check-tally-imp-file-for-errors) for step-by-step instructions.

![2 reason.png](https://strapi.suvit.io/uploads/2_reason_a87f2a53a7.png)

The Tally.imp file provides the following details:

1. **Date and time** of the entry.
2. **Company name**.
3. **Error reason**.
4. **Error type**.

### For tally version 3 and above check All Exception for Error reason

* Step 1. Press Alt+Y (Data) > All Exceptions.
* Step 2. The All Exceptions report appears, displaying the number of exceptions caused due to Import, Migrate/Repair, and Synchronization in Tally Prime.

![11  tally 3 error.png](https://strapi.suvit.io/uploads/11_tally_3_error_73a58197e2.png)

---

### Common Error: "Date is Out of Range"

The **"Date is Out of Range"** or **"Voucher date is earlier than Financial year beginning from date"** error in Tally occurs when a voucher date is **before the company's books beginning date**. This error can arise when importing data from Excel or syncing transactions.

---

### **Possible Causes**

1. The data in the Excel file is in the **wrong format**.
2. The **book beginning date** in Tally does not align with the uploaded data

---

### **Solutions**

#### Step 1: Verify Date Format in Excel

* Ensure the date format in the Excel file follows **DD-MM-YYYY**.

#### Step 2 : Update Book Beginning Date in Tally

* Modify the financial year and books beginning date in Tally to match the uploaded data.  
  ℹ . **Steps to update in Tally:**
* Press **Alt+K (Company)** → **Alter**.
* In the **Company Alteration** screen:
  + Update the **Financial Year Beginning** and **Books Beginning From** dates to match the uploaded data.
* Press **Ctrl+A** to save.

![3 tally alter.png](https://strapi.suvit.io/uploads/3_tally_alter_40c8cb76b9.png)

#### Step 3 : Re-save and Resend Data in Suvit

* After updating the date in Tally, **re-save** the data in Suvit and **resend** it to Tally.