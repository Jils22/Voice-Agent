# Mandatory things to check before using Purchase/Purchase Return module

Source: https://taxone.vyapar.com/help/articles/mandatory-things-to-check-before-using-purchase-purchase-return-module

[All Collection](/help)[Purchase and Purchase Return](/help/collections/purchase-and-purchase-return)[Mandatory things to check before using Purchase/Purchase Return module](/help/articles/mandatory-things-to-check-before-using-purchase-purchase-return-module)

[📋 Checklist for Excel Sheet Before Using Purchase / Purchase Return Module](#-checklist-for-excel-sheet-before-using-purchase-purchase-return-module)[✅ Do These Before Uploading Your Excel File:](#-do-these-before-uploading-your-excel-file-)[📘 How to Prepare Your Excel Sheet: Click here](#-how-to-prepare-your-excel-sheet-click-here)[📚 You May Find This Useful:](#-you-may-find-this-useful-)

# Mandatory things to check before using Purchase/Purchase Return module

One can record the export of goods, purchase under diff GST rates, nil-rated and exempt purchase, deemed export, and so on.

### 📋 Checklist for Excel Sheet Before Using Purchase / Purchase Return Module

Before uploading your **Purchase** or **Purchase Return** Excel file into Suvit, make sure it’s neat, clean, and Tally-ready.

Let’s break it down — **simple enough for anyone to follow!**

---

### ✅ Do These Before Uploading Your Excel File:

1. **Use the First Sheet Only**

   → Keep your data in the **first worksheet** of your Excel file.
2. **Headers Go on Top**

   → The **first row** should have titles like: Date, Invoice No., GST, Amount, etc.
3. **No Dots or Dollar Signs in Headings**

   → Don’t use symbols like **.** or **$** in your column titles.

   → Also, don’t put extra rows or headings above your data.
4. **Invoice Number Must Be Filled**

   → No blank invoice numbers allowed.
5. **Group Same Invoice Numbers Together**

   → Sort your data **A–Z** by Invoice Number to keep them lined up properly.
6. **Avoid Words Like NA / Not Applicable**

   → If GST isn’t available, just leave the cell **empty**.

   → Don’t write "NA", "none", or "not applicable".
7. **Use DD/MM/YYYY for Dates**

   → Example: 27/05/2022 (This is the right format)
8. **Delete Extra Totals or Notes**

   → Remove rows like “Grand Total” — Tally doesn’t need them.
9. **Keep it Under 10,000 Transactions**

   → Don’t go over **10,000 rows** in one sheet.
10. **Add a Ledger Column Based on GST**

    → Create a column that has **Purchase Ledger Name** as per the GST rate.
11. **GST Ledgers Must Exist in Tally**

    → Make sure **SGST, CGST, IGST** are created under **Duties & Taxes** in your Tally.
12. **Use Correct Excel Formats**

    → Text fields → Set as **TEXT** or **General**

    → Numbers → Set as **Number** format

→ Learn how to change formats: [Microsoft Support Link](https://support.microsoft.com/en-us/office/change-the-format-of-a-cell-0a45ff85-ee24-4276-94e8-aed6083e8050#:~:text=Select%20the%20cells%20with%20the,to%20change%20what%20you%20want.)

13. **Add a Column Named “Particular”**

    → Fill this with the correct **Purchase Ledger Name** as per GST rate.
    📌 Example: If GST is **18%**, then use the ledger with **18% Purchase** defined.
14. **Save as Excel Workbook (.xlsx)**

    → Use "Excel Workbook" format — not CSV or PDF.

#### 📘 How to Prepare Your Excel Sheet: [Click here](https://help.suvit.io/articles/requirements-sales-purchase-excel-sheets)

---

### 📚 You May Find This Useful:

Want to know how to upload your Excel file to Suvit? 👉 [Learn more](https://help.suvit.io/articles/uploading-purchase-purchase-return-data-through-an-excel-sheet)