# Transaction are getting fail while pushing data from Suvit to tally?

Source: https://taxone.vyapar.com/help/articles/transaction-are-getting-fail-while-pushing-data-from-suvit-to-tally

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Transaction are getting fail while pushing data from Suvit to tally?](/help/articles/transaction-are-getting-fail-while-pushing-data-from-suvit-to-tally)

[Common reasons for Tally entry failures:](#common-reasons-for-tally-entry-failures-)[How to Check Tally IMP File for Errors](#how-to-check-tally-imp-file-for-errors)[Step 1: Locate the Tally Application](#step-1-locate-the-tally-application)[Step 2: Open File Location](#step-2-open-file-location)[Step 3: Find the Tally IMP File](#step-3-find-the-tally-imp-file)[Step 4: Open and Review the File](#step-4-open-and-review-the-file)[Additional Note ✍](#additional-note-)[For tally version 3 and above check All Exception for Error reason](#for-tally-version-3-and-above-check-all-exception-for-error-reason)[Here are a few reasons why the entry failed:](#here-are-a-few-reasons-why-the-entry-failed-)

# Transaction are getting fail while pushing data from Suvit to tally?

Entries not meeting Tally requirements may fail in Suvit. Read the article to understand common reasons for failure and follow steps to resolve them easily.

### Common reasons for Tally entry failures:

1. Ledger name not found.
2. Voucher number cannot be left blank.
3. No accounting allocation.
4. Voucher number already exists.
5. Educational mode in Tally.

* And many more. Below are the steps to check the reasons for entry failure:

### How to Check Tally IMP File for Errors

* Follow these steps to locate and review the **Tally.imp** file, which logs import details and errors.

#### Step 1: Locate the Tally Application

![1 img.png](https://strapi.suvit.io/uploads/1_img_0b343be71f.png)

1. **Right-click the Tally icon** on your desktop.
2. Select **Properties**.

#### Step 2: Open File Location

![2 img.png](https://strapi.suvit.io/uploads/2_img_6a1ab13c92.png)

3. Click on **Open File (.exe) Location**.

#### Step 3: Find the Tally IMP File

![27YJ1Z39tC5M1qd8qY7iiBPmCKoOSC0tPVxA(copy).png](https://strapi.suvit.io/uploads/27_YJ_1_Z39t_C5_M1qd8q_Y7ii_B_Pm_C_Ko_OSC_0t_P_Vx_A_copy_3b2df23f29.png)

4. Locate the **Tally.imp** file in the same folder as **Tally.exe**.

#### Step 4: Open and Review the File

5. **Right-click** on **Tally.imp** and open it with **Notepad**.
6. Scroll to the **end of the file** to check for recent errors or logs.

### **Additional Note ✍**

* The **Tally.imp file** contains detailed logs of all import activities, including reasons for errors.
* You can use this log to troubleshoot issues in data import.

### For tally version 3 and above check All Exception for Error reason

![11  tally 3 error.png](https://strapi.suvit.io/uploads/11_tally_3_error_73a58197e2.png)

* Step 1. Press **Alt+Y (Data)** > **All Exceptions**.
* Step 2. The All Exceptions report appears, displaying the number of exceptions caused due to Import, Migrate/Repair, and Synchronization in Tally Prime.

### Here are a few reasons why the entry failed:

\*\*The date is out Range! Can`t import!\*\*

\*\*Cause:\*\*

* When the Date of the entry does not fall between the current period of the Company

\*\*Solution:\*\*

* Go to \*\*Company (alt+k) → Alter → change Financial year beginning\*\* from or \*\*Books beginning\*\* from or both as per requirement

* Follow this [link](https://help.suvit.io/articles/date-out-of-range)to get it solved.
\*\*No Accounting Allocations\*\*

\*\*Cause:\*\* \*\*Inventory Values are affected disabled\*\*

* If the \*\*"Inventory Values are affected"\*\* option is disabled in the ledger master for the ledger inventories that have already been allocated in voucher, the error message may appear

![no-accounting-allocation1.gif](https://strapi.suvit.io/uploads/no\_accounting\_allocation1\_244a11d1e0.gif)

\*\*Solution:\*\*

* Select No Accounting Allocations, and drill down.

* In the \*\*Ledger Alteration\*\* screen, press \*\*F12\*\* > \*\*Use Inventory Allocation for Ledgers\*\* to \*\*Yes\*\*.
  Now you can see the option \*\*Inventory values are affected\*\* in the \*\*Ledger Alteration\*\* screen. Set the option to \*\*Yes\*\*.

* Drill down from the relevant ledger.

* Accept the ledger to resolve the issue.

* Follow this [link](https://help.suvit.io/articles/no-accounting-allocations)to get it solved.
\*\*0 value entry can be passed from Sales/Purchase Transaction\*\*

Follow this [link](https://help.suvit.io/articles/value-entry-can-be-passed-from-sales-purchase-transaction)to get it solved.