# "Failed" status after processing the Statement

Source: https://taxone.vyapar.com/help/articles/failed-status-after-processing-the-statement

[All Collection](/help)[Banking](/help/collections/banking)["Failed" status after processing the Statement](/help/articles/failed-status-after-processing-the-statement)

[If the Status is "Complete"](#if-the-status-is-complete-)[If the Status is "Failed"](#if-the-status-is-failed-)[Common Reasons for Failure](#common-reasons-for-failure)[Tips to Avoid Document Failure](#tips-to-avoid-document-failure)[You may find this usesful](#you-may-find-this-usesful)

# "Failed" status after processing the Statement

Here you can understand why the bank statement you uploaded shows a "Failed" status and what points you can consider resolving the issue.

##### Once you upload the bank statement, its status will show as **"Processing"**. After a few minutes, the status will change to either **"Complete"** or **"Failed"**.

### If the Status is "Complete"

* You can proceed with the further process of ledger **selection and sending** the transactions to Tally.

### If the Status is "Failed"

* Check the **reason for failure**, make corrections in the document, and re-upload it. Refer to the image below for better understanding:

![failed status.png](https://strapi.suvit.io/uploads/failed_status_cbe4b0ae2f.png)

---

#### **Common Reasons for Failure**

1. **Unsupported format**
2. **Closing Balance mismatch**
3. **Missing column headers**
4. **Handwritten or punching marks on the statement**
5. **Password-protected file**

---

#### **Tips to Avoid Document Failure**

1. **Ensure proper alignment:**

* The data should be well-aligned and not merged.
* For example, the date line should not merge with the narration, and narration should not overflow into the amount column.

2. **Complete transaction data:**

* Ensure no transaction is missing or incomplete.

3. **Date continuity:**

* The transactions should be in date-wise chronological order.

4. **Column headers:**

* The statement must include headers like **Date**, **Narration**, **Debit Amount**, and **Credit Amount**.
* If you're splitting the bank statement, ensure headers are included on each part being uploaded.

5. **Scanned PDFs:**

* Ensure the scanned PDF is:  
  -> **Aligned and Maintains** continuity across all pages.  
  -> Not too\*\* blurred or dark,\*\* avoiding ink marks from previous pages.  
  -> Free from **punching marks, pen/ink marks, or handwritten notes** on the data.  
  -> Clear, without overlapping narration in the amount fields.  
  -> Free from cropped or incomplete data.

6. **Excel Sheets:**

* Ensure the data is in the first sheet of the workbook.
* Include columns for **Date**, **Narration**, **Debit Amount**, and **Credit Amount**.

---

#### You may find this usesful

* How to Remove a Password from a Password-Protected Document [Learn more](https://help.suvit.io/articles/how-to-remove-a-password-from-a-password-protected-file)