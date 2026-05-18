# Multiple Tax Rates with SGST/CGST/IGST in Purchase

Source: https://taxone.vyapar.com/help/articles/multiple-tax-rates-with-multiple-taxes-purchase

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Multiple Tax Rates with SGST/CGST/IGST in Purchase](/help/articles/multiple-tax-rates-with-multiple-taxes-purchase)

[How to upload Excel sheet Click Here](#how-to-upload-excel-sheet-click-here)[Mapping](#mapping)[Step 1: Field Mapping](#step-1-field-mapping)[Step 2: GST Mapping (Map Your Tax Ledger).](#step-2-gst-mapping-map-your-tax-ledger-)[Step 3: Ledger Mapping](#step-3-ledger-mapping)

# Multiple Tax Rates with SGST/CGST/IGST in Purchase

Learn to map purchase bills with multiple tax rates using common Duties & Taxes ledgers in Suvit. Follow steps for Excel upload and GST ledger mapping.

If your entry resembles the image below or you need to record similar entries where each Purchase bill includes multiple **DUTIES & TAXES ledgers** with **multiple TAX RATES**, follow this guide for accurate data management.
![1 sample main.png](https://strapi.suvit.io/uploads/1_sample_main_99af6a474f.png)

Data requirement for excel sheet

![2 excel sample.png](https://strapi.suvit.io/uploads/2\_excel\_sample\_383217bafa.png)

* 1. \*\*Supplier Invoice Number\*\* (A)

* 2. \*\*Invoice Date\*\* (B)

* 3. \*\*GST number\*\* (C) (Not Mandatory)

* 4. \*\*Party Name\*\* (D)

* 5. \*\*Place of Supply\*\* (E) (Not Mandatory)

* 6. \*\*Particulars\*\* (F) (Multiple Purchase Ledger Account Name)

* 7. \*\*Taxable Amount\*\* (G)

* 8. \*\*SGST/CGST/IGST amount\*\* (H,I,J) (Required for such type of sheet)

* 9. \*\*Total Amount\*\* for cross verification (K)

* 10. Need to create three additional rows in excel sheet and name them \*\*SGST NAME\*\*, \*\*CGST NAME\*\*, and \*\*IGST NAME\*\* respectively. (L,M,N))

* 11. By using filter in \*\*GST TAX RATE\*\* or in \*\*Purchase Account name\*\*, put \*\*DUTIES & TAXES\*\* name respectively as shown in the above image. (All three fields are compulsory; if IGST is not applicable, kindly create IGST in Tally.)

* Other things to keep in mind [Click Here](https://help.suvit.io/articles/mandatory-things-to-check-before-using-purchase-purchase-return-module)

#### How to upload Excel sheet [Click Here](https://help.suvit.io/articles/uploading-sales-sales-return-data-through-an-excel-sheet)

### Mapping

* Click on file to open *Mapping Process*

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
  ![3 ledger from excel sheet.png](https://strapi.suvit.io/uploads/3_ledger_from_excel_sheet_74041018a2.png)

8. **GST Ledger from Excel Sheet** : Click to **YES** ( it will open the new menu)
9. Select SGST Ledger details in front of SGST NAME, Select CGST Ledger details in front of CGST NAME and Select IGST Ledger details in front of IGST NAME respectively
10. **Gst Auto Calculation**: If you have Defined GST TAX Rate in Tally. Keep this setting as it is.

* **A.** **Manual Calculation** If You click **NO**. You can pick the Duties & taxes(SGST/CGST/IGST) **Amount** from the Excel Sheet
* **B.** You will have the option to tick mark the SGST, CGST & IGST tax amount from the excel sheet.
  ![11 gst calculation of.png](https://strapi.suvit.io/uploads/11_gst_calculation_of_7ec243d252.png)

```
**Note**: SGST, CGST, and IGST Tax Ledgers are mandatory fields that must be mapped. You can also map the round-off ledger from below option.
```

### **Step 3: Ledger Mapping**

![5.png](https://strapi.suvit.io/uploads/3_7c6bbdda35.png)

* In this step, you can map additional fields such as, discount, freight amount, etc., by selecting the appropriate file header and ledger.

Click **Save & Proceed** to move to the process screen.  
This action will also save the particular format within SUVIT for future uploads.