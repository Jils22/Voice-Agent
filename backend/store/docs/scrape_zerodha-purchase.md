# ⚡Quick & Easy: Upload Your Zerodha Purchase (tradebook) Sheet to Suvit

Source: https://taxone.vyapar.com/help/articles/zerodha-purchase

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[⚡Quick & Easy: Upload Your Zerodha Purchase (tradebook) Sheet to Suvit](/help/articles/zerodha-purchase)

[🔍 Overview](#-overview)[📝 Preparing the Excel Sheet](#-preparing-the-excel-sheet)[Step 1 - Remove Unwanted Data](#step-1-remove-unwanted-data)[Step 2 - Change the Date Format of Trade Date (DD/MM/YYYY)](#step-2-change-the-date-format-of-trade-date-dd-mm-yyyy-)[Step 3 - Change the Format of Order Execution Time (DD/MM/YYYY)](#step-3-change-the-format-of-order-execution-time-dd-mm-yyyy-)[Step 4 - Add Required Details](#step-4-add-required-details)[📤 Uploading the Purchase Sheet in Suvit](#-uploading-the-purchase-sheet-in-suvit)[Step 5 - Upload the Excel Sheet](#step-5-upload-the-excel-sheet)[Step 6 - Enable Order Number & Order Date (If Required)](#step-6-enable-order-number-order-date-if-required-)[🔄 Mapping Process](#-mapping-process)[Step 7 - Field Mapping](#step-7-field-mapping)[Step 8 - GST Mapping](#step-8-gst-mapping)[Step 9 - Ledger Mapping](#step-9-ledger-mapping)[📚 What's Next?](#-what-s-next-)

# ⚡Quick & Easy: Upload Your Zerodha Purchase (tradebook) Sheet to Suvit

Learn how to process the Zerodha (tradebook) Stock/Share Excel purchase sheet in Suvit, including Sheet Preparation, Uploading to Suvit & Mapping Data

### 🔍 **Overview**

This guide will help you format your **Zerodha Purchase Excel Sheet** and upload it to **Suvit** including mapping the **Order Number** and **Order Date** fields.

📝 **Notes**

```
Make sure there is only purchase (buy) data in excel sheet. Sales (sell) data can be removed using filter)
```

---

### 📝 **Preparing the Excel Sheet**

#### Step 1 - Remove Unwanted Data

🗑 **Delete unnecessary data** from the **Zerodha Excel sheet** before proceeding.

#### Step 2 - Change the Date Format of **Trade Date** (DD/MM/YYYY)

* 📅 **Modify the Trade Date Format** using the steps below:

![2.png](https://strapi.suvit.io/uploads/2_cdb969154d.png)

* Select the **Trade Date** column. Navigate to **Data** → **Text to column**

![3.png](https://strapi.suvit.io/uploads/3_39c7dfc2b9.png)

* Select **Delimited** → **Next**

![5.png](https://strapi.suvit.io/uploads/5_3b0c07fdef.png)

* Choose **DMY (Day/Month/Year)** as the format and click **Finish**.

---

#### Step 3 - Change the Format of **Order Execution Time** (DD/MM/YYYY)

⏳ **Modify the Order Execution Time Format** using the steps below:

* Select the **Order Execution Time** column.

![6.png](https://strapi.suvit.io/uploads/6_fc0b734461.png)

* Navigate to **Data** → **Text to Column**

![7.png](https://strapi.suvit.io/uploads/7_3fb7dd87fb.png)

* Select **Fixed Width** → **Next**.

![8.png](https://strapi.suvit.io/uploads/8_067113fa50.png)

* Select **Separator** and format as **DMY (Day/Month/Year)**.

![9.png](https://strapi.suvit.io/uploads/9_22c182437d.png)

* Choose **DMY (Day/Month/Year)** as the format and click **Finish**.

---

#### Step 4 - Add Required Details

✅ Before saving, add:

* **Party Name**
* **Purchase Ledger**

![10.png](https://strapi.suvit.io/uploads/10_c9dd061d32.png)

💾 **Save the Excel Sheet**.

---

### 📤 **Uploading the Purchase Sheet in Suvit**

#### Step 5 - Upload the Excel Sheet

* **Login to** [Suvit](https://in.suvit.io/signIn).
* Click on **Explore Now** under **Data Entry Automation**.
* Select **Purchase** and click on **Bulk Upload**.
* Select and **upload the prepared Zerodha Excel sheet**.

---

#### Step 6 - Enable Order Number & Order Date (If Required)

* If needed, enable **Order Number** and **Order Date** under **Order Details**:
* Open the **Purchase Sheet** in Suvit.

![11.png](https://strapi.suvit.io/uploads/11_2ca4fc6cae.png)

* Go to **Configuration** → Enable **Order Number** and **Order Date**.

---

### 🔄 **Mapping Process**

#### Step 7 - Field Mapping

* Map all necessary details under **Field Mapping**.

![12.png](https://strapi.suvit.io/uploads/12_1a5a3ae95f.png)

* Click **Next**.

---

#### Step 8 - GST Mapping

✅ **No changes required** Changes can be done if required. Click **Next**.

![13.png](https://strapi.suvit.io/uploads/13_44ddd805c8.png)

---

#### Step 9 - Ledger Mapping

* Map other charges such as **Purchase Charges, Delivery Charges, etc.**, if required.

![14.png](https://strapi.suvit.io/uploads/14_594fdc9aad.png)

* Click **Save & Proceed**.

---

✅ **You have successfully uploaded the Zerodha Purchase Excel Sheet with Order Number & Order Date!** 🎉

### 📚 What's Next?

* How to create [Stock item and Party Name](https://help.suvit.io/articles/how-to-create-a-ledger-and-stock-item-from-purchase-transaction-screen)
* To learn more about next step: [How to send data to Tally?](https://help.suvit.io/articles/purchase-process)