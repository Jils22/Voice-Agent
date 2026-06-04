# Document Merge Functionality in Banking

Source: https://taxone.vyapar.com/help/articles/document-merge-functionality-in-banking

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Document Merge Functionality in Banking](/help/articles/document-merge-functionality-in-banking)

[Merge document functionality](#merge-document-functionality)[Step 1: Select the Files](#step-1-select-the-files)[Step 2: Merge the Document](#step-2-merge-the-document)[Step 3: View Merged Document](#step-3-view-merged-document)[Step 4: Download the Merged Document](#step-4-download-the-merged-document)[Conditions for Merging PDFs](#conditions-for-merging-pdfs)[Conditions for Removing Duplicate Records:](#conditions-for-removing-duplicate-records-)

# Document Merge Functionality in Banking

The Merge Document feature lets you combine multiple banking files from the same bank. Just select the files, and Suvit will merge them automatically.

### Merge document functionality

* In Banking lets you combine two or more banking files from the same bank and account number. After merging, you can also add more files to the merged document.

#### Step 1: Select the Files

![merger 1.png](https://strapi.suvit.io/uploads/merger_1_d2657ff794.png)

* Make sure both **Bank Statements** should belong to the **Same Bank**
* Select the file you want to merge, as shown in the image above.

#### Step 2: Merge the Document

![merge 2.png](https://strapi.suvit.io/uploads/merge_2_f4a15a02d9.png)

* Click the **Merge Document** button to combine the selected files (must be from the same bank).

#### Step 3: View Merged Document

![merge 3.png](https://strapi.suvit.io/uploads/merge_3_b6960a3e19.png)

* Once merged, the document will appear as shown in the example image. By clicking the "i" icon, you can view the file name.

#### Step 4: Download the Merged Document

![merge 4.png](https://strapi.suvit.io/uploads/merge_4_ce566d4531.png)

* The merged files can be downloaded as a **ZIP file**.

### Conditions for Merging PDFs

* (a) The uploaded PDFs must be from the same bank.
* (b) After merging, the total transactions must equal 30,000 (e.g., if one PDF has 10,000 transactions and the other has 20,000, the merged PDF should have a total of 30,000 transactions).

### Conditions for Removing Duplicate Records:

* If two files with the same ledger are saved, merge them and remove duplicates.
* If two files with different ledgers are saved, do not merge.
* If two files with the same ledger are saved and one file is unsaved, remove all duplicate and unsaved records.
* If one file is saved and one is unsaved, remove all records from the unsaved file.