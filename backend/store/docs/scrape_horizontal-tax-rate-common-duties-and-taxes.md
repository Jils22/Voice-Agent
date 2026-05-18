# Horizontal Tax Rate with Common SGST/CGST/IGST (Duties & Taxes)

Source: https://taxone.vyapar.com/help/articles/horizontal-tax-rate-common-duties-and-taxes

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Horizontal Tax Rate with Common SGST/CGST/IGST (Duties & Taxes)](/help/articles/horizontal-tax-rate-common-duties-and-taxes)

[Horizontal Tax Rate with Common SGST/CGST/IGST (Duties & Taxes)](#horizontal-tax-rate-with-common-sgst-cgst-igst-duties-taxes-)[How to upload Excel sheet Click Here](#how-to-upload-excel-sheet-click-here)[Mapping](#mapping)[Step 1: Field Mapping](#step-1-field-mapping)[Step 2: GST Mapping (Map Your Tax Ledger).](#step-2-gst-mapping-map-your-tax-ledger-)[Step 3: Ledger Mapping](#step-3-ledger-mapping)

# Horizontal Tax Rate with Common SGST/CGST/IGST (Duties & Taxes)

Handle sales entries with horizontal GST rates in Suvit. Learn to modify your Excel sheet, upload it, and map fields, GST ledgers, and related data accurately.

### Horizontal Tax Rate with Common SGST/CGST/IGST (Duties & Taxes)

**1.** If you have sales excel sheet which looks like below image. In which GST TAX Rate given in horizontal or in row as shown in below image
![1 sample excel.png](https://strapi.suvit.io/uploads/1_sample_excel_4e061283a2.png)
**2** With such data you want sales entries like below image
![2 sample entry.png](https://strapi.suvit.io/uploads/2_sample_entry_22c03b3d92.png)

Sheet Modification![3 sheet modification.png](https://strapi.suvit.io/uploads/3\_sheet\_modification\_e59b6e48d7.png)

* 1. Pick the smallest GST Tax Rate Number and add one row with name Sales/Ledger

* 1.1 Enter the Sales account Ledger Name

\*\*Some other data should hvae in Excel Sheet\*\*

* 2. Reference number

* 3. Invoice Date

* 4. GST number ( Not Mandatory )

* 5. Party Name

* 6. Place of Supply (Not Mandatory )

* 7. Particulars ( Smallest Sales account GST rate name )

* 8. Taxable Amount

* Other things to keep in mind [Click Here](https://help.suvit.io/articles/mandatory-things-to-check-before-using-the-sales-sales-return-module)

#### How to upload Excel sheet [Click Here](https://help.suvit.io/articles/uploading-sales-sales-return-data-through-an-excel-sheet)

### Mapping

* Click on file to open *Mapping Process*\*

![1sales4.png](https://strapi.suvit.io/uploads/1sales4_e47be02491.png)

### **Step 1: Field Mapping**

```
Note: In this sheet you have to map **Smallest Taxable amount** in **Amount**
- As per this sheet we have mapped the GST Tax Rate 5
```

![8 mapping.png](https://strapi.suvit.io/uploads/8_mapping_13492bd8c8.png)

1. **Choose your data type**: Decide if your data has **items** or **no items**. For this example, we will choose **Without Item** (see the image above).
2. **Mapped Fields**: These are fields that the system has matched automatically from your uploaded data.
3. **Unmapped Fields**: These are fields not matched yet. You need to select the right Tally fields for them. *(Not all fields need to be matched.)*
4. **Your Sheet Header**: The headings from your Excel sheet will appear here. This helps you understand the data easily.
5. **Tally Fields**: These are fields matched with Tally filed. You can change them if needed.
6. **Your Sheet Data**: Shows the top 3 values from your Excel sheet to help you cross-check the data.
7. Press **Next** to go to the **GST Mapping** step.

### **Step 2: GST Mapping (Map Your Tax Ledger)**.

* Here we will mapp the Duties & Taxes and its details
  ![4 gst mapping1.png](https://strapi.suvit.io/uploads/4_gst_mapping1_ec416d30cd.png)

8. **GST Ledger from Excel Sheet** & **GST Auto Calculation** settings will remain same(no changes).
9. Select SGST Ledger name in front of SGST, similarly for CGST & IGST as given in above image
10. Click Next for 3rd Stage Mapping.

```
**Note**: SGST, CGST, and IGST Tax Ledgers are mandatory fields that must be mapped. You can also map the round-off ledger from below option.
```

### **Step 3: Ledger Mapping**

![5 other ledger.png](https://strapi.suvit.io/uploads/5_other_ledger_9803166614.png)

11. Select remaining TAXABLE AMOUNT in increasing Order (small to big).
12. Click **Save & Proceed** to move to the process screen.  
    This action will also save the particular format within SUVIT for future uploads.