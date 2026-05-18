# Processing Purchase Excel with Horizontal GST Rates and Duties & Taxes

Source: https://taxone.vyapar.com/help/articles/purchase-horizontal-tax-rate-multiple-duties-and-taxes

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Processing Purchase Excel with Horizontal GST Rates and Duties & Taxes](/help/articles/purchase-horizontal-tax-rate-multiple-duties-and-taxes)

[Follow the steps below:](#follow-the-steps-below-)[How to upload Excel sheet Click Here](#how-to-upload-excel-sheet-click-here)[Mapping](#mapping)[Step 1: Field Mapping](#step-1-field-mapping)[Step 2: GST Mapping (Map Your Tax Ledger)](#step-2-gst-mapping-map-your-tax-ledger-)[Step 3: Ledger Mapping](#step-3-ledger-mapping)[For Next Step Click Here](#for-next-step-click-here)

# Processing Purchase Excel with Horizontal GST Rates and Duties & Taxes

Learn to process purchase Excel sheets with horizontal GST rates and map SGST, CGST, IGST fields for smooth Suvit upload and seamless Tally integration.

---

### Follow the steps below:

![2 excel sample.png](https://strapi.suvit.io/uploads/2_excel_sample_bc9e8f3bee.png)
**A.** If you have a purchase excel sheet which looks like the image above, in which GST TAX Rate is given horizontally or in a row.

![1 sample main.png](https://strapi.suvit.io/uploads/1_sample_main_a07e151c6e.png)

* With such data, you want purchase entries like the image above.

Sheet Modification![sheet modification.png](https://strapi.suvit.io/uploads/sheet\_modification\_dc832a6393.png)

* A. In excel sheet along with the different Taxable amount there should be Individual Duties & Taxes

* B. Pick the smallest GST Tax Rate Number and add one row with the name Purchase Ledger(Enter the Purchase account Ledger Name)

\*\*Some other data should be in the Excel Sheet\*\*

* 1. Supplier Invoice Number

* 2. Invoice Date

* 3. GST number (Not Mandatory)

* 4. Party Name

* 5. Place of Supply (Not Mandatory)

* 6. Taxable Amount

* 7. Particulars-Purchase Ledger (Smallest Sales account GST rate name)

* Other things to keep in mind [Click Here](https://help.suvit.io/articles/mandatory-things-to-check-before-using-the-sales-sales-return-module)

#### How to upload Excel sheet [Click Here](https://help.suvit.io/articles/uploading-sales-sales-return-data-through-an-excel-sheet)

### Mapping

* Click on file to open *Mapping Process*

![1sales4.png](https://strapi.suvit.io/uploads/1sales4_e47be02491.png)

### **Step 1: Field Mapping**

```
Note: In this sheet you have to map **Smallest Taxable amount** in **Amount**
- As per this sheet we have mapped the GST Tax Rate 5
```

![3  mapping.png](https://strapi.suvit.io/uploads/3_mapping_c38578201f.png)

**1.** **Choose your data type**: Decide if your data has **items** or **no items**.

* For this example, we will choose **Without Item** (see the image above).

**2.** **Mapped Fields**: These are fields that the system has matched automatically from your uploaded data.

**3.** **Unmapped Fields**: These are fields not matched yet. You need to select the right Tally fields for them. *(Not all fields need to be matched.)*

**4.** **Your Sheet Header**: The headings from your Excel sheet will appear here. This helps you understand the data easily.

**5.** **Tally Fields**: These are fields matched with Tally filed. You can change them if needed.

**6.** **Your Sheet Data**: Shows the top 3 values from your Excel sheet to help you cross-check the data.

**7.** Press **Next** to go to the **GST Mapping** step.

### **Step 2: GST Mapping (Map Your Tax Ledger)**

* Here we will map the Duties & Taxes and its details.

![6 gst calculation of.png](https://strapi.suvit.io/uploads/6_gst_calculation_of_398cc636ef.png)

**8.** Change **GST Auto Calculation** settings to **No**
**9.** Select SGST Ledger name in front of SGST, similarly for CGST & IGST as shown in the above image.

* For example: here we have selected Sgst 2.5, Cgst 2.5 & Igst 5 **Ledger** as we have selected Purchase 5 in Particulars.

**10.** **Duties & Taxes**: You can select **common Duties & Taxes ledger**.

* This option is available after you click **No** in **Step 8**. You can pick the Duties & taxes (SGST/CGST/IGST) **Amount** from the Excel Sheet.
* For example: here we have selected Sgst 2.5, Cgst 2.5 & Igst 5 **amount** as we have selected Purchase 5 in Particulars.

```
**Note**: SGST, CGST, and IGST Tax Ledgers are mandatory fields that must be mapped. You can also map the round-off ledger from the below option.
```

* Go to **Next**

### **Step 3: Ledger Mapping**

![7.png](https://strapi.suvit.io/uploads/7_74af944440.png)

**11.** Select remaining TAXABLE AMOUNT in increasing order (small to big).

* First select the remaining Taxable amount and then its duties and taxes as shown in the above image.
* Maintain the same order for all other tax rates.

**12.** Click **Save & Proceed** to move to the process screen.

* This action will also save the particular format within **SUVIT** for future uploads.

#### For Next Step [Click Here](https://help.suvit.io/articles/how-do-we-process-or-push-sales-sales-return-data-to-tally)