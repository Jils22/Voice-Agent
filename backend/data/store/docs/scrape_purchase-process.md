# How do we process or push Purchase/Purchase return data to Tally

Source: https://taxone.vyapar.com/help/articles/purchase-process

[All Collection](/help)[Purchase and Purchase Return](/help/collections/purchase-and-purchase-return)[How do we process or push Purchase/Purchase return data to Tally](/help/articles/purchase-process)

[Save & Send Data to Tally](#save-send-data-to-tally)[Progress Tracking](#progress-tracking)[How to Select Mismatched Data and General Filters](#how-to-select-mismatched-data-and-general-filters)[Processing Screen (Purchase Transaction Screen)](#processing-screen-purchase-transaction-screen-)[Error Resolution for Ledger Mismatch](#error-resolution-for-ledger-mismatch)[Step 1 : Check Existing Ledgers](#step-1-check-existing-ledgers)[Step 2 : Create Missing Ledgers](#step-2-create-missing-ledgers)[General Filters](#general-filters)[Bulk Operations](#bulk-operations)[Step 1 : Update Bulk Records](#step-1-update-bulk-records)[Step 2 : Use Bulk Selection Tools](#step-2-use-bulk-selection-tools)[Step 3 : Cross-Check and Verify](#step-3-cross-check-and-verify)[You may find this useful:](#you-may-find-this-useful-)

# How do we process or push Purchase/Purchase return data to Tally

After mapping the purchase data, the next screen will display it in an Excel-like format, allowing you to review all details.

---

### Save & Send Data to Tally

![1 i mg.png](https://strapi.suvit.io/uploads/1_i_mg_8aadf56854.png)

* **A**→ Select your Purchase Transaction (All or Individually)
* **B**→ Click on **Save**
* **C**→ Click on **Send to Tally** button to send the purchase data into Tally.

```
**Instruction**:Ensure all transactions are properly filled, and caution triangles are cleared before proceeding.
```

![2 img.png](https://strapi.suvit.io/uploads/2_img_e2fba2d252.png)

* **D**→ Click on **OK** for the confirmation.

```
**Warning**:Only selected and saved purchase data will be pushed to Tally. Remaining entries can be sent later.
```

#### Progress Tracking

\*\*Sending Progress Tracking Data to Tally\*\*

\*\*1\*\* → \*\*Gray Stage\*\* (1st Stage)

* It indicates the process has been initiated

![1.1 img.png](https://strapi.suvit.io/uploads/1\_1\_img\_5eeaf4fc0e.png)

\*\*2\*\* → \*\*Orange Stage\*\* (2nd Stage)

![1.2 img.png](https://strapi.suvit.io/uploads/1\_2\_img\_19cdd31ea7.png)

* It indicates the process has started

\*\*3\*\* → \*\*Green Stage\*\* (3rd Stage)

![1.3 img.png](https://strapi.suvit.io/uploads/1\_3\_img\_1b4b7effe5.png)

* It indicates that the purchase data has been successfully sent to Tally.

### How to Select Mismatched Data and General Filters

#### Processing Screen (Purchase Transaction Screen)

![3 img.png](https://strapi.suvit.io/uploads/3_img_facde9f25c.png)

* The process screen will look like the above image.

\*\*Check details here\*\*

\*\*1\*\* → \*\*Bulk Selection\*\*: It will help you select purchase transactions one by one or in bulk.

\*\*2\*\* → \*\*Update Bulk Records\*\*: Used to change or select specific data within the Purchase Transaction screen.

\*\*3\*\* → \*\*Reference No\*\*: As per the Excel sheet, the reference will be displayed here.

\*\*4\*\* → \*\*Voucher Type\*\*: By default, the Purchase voucher type will be selected. It can be changed as required.

\*\*5\*\* → \*\*Supplier Name\*\*: Name of the supplier will be displayed here.

\*\*6\*\* → \*\*GST No\*\*: It will show as per the supplier details.

\*\*7\*\* → \*\*Place of Supply\*\*: If you have selected in mapping, or else it will display according to the dataset in Tally.

\*\*8\*\* → \*\*Particulars\*\*: It will show Purchase Account.

\*\*9\*\* → \*\*Warning Triangle\*\*: Indicates missing details due to spelling mistakes or a new supplier name.

\*\*10\*\* → \*\*Other Details\*\*: Data in orange indicates unselected fields.

```
**Note**:Words in Blue represent selected ones, while words in Orange indicate unselected or not yet created in Tally.
```

---

### Error Resolution for Ledger Mismatch

* If you encounter ledger mismatches while pushing purchase data to Tally, follow these steps:

#### Step 1 : Check Existing Ledgers

![4 img.png](https://strapi.suvit.io/uploads/4_img_886cb0f563.png)

* **Select** the records in bulk.

![5 img.png](https://strapi.suvit.io/uploads/5_img_749cc56e55.png)

* Use **Bulk Selection** to update and correct these entries.

#### Step 2 : Create Missing Ledgers

![6 img.png](https://strapi.suvit.io/uploads/6_img_b6702807ad.png)

* If the ledgers are missing in Tally, create them instantly by clicking the **"+" button** next to the supplier name.
* For detailed steps, [Click Here](https://help.suvit.io/articles/bulk-party-creation-sales-purchase#step-2-plus-icon).

---

### **General Filters**

![7 img.png](https://strapi.suvit.io/uploads/7_img_735f02772f.png)

* The purchase transaction screen offers various filters to efficiently manage data. You can filter records to **Hide Tally-sent data, Blank entries, Saved records, Failed records, and also sort by Date** [Learn More](https://help.suvit.io/articles/how-to-use-general-filters-in-sales-purchase-sales-return-and-purchase-return).

---

### **Bulk Operations**

#### **Step 1 : Update Bulk Records**

![8 img.png](https://strapi.suvit.io/uploads/8_img_3d517d8eab.png)

* Use **Bulk Update** to modify **Voucher Type, Supplier A/c Name,** and **Particulars (Purchase Account Ledger).**

#### **Step 2 : Use Bulk Selection Tools**

![9 img.png](https://strapi.suvit.io/uploads/9_img_d2cbd01f8a.png)

* Bulk operations help with **searching, filtering voucher types**, and **selecting purchase account ledgers**.
* You can select multiple records for quick actions like filtering, updating, or pushing purchase data to Tally.

#### **Step 3 : Cross-Check and Verify**

![10 img.png](https://strapi.suvit.io/uploads/10_img_d5c52fd41a.png)

* Search for **Bill numbers** or **specific supplier names**.
* Verify **GST numbers** and the **Place of supply** for accuracy.

#### You may find this useful:

* [Learn more](https://help.suvit.io/articles/how-to-create-a-ledger-and-stock-item-from-purchase-transaction-screen) about creating ledgers and stock items from the Purchase Transaction Screen.