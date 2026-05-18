# How to Format and Upload Choice Broker Purchase Excel Sheet in Suvit

Source: https://taxone.vyapar.com/help/articles/choice-broker-purchase-excel-upload-suvit

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[How to Format and Upload Choice Broker Purchase Excel Sheet in Suvit](/help/articles/choice-broker-purchase-excel-upload-suvit)

[🔍 Overview](#-overview)[📝 Preparing the Excel Sheet](#-preparing-the-excel-sheet)[Step 1 - Remove Unwanted Data](#step-1-remove-unwanted-data)[Step 2 - Date Formatting](#step-2-date-formatting)[Step 3 - Add Required Details](#step-3-add-required-details)[📤 Uploading the Purchase Sheet in Suvit](#-uploading-the-purchase-sheet-in-suvit)[Step 4 - Upload the Excel Sheet](#step-4-upload-the-excel-sheet)[🔄 Mapping Process](#-mapping-process)[Step 5 - Field Mapping](#step-5-field-mapping)[Step 6- GST Mapping](#step-6-gst-mapping)[Step 7 - Ledger Mapping](#step-7-ledger-mapping)[📚 What's Next?](#-what-s-next-)

# How to Format and Upload Choice Broker Purchase Excel Sheet in Suvit

Learn to format and upload your Choice Broker Purchase Excel in Suvit. This guide covers date formatting, field mapping, GST setup, and ledger mapping.

### 🔍 **Overview**

* This guide will help you format your **Choice Broker** Purchase Excel Sheet and upload it to **Suvit**

---

### 📝 **Preparing the Excel Sheet**

#### Step 1 - Remove Unwanted Data

* **Delete unnecessary data** from the **Choice Broker Excel sheet** before proceeding.

#### Step 2 - Date Formatting

![1.png](https://strapi.suvit.io/uploads/1_bcaa435da8.png)

* Select **Date Column** -> Go To **Data** -> **Text to Column**

![2.png](https://strapi.suvit.io/uploads/2_3acd73daa8.png)

* Select **Delimited** -> Click **Next**

![3.png](https://strapi.suvit.io/uploads/3_b8fca4f518.png)

* Click **Next** again

![4.png](https://strapi.suvit.io/uploads/4_032e126ebf.png)

* Select **Date** (DMY)-> Click **Finish**
* Convert the date format into **DD-MM-YYYY** using **Date Format**

#### Step 3 - Add Required Details

✅ Before saving, add:  
![5.png](https://strapi.suvit.io/uploads/5_22abd29c8d.png)

* For invoice number add **Supplier Invoice Number**
* **Party Name**: Add clients name
* **Purchase Ledger** : Add Purchase ledger name
* For example: **Purchase (Choice Broker)** ledger added in Purchase ledger column

💾 **Save the Excel Sheet**.

---

### 📤 **Uploading the Purchase Sheet in Suvit**

#### Step 4 - Upload the Excel Sheet

* **Login to** [Suvit](https://in.suvit.io/signIn).
* Click on **Explore Now** under **Data Entry Automation**.
* Select **Purchase** and click on **Bulk Upload**.
* Select and **upload the prepared Choice Broker Excel sheet**.

---

### 🔄 **Mapping Process**

#### Step 5 - Field Mapping

![6.png](https://strapi.suvit.io/uploads/6_63021386a5.png)

* Map all necessary details under **Field Mapping**.
* Click **Next**.

Here is the formatted table based on Choice broker data:

|  |  |
| --- | --- |
| **Excel Sheet Heading** | **Mapped Column in Suvit** |
| SYMBOL | Name of Item |
| QUANTITY | Quantity |
| BUY DATE | Date |
| BUY VALUE | Amount |
| Suplier invoice number | Supplier Invoice No. |
| Party Name | Party A/C Name |
| Purchase Name | Purchase Ledger |

* This table correctly maps the given fields to Suvit’s column structure while maintaining the format.

---

#### Step 6- GST Mapping

✅ **No changes required** : Changes can be done if required.

* Here we have taken **Default** Settings

![7.png](https://strapi.suvit.io/uploads/7_f348199644.png)

* **Duties and Taxes** are mandatory to map
* Click **Next**

---

#### Step 7 - Ledger Mapping

* Map other charges such as **Stamp Duty, Brokerage Charges, Expenses etc.**, if required.  
  ![9.png](https://strapi.suvit.io/uploads/9_526558b9df.png)
* Use **dropdown** -> **Search & Select** desired ledger name
* Click **Save & Proceed**.

##### Similar method can be used for Sales Entry

### 📚 What's Next?

* How to create [Stock item and Party Name](https://help.suvit.io/articles/how-to-create-a-ledger-and-stock-item-from-purchase-transaction-screen)
* To learn more about next step: [How to send data to Tally?](https://help.suvit.io/articles/purchase-process)