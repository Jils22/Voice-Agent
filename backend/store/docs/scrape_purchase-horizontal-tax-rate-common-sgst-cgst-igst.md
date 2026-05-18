# Purchase Horizontal Tax with Common SGST/CGST/IGST

Source: https://taxone.vyapar.com/help/articles/purchase-horizontal-tax-rate-common-sgst-cgst-igst

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Purchase Horizontal Tax with Common SGST/CGST/IGST](/help/articles/purchase-horizontal-tax-rate-common-sgst-cgst-igst)

[Folow the steps below:](#folow-the-steps-below-)[How to upload Excel sheet Click Here](#how-to-upload-excel-sheet-click-here)[Mapping](#mapping)[Step 1: Field Mapping](#step-1-field-mapping)[Step 2: GST Mapping (Map Your Tax Ledger).](#step-2-gst-mapping-map-your-tax-ledger-)[Step 3: Ledger Mapping](#step-3-ledger-mapping)[For Next Step Click Here](#for-next-step-click-here)

# Purchase Horizontal Tax with Common SGST/CGST/IGST

Handle purchase Excel sheets with horizontal GST rates. Learn sheet edits, field mapping, GST mapping, and ledger mapping for smooth Suvit-Tally integration

---

### Folow the steps below:

![2 excel sample.png](https://strapi.suvit.io/uploads/2_excel_sample_5898a648d5.png)
**1.** If you have purchase excel sheet which looks like above image. In which GST TAX Rate given in horizontal or in row.

![1 sample main.png](https://strapi.suvit.io/uploads/1_sample_main_8073143325.png)

* With such data you want purchase entries like above image

Sheet Modification![sheet modification.png](https://strapi.suvit.io/uploads/sheet\_modification\_0289b51de7.png)

* A. Pick the smallest GST Tax Rate Number and add one row with name Purchase Ledger

* Enter the Purchase account Ledger Name

\*\*Some other data should have in Excel Sheet\*\*

* 1. Supplier Invoice Number

* 2. Invoice Date

* 3. GST number ( Not Mandatory )

* 4. Party Name

* 5. Place of Supply (Not Mandatory )

* 6. Taxable Amount

* 7. Particulars-Purchase Ledger ( Smallest Sales account GST rate name )

* Other things to keep in mind [Click Here](https://help.suvit.io/articles/mandatory-things-to-check-before-using-purchase-purchase-return-module)

#### How to upload Excel sheet [Click Here](https://help.suvit.io/articles/uploading-sales-sales-return-data-through-an-excel-sheet)

### Mapping

* Click on file to open *Mapping Process*

![1sales4.png](https://strapi.suvit.io/uploads/1sales4_e47be02491.png)

### **Step 1: Field Mapping**

```
Note: In this sheet you have to map **Smallest Taxable amount** in **Amount**
- As per this sheet we have mapped the GST Tax Rate 5
```

![3  mapping.png](https://strapi.suvit.io/uploads/3_mapping_f66274f532.png)

1. **Choose your data type**: Decide if your data has **items** or **no items**.

* For this example, we will choose **Without Item** (see the image above).

2. **Mapped Fields**: These are fields that the system has matched automatically from your uploaded data.
3. **Unmapped Fields**: These are fields not matched yet. You need to select the right Tally fields for them. *(Not all fields need to be matched.)*
4. **Your Sheet Header**: The headings from your Excel sheet will appear here. This helps you understand the data easily.
5. **Tally Fields**: These are fields matched with Tally filed. You can change them if needed.
6. **Your Sheet Data**: Shows the top 3 values from your Excel sheet to help you cross-check the data.
7. Press **Next** to go to the **GST Mapping** step.

### **Step 2: GST Mapping (Map Your Tax Ledger)**.

* Here we will mapp the Duties & Taxes and its details
  ![4 gst mapping1.png](https://strapi.suvit.io/uploads/4_gst_mapping1_52ec3edb44.png)

8. **GST Ledger from Excel Sheet** & **GST Auto Calculation** settings will remain same(no changes).
9. Select SGST Ledger name in front of SGST, similarly for CGST & IGST as given in above image
10. **Duties & Taxes**: You can select **common Duties & Taxes ledger**

* **For Example:** If entire sheet belongs to 18 GST Rate You can choose **SGST, CGST, IGST** or else **SGST 9, CGST 9, IGST 18**
* **A.** **Manual Calculation** If You click **NO**. You can pick the Duties & taxes(SGST/CGST/IGST) **Amount** from the Excel Sheet
* **B.** You will have the option to tick mark the SGST, CGST & IGST tax amount from the excel sheet.
  ![6 gst calculation of.png](https://strapi.suvit.io/uploads/6_gst_calculation_of_b4bf40e5d1.png)

```
**Note**: SGST, CGST, and IGST Tax Ledgers are mandatory fields that must be mapped. You can also map the round-off ledger from below option.
```

### **Step 3: Ledger Mapping**

![7.png](https://strapi.suvit.io/uploads/7_91b3080c36.png)

11. Select remaining TAXABLE AMOUNT in increasing Order (small to big).
12. Click **Save & Proceed** to move to the process screen.  
    This action will also save the particular format within SUVIT for future uploads.

#### For Next Step [Click Here](https://help.suvit.io/articles/how-do-we-process-or-push-sales-sales-return-data-to-tally)