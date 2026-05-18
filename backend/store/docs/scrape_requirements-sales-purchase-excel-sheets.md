# Requirements for Sales and Purchase Excel Sheets

Source: https://taxone.vyapar.com/help/articles/requirements-sales-purchase-excel-sheets

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Requirements for Sales and Purchase Excel Sheets](/help/articles/requirements-sales-purchase-excel-sheets)

[What is Required for the Sales/Purchase Excel Sheet?](#what-is-required-for-the-sales-purchase-excel-sheet-)[For Sales/Purchase Excel Sheet](#for-sales-purchase-excel-sheet-) [Mandatory Fields (Without Stock Items):](#mandatory-fields-without-stock-items-)[Mandatory Fields (With Stock Items):](#mandatory-fields-with-stock-items-)[Optional Fields (For Both Sales and Purchase Sheets):](#optional-fields-for-both-sales-and-purchase-sheets-)[How to Modify the Excel Sheet](#how-to-modify-the-excel-sheet-) [Step 1 - Create Mandatory Columns](#step-1-create-mandatory-columns)[Step 2 - Ensure Correct Formatting](#step-2-ensure-correct-formatting)[Step 3 - Add Optional Columns](#step-3-add-optional-columns)[Example of a Completed Excel Sheet](#example-of-a-completed-excel-sheet)[Without Stock Item](#without-stock-item)[With Stock](#with-stock)[Final Steps](#final-steps)[PRO TIPS](#pro-tips)

# Requirements for Sales and Purchase Excel Sheets

Learn the mandatory and optional fields for sales/purchase Excel sheets in Suvit. Follow step-by-step formatting and data tips for smooth Tally integration.

### What is Required for the Sales/Purchase Excel Sheet?

* To ensure your Excel sheet is compatible with Suvit and Tally, you need to include specific mandatory fields and optional fields based on your requirements.

### For Sales/Purchase Excel Sheet

#### Mandatory Fields (Without Stock Items):

1. **Reference No:** A unique number for each transaction, such as INV001 or SALE2025 or PURCHASE2025.
2. **Invoice Date:** The date of the transaction in formats like DD-MM-YYYY.
3. **Party Name:** The name of the client or customer as recorded in Tally, such as John Doe or ABC Pvt Ltd.
4. Particular **(Sales /Purchase Ledger)**: The name of the sales/purchase account, like GST Ledger, for example, Local GST 18% or Purchase GST 18%
5. **Amount:** The total price before tax (taxable amount), such as 10,000.

#### Mandatory Fields (With Stock Items):

1. **Reference No:** A unique number for each transaction, such as INV001 or SALE2025 or PURCHASE2025.
2. **Invoice Date:** The date of the transaction in formats like DD-MM-YYYY .
3. **Party Name:** The name of the client or customer as recorded in Tally, such as John Doe or ABC Pvt Ltd.
4. Particular **(Sales /Purchase Ledger)**: The name of the sales/purchase account, like GST Ledger, for example, Local GST 18% or Purchase GST 18% .
5. **Name of Item:** The name of the product sold, such as Laptop or Mobile.
6. **Quantity:** You can choose quantity (number of units sold, e.g., 5)
7. **Amount And Rate:** You can choose either Rate OR Amount. (Quantity x Rate = Amount and Amount / Quantity = Rate)

#### Optional Fields (For Both Sales and Purchase Sheets):

* **GST No:** GST Identification Number of the client or vendor.
* **Place of Supply:** Location where goods or services were delivered, such as Maharashtra or Delhi.
* **SGST, CGST, IGST:** Taxes applied, useful for manual calculations.
* **Total Amount:** The grand total, including taxes, for validation purposes.

### How to Modify the Excel Sheet

#### Step 1 - Create Mandatory Columns

Open your Excel file and ensure the following columns are included:

* **For Sales/Purchase without stock:** Reference No, Invoice Date, Party Name, Sales/Purchase Ledger, Amount.
* **For Sales/Purchase with stock:** Add Name of Item, Quantity and Rate or Amount.

#### Step 2 - Ensure Correct Formatting

* **Dates:** Use a consistent format like DD-MM-YYYY.
* **Amounts:** It should be in Number Format , 10000.00.
* **GST Numbers:** Use the standard 15-character GST number format.

#### Step 3 - Add Optional Columns

Include columns for GST No, Place of Supply, or Total Amount if needed for additional tracking or compliance.

How to Input Data into the Excel Sheet

* \*\*Step 1\*\* - Input Reference Numbers: Assign unique numbers for each transaction, such as \*\*INV001 or INV002\*\*.

* \*\*Step 2\*\* - Enter Invoice or Purchase Dates: Add the exact date of the transaction, for example, \*\*27-05-2025\*\*.

* \*\*Step 3\*\* - Add Party Names: Input the names of clients or vendors exactly as they appear in Tally, such as \*\*Suvit\*\* or \*\*XYZ Pvt Ltd\*\*.

* \*\*Step 4\*\* - Fill in the Sales or Purchase Ledger: Use the correct GST Ledger account name, like \*\*Local GST 18%\*\*, \*\*Sales GST 18%\*\*, \*\*Purchase 18%\*\*.

* \*\*Step 5\*\* - List Items (If Applicable): For transactions involving stock, enter the name of the item, quantity, and rate (choose one if mapping).

* \*\*Step 6\*\* - Taxable Amount: Specify the amount on which the GST will apply.

* \*\*Step 7\*\* - Include Optional Details (If Required): Add GST numbers, taxes like SGST/CGST/IGST, and place of supply if necessary.

### Example of a Completed Excel Sheet

* Here is the two sets of table with your data inserted in form of **Without Stock** and **With Stock**:

#### Without Stock Item

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Reference No** | **Invoice Date** | **Party Name** | **Sales/Purchase Ledger** | **Amount** | **GST No** | **Place of Supply** |
| INV001 | 28-01-2025 | John Doe | Local GST 18% | 50000 | 24ABCDE1234FZ | Gujarat |
| INV002 | 29-01-2025 | ABC Pvt Ltd | Interstate GST 18% | 20000 | 29BCDEF5678XZ | Karnataka |
| INV003 | 30-01-2025 | XYZ Corp | Local GST 18% | 30000 | 24XYZ1234ABC | Gujarat |

#### With Stock

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Reference No** | **Invoice Date** | **Party Name** | **Sales/Purchase Ledger** | **Name of Item** | **Qty** | **Rate** | **Amount** | **GST No** | **Place of Supply** |
| INV001 | 28-01-2025 | John Doe | Local GST 18% | Laptop | 2 | 50000 | 100000 | 24ABCDE1234FZ | Gujarat |
| INV002 | 29-01-2025 | ABC Pvt Ltd | Interstate GST 18% | Mobile | 5 | 20000 | 100000 | 29BCDEF5678XZ | Karnataka |
| INV003 | 30-01-2025 | XYZ Corp | Local GST 18% | Tablet | 3 | 30000 | 90000 | 24XYZ1234ABC | Gujarat |

### Final Steps

1. Save the Excel file in **.xlsx** or **.csv** format.

\*\*Sample Excel Sheet\*\*

\*\*Click on file to Download\*\*

* [Sales-without-item-sample-file.xlsx](https://strapi.suvit.io/uploads/Sales\_without\_item\_sample\_file\_23467f2f0b.xlsx)

* [Sales-with-item-sample-file.xlsx](https://strapi.suvit.io/uploads/Sales\_with\_item\_sample\_file\_e862d4e41b.xlsx)

* [Purchase-without-item-sample-file.xlsx](https://strapi.suvit.io/uploads/Purchase\_without\_item\_sample\_file\_1fbfa350c8.xlsx)

* [Purchase-with-item-sample-file.xlsx](https://strapi.suvit.io/uploads/Purchase\_with\_item\_sample\_file\_49273d3d23.xlsx)

2. Upload it to Suvit for mapping to Tally:

* Common Mapping for Sales <a href="https://help.suvit.io/articles/auto-mapping-excel-sheet-data-with-suvit-configuration"target="\_blank">Click Here
* Common Mapping for Purchase <a href="https://help.suvit.io/articles/auto-mapping-purchas"target="\_blank">Click Here

3. Validate the data and verify that all fields are mapped correctly.

### PRO TIPS

1. Use Minus: ( **-** ) Symbol for such as Discount, round off
2. Party Name: Use same name from Tally
3. Always use defined a GST Rate Sales/Purchase Account ledger
4. In Stock Item define GST the Rate
5. Add additional row in the end. For example: TDS, Voucher Number, Consignee Details Dispatch details etc.