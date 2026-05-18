# With Item - Single Tax Rate - Common GST (Duties & Taxes)

Source: https://taxone.vyapar.com/help/articles/with-item-single-tax-rate-common-gst

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[With Item - Single Tax Rate - Common GST (Duties & Taxes)](/help/articles/with-item-single-tax-rate-common-gst)

[How to upload an Excel sheet:Click Here](#how-to-upload-an-excel-sheet-click-here)[Mapping](#mapping)[Step 1: Field Mapping](#step-1-field-mapping)[Step 2: GST Mapping (Map Your Tax Ledger)](#step-2-gst-mapping-map-your-tax-ledger-)[How to pick Duties & Taxes amounts from the Excel sheet:](#how-to-pick-duties-taxes-amounts-from-the-excel-sheet-)[Step 3: Ledger Mapping](#step-3-ledger-mapping)[For Next Step Click Here](#for-next-step-click-here)

# With Item - Single Tax Rate - Common GST (Duties & Taxes)

Learn to manage bills with same tax rates and a common GST ledger. Follow step-by-step instructions to upload and map Excel sheets for smooth data entry.

---

If your bill has items with the \*\*same tax rate\*\* and uses the \*\*same GST ledger (Duties & Taxes)\*\*, you can enter it like this.
This works for:

* A bill with **one item**.
* A bill with **many items** (as long as all items have the **same tax rate**).

![1. sample entry.png](https://strapi.suvit.io/uploads/1_sample_entry_8a1bc05f0c.png)

\*\*Data requirement for excel sheet\*\*

![2. sample excel sheet.png](https://strapi.suvit.io/uploads/2\_sample\_excel\_sheet\_e3f1e72760.png)

⇒  \*\*You need at least 7 types of data in your Excel sheet for mapping:\*\*

* 1. \*\*REFERENCE NO:\*\* A unique number for each sale.

* 2. \*\*INVOICE DATE:\*\* The date the sale happened.

* 3. \*\*PARTY NAME:\*\* Name of the client (as entered in Tally).

* 4. \*\*SALES LEDGER:\*\* The sales account name (GST Ledger).

* 5. \*\*NAME OF ITEM:\*\* The product sold (e.g., Mobile, Laptop).

* 6. \*\*QUANTITY\*\* or \*\*Rate\*\* (both cannot be mapped together).

* 7. \*\*AMOUNT:\*\* Total price before tax (Quantity × Rate = Taxable Amount).

⇒ \*\*Not Mandatory list\*\*

* 8. \*\*GST NO:\*\* Client's GST number.

* 9. \*\*PLACE OF SUPPLY:\*\* State or city where the item was delivered.

* 10. \*\*SGST, CGST, IGST:\*\* Duties & Taxes amounts (required only for \*\*Manual Calculation\*\*).

* 11. \*\*TOTAL AMOUNT:\*\* Grand total including taxes (for verification).

* Other things to keep in mind: [Click Here](https://help.suvit.io/articles/mandatory-things-to-check-before-using-the-sales-sales-return-module)

#### How to upload an Excel sheet:[Click Here](https://help.suvit.io/articles/uploading-sales-sales-return-data-through-an-excel-sheet)

### Mapping

* Click on your file to open the *Mapping Process*.

![1sales4.png](https://strapi.suvit.io/uploads/1sales4_e47be02491.png)

### **Step 1: Field Mapping**

![3 mapping 1.png](https://strapi.suvit.io/uploads/3_mapping_1_1cf45dae68.png)

1. Choose your data type: Select **Item invoice**.
2. **Mapped Fields:** These are matched fields from your uploaded data.
3. **Unmapped Fields:** Fields not yet matched. Choose the correct Tally fields for them.
4. **Your Sheet Header:** Shows headings from your Excel sheet.
5. **Tally Fields:** Fields matched with Tally. You can change them if needed.
6. **Your Sheet Data:** Shows sample data for cross-checking.
7. **Tally Fields Selection:** Choose the correct field from the dropdown.
8. Press **Next** to move to **GST Mapping**.

### **Step 2: GST Mapping (Map Your Tax Ledger)**

![4 gst mapping1.png](https://strapi.suvit.io/uploads/4_gst_mapping1_bca4969b05.png)

--- OR ---

![5 gst mapping1.png](https://strapi.suvit.io/uploads/5\_gst\_mapping1\_0599fcd7a2.png)

9. **GST Ledger from Excel Sheet:** Keep this as it is.
10. **GST Auto Calculation:** If GST rates are already defined in Tally, leave this setting as it is.
11. **Duties & Taxes:** Choose a common Duties & Taxes ledger.

* **Example:** For an 18% GST rate, select **SGST 9, CGST 9, IGST 18**.

12. Press **Next** to move to **Other Mapping**.

### How to pick Duties & Taxes amounts from the Excel sheet:

![6 gst calculation of.png](https://strapi.suvit.io/uploads/6_gst_calculation_of_b11f0e0432.png)

* **A. Manual Calculation:** If you click **NO**, pick the Duties & Taxes amounts (SGST, CGST, IGST) from your sheet.
* **B. Tick-mark the tax amounts:** Use the tick option to assign **Duties & Taxes amounts**.
* **C. Verify amounts for SGST, CGST, IGST from the sheet.**

12. Press **Next** to move to **Other Mapping**.

```
**Note:** SGST, CGST, and IGST Tax Ledgers are mandatory. You can also map the round-off ledger.
```

### **Step 3: Ledger Mapping**

![5.png](https://strapi.suvit.io/uploads/3_7c6bbdda35.png)

* In this step, map additional fields such as **Discount** or **Freight Amount** by selecting the appropriate Excel header and Tally ledger.

Click **Save & Proceed** to finalize the process.

This format will be saved for future uploads in Suvit.

### For Next Step [Click Here](https://help.suvit.io/articles/how-do-we-process-or-push-sales-sales-return-data-to-tally)