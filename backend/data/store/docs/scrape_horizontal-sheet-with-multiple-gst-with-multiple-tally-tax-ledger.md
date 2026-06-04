# Horizontal Sheet with Multiple GST with Multiple tally tax ledger

Source: https://taxone.vyapar.com/help/articles/horizontal-sheet-with-multiple-gst-with-multiple-tally-tax-ledger

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Horizontal Sheet with Multiple GST with Multiple tally tax ledger](/help/articles/horizontal-sheet-with-multiple-gst-with-multiple-tally-tax-ledger)

[Step 1: Add Particulars for GST Mapping](#step-1-add-particulars-for-gst-mapping)[Step 2: Map Remaining GST Ledgers in Ledger Mapping](#step-2-map-remaining-gst-ledgers-in-ledger-mapping)[Step 3: Complete GST Mapping](#step-3-complete-gst-mapping)[Step 4: Final Mapping for Other GST Ledgers](#step-4-final-mapping-for-other-gst-ledgers)[Step 5: Save & Proceed](#step-5-save-proceed)

# Horizontal Sheet with Multiple GST with Multiple tally tax ledger

Here we will guide you to map respective tally tax ledgers in case where your data is of multiple GST rate applicability.

---

If you have the sheet containing data where multiple GST % is applicable in Horizontal format like shown in below Image:

![1Image S9.png](https://strapi.suvit.io/uploads/1_Image_S9_01df791d1a.png)

Now, if you want to consider and post tax amounts into multiple respective Tally tax ledgers as per the rates applicable, you can easily map them from the **"GST Mapping"** section and **"Ledger Mapping"**.

## How to Map GST Rates to Tally Tax Ledgers

### Step 1: Add Particulars for GST Mapping

* In the **Particulars** column of your sheet, add any one of the ledgers corresponding to the rates.
* For example, in the below sheet image, we have four GST rates applicable, including **Sales Exempt**, **Sales @ 5%**, **Sales @ 12%**, **Sales @ 18%**, and **Sales @ 28%**. In this case, we have added **Sales @ 5%** to the **Particulars** column.

![2Image S10.png](https://strapi.suvit.io/uploads/2_Image_S10_6e691979ee.png)

### Step 2: Map Remaining GST Ledgers in Ledger Mapping

* The other applicable sales tax ledgers (**Sales 12%**, **Sales 18%**, **Sales 28%**, and **Sales Exempt**) should be mapped in the **Ledger Mapping** section.
* In the **Imported File Header**, select the corresponding headings from your sheet. Then, in the **Select Ledger** dropdown, map them to the respective tax ledgers available in your Tally.
* Refer to the mapping setup below:

![3Mapping1.png](https://strapi.suvit.io/uploads/3_Mapping1_1e86a83453.png)

### Step 3: Complete GST Mapping

* In **GST Mapping**, map the required Tally GST ledger corresponding to your data. Since we are taking **Sales @ 5%** as a common entry, the remaining sales ledgers for different tax rates will be mapped in the **Ledger Mapping** section.
* Here is an example of how the mapping will appear in **GST Mapping**:

![4GST mapping.png](https://strapi.suvit.io/uploads/4_GST_mapping_6091296df0.png)

### Step 4: Final Mapping for Other GST Ledgers

* The remaining GST tax ledgers like **CGST 6%**, **SGST 6%**, **IGST 12%**, and others will be mapped in the **Ledger Mapping** section. Here’s how the mapping should look:

![5GST mapping2.png](https://strapi.suvit.io/uploads/5_GST_mapping2_bc1c1ec7b3.png)

### Step 5: Save & Proceed

* After successfully mapping the ledgers, click on **"Save & Proceed"** to continue sending the transactions to Tally.

## Conclusion

* This approach simplifies the process of mapping horizontal data Excel sheets with multiple GST tax ledgers in Suvit. By ensuring that each GST rate is mapped to the corresponding Tally tax ledger, you can efficiently manage and post your transactions in Tally with minimal errors. With Suvit’s user-friendly interface, this mapping process becomes seamless and quick, making GST filing and ledger management more efficient.

For further assistance, feel free to reach out to our support team or check out more articles in our help center.