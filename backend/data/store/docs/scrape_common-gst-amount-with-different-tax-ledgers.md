# Common GST amount with different Tax ledgers

Source: https://taxone.vyapar.com/help/articles/common-gst-amount-with-different-tax-ledgers

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Common GST amount with different Tax ledgers](/help/articles/common-gst-amount-with-different-tax-ledgers)

[Common GST Amount with Different Tax Ledgers](#common-gst-amount-with-different-tax-ledgers)[Sample Entry:](#sample-entry-)[Step 1: Add Sales/Purchase Account Ledger Name](#step-1-add-sales-purchase-account-ledger-name)[Step 2: Map the Sales/Purchase Account Ledger as Particulars](#step-2-map-the-sales-purchase-account-ledger-as-particulars)[Step 3: Select "No" for GST Auto Calculation](#step-3-select-no-for-gst-auto-calculation)[Step 4: Select Duties and Tax Ledgers](#step-4-select-duties-and-tax-ledgers)[Step 5: Select Amounts for the Respective Duties and Tax Ledgers](#step-5-select-amounts-for-the-respective-duties-and-tax-ledgers)[Step 6-a: Go to Ledger Mapping](#step-6-a-go-to-ledger-mapping)[Step 9-a: Click on "Save & Proceed"](#step-9-a-click-on-save-proceed-)[Step 9-b: Transfer Data to Tally](#step-9-b-transfer-data-to-tally)

# Common GST amount with different Tax ledgers

If your data has a common taxable amount but GST is posted to rate-wise ledgers, this article guides you through handling it accurately in Suvit.

### Common GST Amount with Different Tax Ledgers

In this guide, we will show you how to map a common GST amount with different tax ledgers. For example, if the total taxable amount is **1000**, and the GST amounts are as follows:

* **SGST 2.5%** = **12.5**
* **CGST 2.5%** = **12.5**
* **SGST 9%** = **45**
* **CGST 9%** = **45**

#### Sample Entry:

![1TALLY ENTRY.jpg](https://strapi.suvit.io/uploads/1_TALLY_ENTRY_7f6dc49cf9.jpg)

Below is the sample data you might have in your Excel sheet:
![2common taxable multi gst.jpg](https://strapi.suvit.io/uploads/2common_taxable_multi_gst_4f335b7883.jpg)

#### Step 1: Add Sales/Purchase Account Ledger Name

While preparing the Excel sheet, you need to add a row for the **Sales Account** or **Purchase Account** ledger name as shown below:

![3sales ledger.jpg](https://strapi.suvit.io/uploads/3sales_ledger_eb23a9faa0.jpg)

#### Step 2: Map the Sales/Purchase Account Ledger as Particulars

Map the **Sales Account** or **Purchase Account** ledger as **Particulars** in the mapping section, as shown below:

![4mapping2.png](https://strapi.suvit.io/uploads/4mapping2_03ea085dfb.png)

#### Step 3: Select "No" for GST Auto Calculation

In the GST Mapping section, **select "NO"** for GST auto calculation:

![5gst mapping3.png](https://strapi.suvit.io/uploads/5gst_mapping3_c24f0d544e.png)

#### Step 4: Select Duties and Tax Ledgers

Select the appropriate **Duties and Tax ledgers** as shown in the image below:

![6mapping gst.png](https://strapi.suvit.io/uploads/6mapping_gst_2732c28f43.png)

#### Step 5: Select Amounts for the Respective Duties and Tax Ledgers

Then, select the amounts for the respective **Duties and Tax ledgers** that correspond to the values provided in your Excel sheet:

![7mapping gst 1.png](https://strapi.suvit.io/uploads/7mapping_gst_1_d53d392a81.png)

#### Step 6-a: Go to Ledger Mapping

Now, press **"Next"** from the bottom right to go to **"Ledger Mapping"**, where the remaining column headers from your Excel sheet will appear. Simply select the respective ledgers for the headers, so the amounts will reflect correctly in your Tally account.

![8mapping gst 2.png](https://strapi.suvit.io/uploads/8mapping_gst_2_e22cab9945.png)

**After successfully assigning the correct ledgers, your screen will look like this:**

![9mapping gst 3.png](https://strapi.suvit.io/uploads/9mapping_gst_3_f560118974.png)

#### Step 9-a: Click on "Save & Proceed"

Once you have mapped the GST amounts and ledgers correctly, click on **"Save & Proceed"**.

#### Step 9-b: Transfer Data to Tally

After transferring the data to Tally successfully, your entry will appear in Tally as shown below:

![10sample entry.jpg](https://strapi.suvit.io/uploads/10sample_entry_f50d45c44a.jpg)