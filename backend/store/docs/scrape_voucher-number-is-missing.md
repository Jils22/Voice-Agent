# Voucher number cannot be left Blank or Voucher Number is missing

Source: https://taxone.vyapar.com/help/articles/voucher-number-is-missing

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Voucher number cannot be left Blank or Voucher Number is missing](/help/articles/voucher-number-is-missing)

[Understanding Failed Entries in Banking & Sales/Purchase Module](#understanding-failed-entries-in-banking-sales-purchase-module)[Error Details in the Tally.imp File](#error-details-in-the-tally-imp-file)[For tally version 3 and above check All Exception for Error reason](#for-tally-version-3-and-above-check-all-exception-for-error-reason)[Common Error: "Voucher number cannot be left Blank" or "Voucher Number is missing"](#common-error-voucher-number-cannot-be-left-blank-or-voucher-number-is-missing-)[Possible Cause](#possible-cause)[Possible Solutions](#possible-solutions)[For Banking:](#for-banking-)[For Sales/Purchase:](#for-sales-purchase-)

# Voucher number cannot be left Blank or Voucher Number is missing

Troubleshoot failed entries in Suvit’s Banking Module. Identify common issues like missing voucher numbers and fix them easily with step-by-step solutions.

### Understanding Failed Entries in Banking & Sales/Purchase Module

Below image indicates that an entry has failed:

![1 entry fail .png](https://strapi.suvit.io/uploads/1_entry_fail_3a6c38fc48.png)

1. **Red color** indicates the number of entries that have failed.
2. From here, you can cross-check the error type by visiting.[Click Here](https://help.suvit.io/articles/transaction-are-getting-fail-while-pushing-data-from-suvit-to-tally)

### Error Details in the **Tally.imp** File

![2 reason.png](https://strapi.suvit.io/uploads/2_reason_fca32c6762.png)

The **Tally.imp** file provides the following details:

1. **Date and time** of the entry.
2. **Company name**.
3. **Error reason**.
4. **Error type**.

### For tally version 3 and above check All Exception for Error reason

* **Step 1**. Press Alt+Y (Data) > All Exceptions.
* **Step 2**. The All Exceptions report appears, displaying the number of exceptions caused due to Import, Migrate/Repair, and Synchronization in Tally Prime.
  ![3 tally 5.png](https://strapi.suvit.io/uploads/3_tally_5_c04085d0a0.png)

---

### Common Error: "Voucher number cannot be left Blank" or "Voucher Number is missing"

#### **Possible Cause**

* The **"Voucher number cannot be left Blank"** or **"Voucher Number is missing"** error in Tally occurs when a Method of voucher numbering is set manual and no input has been given for Voucher number.

---

### Possible Solutions

### For Banking:

* **Solution 1:** Change the **Voucher numbering method to Automatic** [Click Here](https://help.suvit.io/articles/voucher-number-cannot-be-left-blank-banking)
* **Solution 2:** Learn how to add voucher number in Banking(no need to change Voucher numbering method) [Click Here](https://help.suvit.io/articles/enable-voucher-number-banking)

### For Sales/Purchase:

* **Solution 1:** Change the **Voucher numbering method to Automatic**

  + Navigate to: **Gateway of Tally** > **Alter** > **Voucher Type** or (shortcut) press Alt+G (Go To) > Alter Master > Voucher Type.
  + Change the **"Methods of Numbering"** to Automatic
* **Solution 2:** Learn how to add voucher number in Sales/Purchase(no need to change Voucher numbering method) [Click Here](https://help.suvit.io/articles/configuring-other-settings-suvit-sales-sales-return)