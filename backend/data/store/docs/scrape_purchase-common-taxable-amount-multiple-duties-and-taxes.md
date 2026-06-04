# Purchase: Common Tax with Different GST in Horizontal Row

Source: https://taxone.vyapar.com/help/articles/purchase-common-taxable-amount-multiple-duties-and-taxes

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Purchase: Common Tax with Different GST in Horizontal Row](/help/articles/purchase-common-taxable-amount-multiple-duties-and-taxes)

[Instructions](#instructions)[Steps to follow](#steps-to-follow)[Sheet Modification Click Below](#sheet-modification-click-below)[How to upload Excel sheet Click Here](#how-to-upload-excel-sheet-click-here)[Mapping](#mapping)[Step 1: Field Mapping](#step-1-field-mapping)[Step 2: GST Mapping (Map Your Tax Ledger).](#step-2-gst-mapping-map-your-tax-ledger-)[Step 3: Ledger Mapping](#step-3-ledger-mapping)

# Purchase: Common Tax with Different GST in Horizontal Row

Modify and upload purchase sheets with varied tax rates using Suvit. Map smallest taxable amounts, duties, and ledgers step-by-step for accurate Tally entry.

### Instructions

![2 excel sample.png](https://strapi.suvit.io/uploads/2_excel_sample_081eced079.png)

* **A.** If you have Purchase excel sheet which looks like below image. In which Taxable amount is common for (**B**) different Duties & Taxes amount.
  ![1 sample main.png](https://strapi.suvit.io/uploads/1_sample_main_bfbc61029d.png)
* **1 & 2** Sample entry in **Tally** with such data

### Steps to follow

### Sheet Modification Click Below

--> Excel Sheet Modification![sheet modification.png](https://strapi.suvit.io/uploads/sheet\_modification\_c799141e39.png)

* A. Common Taxable Amount for each Bill

* B. In excel sheet bifurcated (separates) duties & taxes amount should be there.

* C. Add one row with name Purchase Ledger and enter \*\*Common Sales account\*\* name also known as GST Ledger which will goes to particular.

\*\*Some other data should hvae in Excel Sheet\*\*

* 1. Reference number

* 2. Invoice Date

* 3. GST number ( Not Mandatory )

* 4. Party Name

* 5. Place of Supply (Not Mandatory )

* 6. Particulars ( Smallest Sales account GST rate name )

* 7. Taxable Amount

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

![3  mapping.png](https://strapi.suvit.io/uploads/3_mapping_028f37ea10.png)

1. **Choose your data type**: Decide if your data has **items** or **no items**. For this example, we will choose **Without Item** (see the image above).
2. **Mapped Fields**: These are fields that the system has matched automatically from your uploaded data.
3. **Unmapped Fields**: These are fields not matched yet. You need to select the right Tally fields for them. *(Not all fields need to be matched.)*
4. **Your Sheet Header**: The headings from your Excel sheet will appear here. This helps you understand the data easily.
5. **Tally Fields**: These are fields matched with Tally filed. You can change them if needed.
6. **Your Sheet Data**: Shows the top 3 values from your Excel sheet to help you cross-check the data.
7. Press **Next** to go to the **GST Matching** step

### **Step 2: GST Mapping (Map Your Tax Ledger)**.

* Here we will map the Duties & Taxes and its details
  ![6 gst calculation of.png](https://strapi.suvit.io/uploads/6_gst_calculation_of_89cf8e4837.png)

8. Change **GST Auto Calculation** to NO
9. Select Duties & Taxes **ledger name** **(** If you have taken Purchase 5 then select SGST 2.5 , CGST 2.5 and IGST 5 respectively **)**
10. Select Duties & Taxes **amount** of which you have selected in **Step 9**
11. Click **Next** for 3rd Stage mapping.

```
**Note**: SGST, CGST, and IGST Tax Ledgers are mandatory fields that must be mapped. You can also map the round-off ledger from below option.
```

### **Step 3: Ledger Mapping**

![7.png](https://strapi.suvit.io/uploads/7_ae72cc620b.png)

12. Select remaining **TAXABLE AMOUNT and its DUTIES & TAXES** amount in decreasing Order (small to big).
13. Click **Save & Proceed** to move to the process screen.