# Transaction(s) failed to sync in Tally.

Source: https://taxone.vyapar.com/help/articles/transaction-s-failed-to-sync-in-tally

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Transaction(s) failed to sync in Tally.](/help/articles/transaction-s-failed-to-sync-in-tally)

[Transaction(s) failed to sync in Tally](#transaction-s-failed-to-sync-in-tally)[Follow the given instructions to check the error of entry failure:](#follow-the-given-instructions-to-check-the-error-of-entry-failure-)[Steps to Check the Error in the IMP File:](#steps-to-check-the-error-in-the-imp-file-)[Step 1: Access the Tally File Location](#step-1-access-the-tally-file-location)[Step 2: Locate the IMP File](#step-2-locate-the-imp-file)[Step 3: Open the IMP File](#step-3-open-the-imp-file)[Step 4: Identify the Error](#step-4-identify-the-error)[Step 5: Rectify the Error](#step-5-rectify-the-error)[Fixing Common Errors in Tally Sync](#fixing-common-errors-in-tally-sync)[1. Date Out of Range](#1-date-out-of-range)[2. Extra Space in the Ledger or Company Name:](#2-extra-space-in-the-ledger-or-company-name-)[3. Voucher Numbering Not Set to Automatic:](#3-voucher-numbering-not-set-to-automatic-)[4. Tally Running in Educational Mode:](#4-tally-running-in-educational-mode-)[5. Ledger Name Altered/Deleted in Tally:](#5-ledger-name-altered-deleted-in-tally-)[6. Voucher Type Does Not Exist:](#6-voucher-type-does-not-exist-)[Important Note ✍️](#important-note-)

# Transaction(s) failed to sync in Tally.

When we send transactions to tally, those entries will either be created or fail to sync in tally. It could be due to various reasons.

### Transaction(s) failed to sync in Tally

#### Follow the given instructions to check the error of entry failure:

When you select ledgers for all transactions and click the **"Send transaction to Tally"** button, those transactions are synced in Tally.

However, sometimes the entries may fail to sync due to the following reasons:

* **The date is out of range**
* **Extra space in the name of ledgers or company name**
* **Voucher numbering setting is not set to automatic in Payment, Receipt & Contra vouchers**
* **Tally running in educational mode**
* **Ledger name altered/deleted in Tally after uploading the document or selecting ledgers in Suvit**
* **A voucher type does not exist**

### Steps to Check the Error in the IMP File:

#### Step 1: Access the Tally File Location

![1B2041.png](https://strapi.suvit.io/uploads/1_B2041_8c1753ddb8.png)

* Right-click on the Tally application shortcut on your desktop and click **Open File Location**.

#### Step 2: Locate the IMP File

![2B2042.png](https://strapi.suvit.io/uploads/2_B2042_dcfc010825.png)

* Look for the **IMP file**. It is usually located right below the Tally application itself.

#### Step 3: Open the IMP File

![3B2043.png](https://strapi.suvit.io/uploads/3_B2043_2ece2bf918.png)

* Open the file in **Notepad**, scroll to the bottom, and use **CTRL+F** to search for **"Error: 1"**. Use the **Find Next** option to locate the error details.

#### Step 4: Identify the Error

![4B2044.png](https://strapi.suvit.io/uploads/4_B2044_41b1a027b6.png)

* The **"Error: 1"** log will display the specific reason for the error, as shown above.

#### Step 5: Rectify the Error

* Correct the identified issue and resend the transactions to Tally for successful syncing.

---

### Fixing Common Errors in Tally Sync

#### **1. Date Out of Range**

* Verify the **book beginning date** in Tally.
* Ensure it aligns with your bank statement period.
* Example: If your bank statement is for FY 2021-22, set the book beginning date to **April** Follow this [Click here](https://help.suvit.io/articles/date-out-of-range) to get it solved.

#### **2. Extra Space in the Ledger or Company Name:**

* Extra spaces often occur when pasting names into Tally.

![5spaceinledger1.png](https://strapi.suvit.io/uploads/5spaceinledger1_39fe736c8c.png)  
![6spaceinledger3.png](https://strapi.suvit.io/uploads/6spaceinledger3_c13eca10fc.png)

* Use Suvit’s **Ledger Module** to detect names with unwanted spaces. **Search** for **&#**
* Remove extra spaces in Tally and re-sync the ledgers by using **Desktop Apllication** → **Sync Master**

#### **3. Voucher Numbering Not Set to Automatic:**

* If the error log indicates "Voucher number cannot be left blank," set the numbering to **Automatic** for Payment, Receipt, and Contra vouchers.
* Navigate to:  
  **Gateway of Tally > Alter > Voucher Type**  
  Alternatively, press **Alt+G** (Go To) > **Alter Master** > **Voucher Type**.
* Change the "Methods of Numbering" to **Automatic** as shown below:  
  ![7Method-of-voucher-numbering-Voucher-Type-Alteration.jpg](https://strapi.suvit.io/uploads/7_Method_of_voucher_numbering_Voucher_Type_Alteration_aff8b68641.jpg)

#### **4. Tally Running in Educational Mode:**

* If the error log is blank, verify that Tally is not running in educational mode.
* Switch to the licensed mode and resend the transactions.

#### **5. Ledger Name Altered/Deleted in Tally:**

* Avoid altering or deleting ledger names in Tally after uploading the bank statement or selecting ledgers in Suvit.
* If changes are made, sync the ledgers again, reselect the altered ones, and save them before resending the data.

#### **6. Voucher Type Does Not Exist:**

* Ensure that voucher types are standard, such as **Payment**, **Receipt**, and **Contra**.
* Custom voucher types like "Cash Payment" or "Bank Payment" may cause syncing issues.

---

#### **Important Note ✍️**

If data fails to sync, stay calm. Identify the issue, correct it, and resend the data to Tally for successful processing.