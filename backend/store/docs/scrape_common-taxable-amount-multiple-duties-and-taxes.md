# Common Taxable Amount with Multiple Horizontal GST Ledgers

Source: https://taxone.vyapar.com/help/articles/common-taxable-amount-multiple-duties-and-taxes

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Common Taxable Amount with Multiple Horizontal GST Ledgers](/help/articles/common-taxable-amount-multiple-duties-and-taxes)

[Instructions](#instructions)[Steps to follow](#steps-to-follow)[Sheet Modification Click Below](#sheet-modification-click-below)[How to upload Excel sheet Click Here](#how-to-upload-excel-sheet-click-here)[Mapping](#mapping)[Step 1: Field Mapping](#step-1-field-mapping)[Step 2: GST Mapping (Map Your Tax Ledger).](#step-2-gst-mapping-map-your-tax-ledger-)[Step 3: Ledger Mapping](#step-3-ledger-mapping)

# Common Taxable Amount with Multiple Horizontal GST Ledgers

Import sales data from Excel to Tally via Suvit with shared taxable amounts and separate taxes like SGST and CGST. Modify, upload, and map key details.

---

### Instructions

![1 sample excel.png](https://strapi.suvit.io/uploads/1_sample_excel_537b291cf9.png)

* **A.** If you have sales excel sheet which looks like below image. In which Taxable amount is common for (**B**) different Duties & Taxes amount.

![2 smaple entry.png](https://strapi.suvit.io/uploads/2_smaple_entry_bd31f6f469.png)

* **1 & 2** Sample entry in **Tally** with such data

### Steps to follow

#### Sheet Modification Click Below

--> Excel Sheet Modification![3 sheet modifictation.png](https://strapi.suvit.io/uploads/3\_sheet\_modifictation\_f281f1c8a5.png)

* A. Common Taxable Amount for each Bill

* B. In excel sheet bifurcated (separates) duties & taxes amount should be there.

* C. Add one row with name Sales/Ledger and enter \*\*Common Sales account\*\* name also known as GST Ledger which will goes to particular.

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

* Click on file to open **Mapping Process**

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
7. Press **Next** to go to the **GST Matching** step

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

![5 other ledger.png](https://strapi.suvit.io/uploads/5_other_ledger_74e0a41553.png)

12. Select remaining **TAXABLE AMOUNT and its DUTIES & TAXES** amount in decreasing Order (small to big).
13. Click **Save & Proceed** to move to the process screen.