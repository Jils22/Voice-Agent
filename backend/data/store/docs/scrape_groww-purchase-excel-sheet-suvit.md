# How to Upload and Map a Groww Purchase Excel Sheet in Suvit

Source: https://taxone.vyapar.com/help/articles/groww-purchase-excel-sheet-suvit

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[How to Upload and Map a Groww Purchase Excel Sheet in Suvit](/help/articles/groww-purchase-excel-sheet-suvit)

[🔍 Overview](#-overview)[📝 Preparing the Excel Sheet](#-preparing-the-excel-sheet)[Step 1 - Remove Unwanted Data](#step-1-remove-unwanted-data)[Step 2 - Date Formatting](#step-2-date-formatting)[Step 3 - Add Required Details](#step-3-add-required-details)[📤 Uploading the Purchase Sheet in Suvit](#-uploading-the-purchase-sheet-in-suvit)[Step 4 - Upload the Excel Sheet](#step-4-upload-the-excel-sheet)[Step 5 - Enable Order Number (If Required)](#step-5-enable-order-number-if-required-)[🔄 Mapping Process](#-mapping-process)[Step 6 - Field Mapping](#step-6-field-mapping)[Step 7 - GST Mapping](#step-7-gst-mapping)[Step 8 - Ledger Mapping](#step-8-ledger-mapping)[📚 What's Next?](#-what-s-next-)

# How to Upload and Map a Groww Purchase Excel Sheet in Suvit

Learn to format, map, and upload your Groww Purchase Excel in Suvit. This guide covers data cleanup, date formatting, field mapping, and order number setup.

### 🔍 **Overview**

* This guide will help you format your **Groww** Purchase Excel Sheet and upload it to **Suvit** including mapping the **Order Number**

---

### 📝 **Preparing the Excel Sheet**

#### Step 1 - Remove Unwanted Data

![1.png](https://strapi.suvit.io/uploads/1_f8f96c3848.png)

* **Delete unnecessary data** from the **Groww Excel sheet** before proceeding.

#### Step 2 - Date Formatting

![2.png](https://strapi.suvit.io/uploads/2_bddfc95e80.png)

* Select **Date Column** -> Go To **Data** -> **Text to Column**

![3.png](https://strapi.suvit.io/uploads/3_ce51cd1ea7.png)

* Select **Fixed Width** -> Click **Next**

![4.png](https://strapi.suvit.io/uploads/4_c2af63b9f1.png)

* Click to **Divide the Data** as per the image -> Click **Next**

![5.png](https://strapi.suvit.io/uploads/5_1e9d1f191f.png)

* Select **Date** -> Click **Finish**

#### Step 3 - Add Required Details

✅ Before saving, add:  
![6.png](https://strapi.suvit.io/uploads/6_a7e9884e51.png)

* **Party Name**: Add clients name
* **Purchase Ledger** : Add Purchase ledger name
* For example: Purchase (Groww) ledger added in Purchase ledger coulmn

💾 **Save the Excel Sheet**.

---

### 📤 **Uploading the Purchase Sheet in Suvit**

#### Step 4 - Upload the Excel Sheet

* **Login to** [Suvit](https://in.suvit.io/signIn).
* Click on **Explore Now** under **Data Entry Automation**.
* Select **Purchase** and click on **Bulk Upload**.
* Select and **upload the prepared Groww Excel sheet**.

---

#### Step 5 - Enable Order Number (If Required)

* Open the **Purchase Sheet** in Suvit.

![7.png](https://strapi.suvit.io/uploads/7_7a1d530c94.png)

* Go to **Configuration** → **Order Details** -> Enable **Order Number**
* And **Save** the settings

---

### 🔄 **Mapping Process**

#### Step 6 - Field Mapping

* Map all necessary details under **Field Mapping**.

![8.png](https://strapi.suvit.io/uploads/8_dc10b6ca72.png)

* Click **Next**.

Here is the formatted table based on Groww data:

|  |  |
| --- | --- |
| **Excel Sheet Heading** | **Mapped Column in Suvit** |
| Stock name | Name of Item |
| ISIN | Supplier Invoice No. |
| Type | Purchase Ledger |
| Quantity | Quantity |
| Price | Rate |
| Exchange Order Id | Order No(s) |
| Execution date and time | Date |
| Party Name | Party A/C Name |

* This table correctly maps the given fields to Suvit’s column structure while maintaining the format.

---

#### Step 7 - GST Mapping

✅ **No changes required** Changes can be done if required.

* Here we have taken **Default** Settings

![9.png](https://strapi.suvit.io/uploads/9_6695e93c65.png)

* **Duties and Taxes** are mandatory to map
* Click **Next**

---

#### Step 8 - Ledger Mapping

* Map other charges such as **Stamp Duty, Brokerage Charges, etc.**, if required.  
  ![10.png](https://strapi.suvit.io/uploads/10_9d00257bb5.png)
* Use **dropdown** -> **Search & Select** desired ledger name
* Click **Save & Proceed**.

---

✅ **You have successfully uploaded the Groww Purchase Excel Sheet with Order Number & Order Date!** 🎉

### 📚 What's Next?

* How to create [Stock item and Party Name](https://help.suvit.io/articles/how-to-create-a-ledger-and-stock-item-from-purchase-transaction-screen)
* To learn more about next step: [How to send data to Tally?](https://help.suvit.io/articles/purchase-process)