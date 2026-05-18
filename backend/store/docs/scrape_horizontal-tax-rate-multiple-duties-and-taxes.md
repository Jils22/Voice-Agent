# Horizontal Tax Rate with Multiple SGST/CGST/IGST (Duties & Taxes)

Source: https://taxone.vyapar.com/help/articles/horizontal-tax-rate-multiple-duties-and-taxes

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Horizontal Tax Rate with Multiple SGST/CGST/IGST (Duties & Taxes)](/help/articles/horizontal-tax-rate-multiple-duties-and-taxes)

[Horizontal Tax Rate with Multiple SGST/CGST/IGST (Duties & Taxes)](#horizontal-tax-rate-with-multiple-sgst-cgst-igst-duties-taxes-)[Sheet Modification Click Below](#sheet-modification-click-below)[How to upload Excel sheet Click Here](#how-to-upload-excel-sheet-click-here)[Mapping](#mapping)[Step 1: Field Mapping](#step-1-field-mapping)[Step 2: GST Mapping (Map Your Tax Ledger).](#step-2-gst-mapping-map-your-tax-ledger-)[Step 3: Ledger Mapping](#step-3-ledger-mapping)

# Horizontal Tax Rate with Multiple SGST/CGST/IGST (Duties & Taxes)

Learn to handle sales entries with horizontal GST rates and split Duties & Taxes. Follow steps for Excel edits, upload, and mapping SGST, CGST, IGST ledgers.

### Horizontal Tax Rate with Multiple SGST/CGST/IGST (Duties & Taxes)

**A.** If you have sales excel sheet which looks like below image. In which GST TAX Rate given in horizontal order along with bifurcated Duties & Tax amount as shown in below image
![1 sample excel.png](https://strapi.suvit.io/uploads/1_sample_excel_37ca106f64.png)
**1.** With such data you want sales entries like below image
![1 sample.png](https://strapi.suvit.io/uploads/1_sample_485c3ab747.png)

### Sheet Modification Click Below

--> Excel Sheet Modification![3 sheet modification.png](https://strapi.suvit.io/uploads/3\_sheet\_modification\_9c6b1ac54e.png)

* A. In excel sheet bifurcated (sepratees) duties & taxes amount should be there.

* B. Pick the smallest GST Tax Rate Number and add one row with name Sales/Ledger and enter Sales account name also known as GST Ledger

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

* Here we will map the Duties & Taxes and its details
  ![4 gst mapping.png](https://strapi.suvit.io/uploads/4_gst_mapping_974c77b3a7.png)

8. Change **GST Auto Calculation** to NO
9. Select Duties & Taxes **ledger name** **(** If you have taken SALES GST 5 then select SGST 2.5 , CGST 2.5 and IGST 5 respectively **)**
10. Select Duties & Taxes **amount** of which you have selected in **Step 9**
11. Click **Next** for 3rd Stage mapping.

```
**Note**: SGST, CGST, and IGST Tax Ledgers are mandatory fields that must be mapped. You can also map the round-off ledger from below option.
```

### **Step 3: Ledger Mapping**

![5 other ledger.png](https://strapi.suvit.io/uploads/5_other_ledger_d94ea24f2d.png)

12. Select remaining **TAXABLE AMOUNT and its DUTIES & TAXES** amount in decreasing Order (small to big).
13. Click **Save & Proceed** to move to the process screen.