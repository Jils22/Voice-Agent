# Single GST Common Tax Ledgers

Source: https://taxone.vyapar.com/help/articles/single-gst-common-tax-ledgers

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Single GST Common Tax Ledgers](/help/articles/single-gst-common-tax-ledgers)

# Single GST Common Tax Ledgers

If single GST applies and common GST ledgers like SGST, CGST & IGST are used in Tally, follow this article to process such data correctly in Suvit.

---

## Single GST Common Tax Ledgers

If you have the sheet containing data where single GST % is applicable. Like below Image:

![1Image S1_Pending.png](https://strapi.suvit.io/uploads/1_Image_S1_Pending_f6c31f9e3f.png)

As you upload the sheet and click on "Complete", the following mapping screen will appear. Suvit will automatically map fields and rest will be shown in unmapped. You need to cross check once if the auto mapping was correctly done as per your need and make required changes.

![2Field mapping.png](https://strapi.suvit.io/uploads/2_Field_mapping_da68f7b723.png)

In GST mapping, you need to map the required tally GST ledgers as per your data available. Refer below Image in case you require the GST Calculation automatic. **The GST % must be set in your Sales ledger or Stock item in tally, only then it will be automatically calculated on the amount you have selected in "Fields mapping".**

![3Common GST.png](https://strapi.suvit.io/uploads/3_Common_GST_a5c1068489.png)

If you require GST amount as per mentioned in your excel sheet, please refer below screenshot, the "GST Auto Calculation" must be selected as NO and a new section will get open as highlighted in below image:

![4Common GST as per excel.png](https://strapi.suvit.io/uploads/4_Common_GST_as_per_excel_bba947e69e.png)

As you click on Next, the "Ledger Mapping" section will open and if you have any additional ledgers to be mapped apart from the GST ledgers, kindly select it in here, refer below image for understanding:

![5Ledger Mapping.png](https://strapi.suvit.io/uploads/5_Ledger_Mapping_7d0de030ae.png)

After completing, click on "Save & Proceed", the transaction screen with your data will appear. See if there are any unselected fields, make changes accordingly and save the data records & send to tally.