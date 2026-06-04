# Multiple Tax Rate with Common SGST/CGST/IGST (Duties & Taxes)

Source: https://taxone.vyapar.com/help/articles/multiple-tax-rate-common-duties-and-taxes

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Multiple Tax Rate with Common SGST/CGST/IGST (Duties & Taxes)](/help/articles/multiple-tax-rate-common-duties-and-taxes)

[How to upload Excel sheet Click Here](#how-to-upload-excel-sheet-click-here)[Mapping](#mapping)[Step 1: Field Mapping](#step-1-field-mapping)[Step 2: GST Mapping (Map Your Tax Ledger).](#step-2-gst-mapping-map-your-tax-ledger-)[Step 3: Ledger Mapping](#step-3-ledger-mapping)

# Multiple Tax Rate with Common SGST/CGST/IGST (Duties & Taxes)

Manage sales bills with identical tax rates using the same Duties & Taxes ledger in Suvit. Learn data needs, Excel upload, and mapping for smooth workflow.

If your entries include **Multiple Tax Rates** but you want to associate them with the same **SGST/CGST/IGST** **Duties & Taxes ledger** you can handle this efficiently in Suvit.
![1 sample main.png](https://strapi.suvit.io/uploads/1_sample_main_af45d8d743.png)

Data requirement for excel sheet

![7 Excel sheet.png](https://strapi.suvit.io/uploads/7\_Excel\_sheet\_d30becf95f.png)

* 1. Reference number

* 2. Invoice Date

* 3. GST number ( Not Mandatory )

* 4. Party Name

* 5. Place of Supply (Not Mandatory )

* 6. Particulars ( Multiple Sales Ledger Account Name )

* 7. Taxable Amount

* 8. SGST/CGST/IGST amount (Only required for \*\*Manual Calculation\*\*)

* Other things to keep in mind [Click Here](https://help.suvit.io/articles/mandatory-things-to-check-before-using-the-sales-sales-return-module)

#### How to upload Excel sheet [Click Here](https://help.suvit.io/articles/uploading-sales-sales-return-data-through-an-excel-sheet)

### Mapping

* Click on file to open *Mapping Process*\*

![1sales4.png](https://strapi.suvit.io/uploads/1sales4_e47be02491.png)

### **Step 1: Field Mapping**

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
  ![9 gst mapping1.png](https://strapi.suvit.io/uploads/9_gst_mapping1_81d6ad9958.png)

8. **GST Ledger from Excel Sheet** : It will remain as it is
9. **Gst Auto Calculation**: If you have Defined GST TAX Rate in Tally. Keep this setting as it is.
10. **Duties & Taxes**: You can select **common Duties & Taxes ledger**

* **For Example:** If entire sheet belongs to 18 GST Rate You can choose **SGST, CGST, IGST** or esle **SGST 9, CGST 9, IGST 18**
* **A.** **Manual Calculation** If You click **NO**. You can pick the Duties & taxes(SGST/CGST/IGST) **Amount** from the Excel Sheet
* **B.** You will have the option to tick mark the SGST, CGST & IGST tax amount from the excel sheet.
  ![11 gst calculation of.png](https://strapi.suvit.io/uploads/11_gst_calculation_of_fbdbb13d36.png)

```
**Note**: SGST, CGST, and IGST Tax Ledgers are mandatory fields that must be mapped. You can also map the round-off ledger from below option.
```

### **Step 3: Ledger Mapping**

![5.png](https://strapi.suvit.io/uploads/3_7c6bbdda35.png)

* In this step, you can map additional fields such as, discount, freight amount, etc., by selecting the appropriate file header and ledger.

Click **Save & Proceed** to move to the process screen.  
This action will also save the particular format within SUVIT for future uploads.