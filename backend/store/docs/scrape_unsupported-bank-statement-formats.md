# Unsupported Bank Statement Formats

Source: https://taxone.vyapar.com/help/articles/unsupported-bank-statement-formats

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Unsupported Bank Statement Formats](/help/articles/unsupported-bank-statement-formats)

[Unsupported Bank Statement Formats](#unsupported-bank-statement-formats)[Unsupported Formats:](#unsupported-formats-)[1. Improper Alignment:](#1-improper-alignment-)[2. Scanned PDFs:](#2-scanned-pdfs-)[Steps to Avoid Errors:](#steps-to-avoid-errors-)

# Unsupported Bank Statement Formats

Some bank formats aren’t supported in Suvit. Avoid upload errors by checking compatibility. Passbooks, RTP TXT, Dot Matrix, loan & share statements aren’t supported.

---

### Unsupported Bank Statement Formats

When you upload a document in Suvit, the system extracts it into a tabular format, making it easier to identify and assign ledgers to transactions. During this process, the system verifies the document's correctness and format.

For example:

* Suvit checks the **opening and closing balance** of the uploaded statement. If there's an error in the closing balance, the system will reject the statement to prevent uploading incorrect data.
* Misalignment issues in certain document formats may cause extraction errors, leading to rejection.

### **Unsupported Formats:**

#### 1. **Improper Alignment:**

* Documents downloaded from mobile banking apps or other sources often have misaligned data (e.g., dates, narrations, and amounts are not aligned in rows). This makes it difficult for the system to extract the data, resulting in rejection.
* Example of unsupported format:
  ![Canara Bank 1](https://strapi.suvit.io/uploads/Canara_Bank_1_6249cbc53d.png)
* **Note:** If the statement is in a **proper tabular format**, it will be successfully uploaded.
  ![Supported Canara Bank Statement](https://strapi.suvit.io/uploads/2image_4ea278855f.png)

#### 2. **Scanned PDFs:**

* Scanned PDFs can be rejected due to issues like:
  + Blurred content.
  + Reflective data from the back side of the page.
* Examples of rejected scanned PDFs:
  ![Blurry Statement](https://strapi.suvit.io/uploads/4image_37_4389f7ccaa.png)
  ![Reflective Data](https://strapi.suvit.io/uploads/5_B_Image_18_a30a144aa2.png)

---

#### **Steps to Avoid Errors:**

1. Ensure the statement is **clearly visible** and in a **readable tabular format**.
2. Check for proper alignment of:
   * Date.
   * Narration.
   * Debit and credit amounts.
3. Avoid uploading:
   * Blurred scanned PDFs.
   * Statements with handwritten content.
   * Documents with missing data (e.g., missing dates or debit/credit amounts).

By following these guidelines, your document will be successfully uploaded, ensuring accurate data extraction and processing.