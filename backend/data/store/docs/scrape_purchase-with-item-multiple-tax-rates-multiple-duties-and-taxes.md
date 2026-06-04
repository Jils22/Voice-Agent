# How to Handle Purchase bill Multiple Tax Rates with Multiple GST Ledgers with Stock Item in Suvit

Source: https://taxone.vyapar.com/help/articles/purchase-with-item-multiple-tax-rates-multiple-duties-and-taxes

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[How to Handle Purchase bill Multiple Tax Rates with Multiple GST Ledgers with Stock Item in Suvit](/help/articles/purchase-with-item-multiple-tax-rates-multiple-duties-and-taxes)

[How to upload an Excel sheet:Click Here](#how-to-upload-an-excel-sheet-click-here)[Mapping](#mapping)[Step 1: Field Mapping](#step-1-field-mapping)[Step 2: GST Mapping (Map Your Tax Ledger)](#step-2-gst-mapping-map-your-tax-ledger-)[How to pick Duties & Taxes amounts from the Excel sheet:](#how-to-pick-duties-taxes-amounts-from-the-excel-sheet-)[Step 3: Ledger Mapping](#step-3-ledger-mapping)

# How to Handle Purchase bill Multiple Tax Rates with Multiple GST Ledgers with Stock Item in Suvit

Manage bills with multiple items and tax rates using different GST ledgers in Suvit. Follow step-by-step Excel upload and mapping for accurate Tally sync.

---

If your bill includes \*\*single or multiple item\*\* with \*\*multiple tax rates\*\* also with \*\*Multiple GST ledger (Duties & Taxes)\*\*, you can enter it as follows:

* A bill with a **single or multiple items**.
* A bill with a **single or multiple tax rates**, using the **different/multiple** GST ledger **(Duties & Taxes)**.
  ![1.png](https://strapi.suvit.io/uploads/1_82963eb0cb.png)

\*\*Data requirement for excel sheet\*\*

![2.png](https://strapi.suvit.io/uploads/2\_f9227ffd50.png)

⇒  \*\*You need at least 7 types of data in your Excel sheet for mapping:\*\*

* In first bill there are 2 stock items with different gst rates(column number 2 & 3) having same reference number

* \*\*A\*\* → Need to create three additional three Row in excel sheet and name it \*\*SGST NAME, CGST NAME and IGST NAME\*\* respectively

* \*\*B\*\* → By using filter in \*\*GST TAX RATE\*\* or in \*\*Purchase Account\*\* name put \*\*DUTIES & TAXES name\*\* respectively as shown in the above image. (All three fields are compulsory so if IGST is not applicable, kindly create IGST in Tally)

* 1. \*\*REFERENCE NO:\*\* A unique number for each sale.

* 2. \*\*INVOICE DATE:\*\* The date the Purchase happened.

* 3. \*\*PARTY NAME:\*\* Name of the client (as entered in Tally).

* 4. \*\*PURCHASE LEDGER:\*\* The Purchase account name (GST Ledger).

* 5. \*\*NAME OF ITEM:\*\* The product sold (e.g., Mobile, Laptop).

* 6. \*\*QUANTITY\*\* or \*\*Rate\*\* (both cannot be mapped together).

* 7. \*\*AMOUNT:\*\* Total price before tax (Quantity × Rate = Taxable Amount).

⇒ \*\*Not Mandatory list\*\*

* 8. \*\*GST NO:\*\* Client's GST number.

* 9. \*\*PLACE OF SUPPLY:\*\* State or city where the item was delivered.

* 10. \*\*SGST, CGST, IGST:\*\* Duties & Taxes amounts (required only for \*\*Manual Calculation\*\*).

* 11. \*\*TOTAL AMOUNT:\*\* Grand total including taxes (for verification).

* Other things to keep in mind: [Click Here](https://help.suvit.io/articles/mandatory-things-to-check-before-using-purchase-purchase-return-module)

#### How to upload an Excel sheet:[Click Here](https://help.suvit.io/articles/uploading-purchase-purchase-return-data-through-an-excel-sheet)

### Mapping

* Click on your file to open the *Mapping Process*.

![1sales4.png](https://strapi.suvit.io/uploads/1sales4_e47be02491.png)

### **Step 1: Field Mapping**

![4.png](https://strapi.suvit.io/uploads/4_bf92dddd24.png)

1. **Choose your data type**: Select **Item invoice**.
2. **Mapped Fields:** These are matched fields from your uploaded data.
3. **Unmapped Fields:** Fields not yet matched. Choose the correct Tally fields for them.
4. **Your Sheet Header:** Shows headings from your Excel sheet.
5. **Tally Fields:** Fields matched with Tally. You can change them if needed.
6. **Your Sheet Data:** Shows sample data for cross-checking.
7. **Tally Fields Selection:** Choose the correct field from the dropdown.
8. Press **Next** to move to **GST Mapping**.

### **Step 2: GST Mapping (Map Your Tax Ledger)**

![5.png](https://strapi.suvit.io/uploads/5_75825549cf.png)

9. **GST Ledger from Excel Sheet:** Change to **Yes**
10. **GST Auto Calculation:** If GST rates are already defined in Tally, leave this setting as it is.
11. **Duties & Taxes:** Choose a common Duties & Taxes ledger.

* **Example:** select **SGST, CGST, IGST**.

### How to pick Duties & Taxes amounts from the Excel sheet:

![7.png](https://strapi.suvit.io/uploads/7_f10ec2a2e6.png)

* **A. Manual Calculation:** If you click **NO**, pick the Duties & Taxes amounts (SGST, CGST, IGST) from your sheet.
* **B. Tick-mark the tax amounts:** Use the tick option to assign **Duties & Taxes amounts**.

12. Press **Next** to move to \*\* Other Ledger Mapping\*\*.

```
**Note:** SGST, CGST, and IGST Tax Ledgers are mandatory. You can also map the round-off ledger.
```

### **Step 3: Ledger Mapping**

![5.png](https://strapi.suvit.io/uploads/3_7c6bbdda35.png)

* In this step, map additional fields such as **Discount** or **Freight Amount** by selecting the appropriate Excel header and Tally ledger.

Click **Save & Proceed** to finalize the process.

This format will be saved for future uploads in Suvit.