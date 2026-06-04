# How to Select Different Voucher Types in Suvit

Source: https://taxone.vyapar.com/help/articles/select-different-voucher-type

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[How to Select Different Voucher Types in Suvit](/help/articles/select-different-voucher-type)

[There are three Method to select Voucher type](#there-are-three-method-to-select-voucher-type)[Method 1: Voucher type in excel sheet](#method-1-voucher-type-in-excel-sheet)[Method 2: Change Voucher Type One-by-one](#method-2-change-voucher-type-one-by-one)[Method 3: Bulk Update](#method-3-bulk-update)[Notes](#notes)[You may find this useful](#you-may-find-this-useful)

# How to Select Different Voucher Types in Suvit

Learn to select the right voucher type in Suvit for accurate data processing. This guide helps you choose based on your specific accounting requirements.

##### In Suvit, selecting the correct **Voucher Type** is essential for accurate data processing in Tally.

### There are three Method to select Voucher type

* By **Default** Suvit will select the standard voucher type of tally for **Sales-Sales Return** & **Purchase-Purchase Return** & in **Journal**.

#### Method 1: Voucher type in excel sheet

![1.png](https://strapi.suvit.io/uploads/1_a8937e6ad2.png)

* **Add** one **Column** name **Voucher Type** in **Excel Sheet**
* Go to → **Gateway of Tally** → **Alter** → **Voucher Type** - **Copy** the **Voucher Type Name**
* **Paste** into the **column** added in **excel sheet**
* **Upload excel sheet** in Suvit

![2.png](https://strapi.suvit.io/uploads/2_3b9189c2b2.png)

* In **mapping screen** → **Map** the **Voucher Type** as shown in above image.

#### Method 2: Change Voucher Type One-by-one

![3.png](https://strapi.suvit.io/uploads/3_2c48625e3c.png)

* In **Transaction Screen** → **Select Voucher type** → **search and select** the required **Voucher Type**

#### Method 3: Bulk Update

![4.png](https://strapi.suvit.io/uploads/4_e1da0e8d06.png)

* **1** → First **Select Transaction**
* **2** → Select **Voucher Type** under **Update Bulk Records**
* **3** → Select required **Voucher type** from the **Drop Down Menu**

### Notes

* The voucher type should match the nature of the transaction to prevent errors in Tally.
* Incorrect voucher selection may lead to mismatched entries or data processing failures.
* **Voucher type not available?** → Ensure the correct module is selected.
* **Data mismatch in Tally?** → Verify that the voucher type aligns with the transaction>

#### You may find this useful

* [How to Map Sales Data in Suvit](https://help.suvit.io/articles/auto-mapping-sales)
* [How to Push Data to Tally](https://help.suvit.io/articles/how-do-we-process-or-push-sales-sales-return-data-to-tally)