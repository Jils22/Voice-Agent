# How to Sync Journal Data with Item Support in Tally using Suvit

Source: https://taxone.vyapar.com/help/articles/Journal-with-item

[All Collection](/help)[Journal](/help/collections/journal)[How to Sync Journal Data with Item Support in Tally using Suvit](/help/articles/Journal-with-item)

[Follow the below steps](#follow-the-below-steps)[Step 1: Navigate to Data Entry Automation](#step-1-navigate-to-data-entry-automation)[Step 2: Select Journal Upload](#step-2-select-journal-upload)[Step 3: Upload File](#step-3-upload-file)[Step 4: Sheet preparation](#step-4-sheet-preparation)[Step 5: Configurtaion](#step-5-configurtaion)[Step 6: Mapping](#step-6-mapping)[Step 7: Sync the Data in Tally](#step-7-sync-the-data-in-tally)[You can find detailed instructions here:](#you-can-find-detailed-instructions-here-)

# How to Sync Journal Data with Item Support in Tally using Suvit

Suvit helps manage financial data by syncing journal entries with item details to Tally. Ensure your data includes item names, quantities, and amounts

### Follow the below steps

#### Step 1: Navigate to Data Entry Automation

![1.webp](https://strapi.suvit.io/uploads/1_c53f716d22.webp)

* Go to **Data Entry Automation** → **Bulk Upload** → **Journal**

#### Step 2: Select Journal Upload

![2.webp](https://strapi.suvit.io/uploads/2_f5215970ae.webp)

* Click on **Upload** button

#### Step 3: Upload File

![3.webp](https://strapi.suvit.io/uploads/3_ba9a2c6b2b.webp)

* Select your file by using **Click to upload** and Click on **Upload** button

![4.webp](https://strapi.suvit.io/uploads/4_eb66c1a896.webp)

* Click on the uploaded **File**

#### Step 4: Sheet preparation

\*\*Data requirement for excel sheet\*\*

![5 Sample sheet.png](https://strapi.suvit.io/uploads/5\_Sample\_sheet\_6c0d598bf5.png)

⇒  \*\*You need at least 9 types of data in your Excel sheet for mapping:\*\*

* 1. \*\*Journal No.:\*\* Journal entry number.

* 2. \*\*Reference no.:\*\* Transaction Number

* 3. \*\*Date:\*\* Date of the invoice bill/entry date.

* 4. \*\*Particulars:\*\* Name of the Debtor and creditor

* 5. \*\*Name of Item:\*\* Stock item name as per tally.

* 6. \*\*Quantity:\*\* total Quantity

* 7. \*\*Rate:\*\* rate of the stock Item

* 8. \*\*Debit/Credit Type:\*\* Type of amount Debit or Credit.

* 9. \*\*Amount:\*\* value of the stock Item or Bill.

⇒ \*\*Not Mandatory list\*\*

* 10. \*\*Cost Center\*\* From which department cost was allocated ( If applicable)

* 11. \*\*TOTAL AMOUNT:\*\* Grand total including taxes (for verification).

#### Step 5: **Configurtaion**

![6 config.png](https://strapi.suvit.io/uploads/6_config_80ed3e9568.png)

* After uploading your spreadsheet, you will need to access the **Mapping Screen** in Suvit:

  + a. Navigate to the **"Configuration"** section.
  + b. Look for an option to enable **item details**. This step is crucial as it allows Suvit to sync the journal data with item support in Tally.

#### Step 6: **Mapping**

![7 mapping.png](https://strapi.suvit.io/uploads/7_mapping_7e1abe0f1a.png)

1. **Imported File Header:** Shows headings from your Excel sheet.
2. **Tally Fields:** Fields matched with Tally. You can change them if needed.
3. **Your Sheet Data:** Shows sample data for cross-checking
4. Press **Next** to move to **GST Mapping**.

#### Step 7: **Sync the Data in Tally**

* Once the mapping is complete, you are ready to sync the data in Tally.
* To do this, follow the instructions provided in Suvit's documentation for syncing journal data to Tally.

#### You can find detailed instructions here:

* How to Push Journal Entries [Learn more](https://help.suvit.io/articles/how-do-we-process-or-push-journal-data-to-tally)