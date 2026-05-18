# Horizontal Sheet Multiple GST with Common tally tax ledger

Source: https://taxone.vyapar.com/help/articles/horizontal-sheet-multiple-gst-with-common-tally-tax-ledger

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Horizontal Sheet Multiple GST with Common tally tax ledger](/help/articles/horizontal-sheet-multiple-gst-with-common-tally-tax-ledger)

[Horizontal Sheet with Multiple GST Rates and Common Tally Tax Ledger](#horizontal-sheet-with-multiple-gst-rates-and-common-tally-tax-ledger)[Step 1:Sheet Modifications](#step-1-sheet-modifications)[Step 2: Map Sales Account Amounts](#step-2-map-sales-account-amounts)[Step 3: Map GST Ledgers](#step-3-map-gst-ledgers)[Step 4: Map Other GST Rates](#step-4-map-other-gst-rates)[You may find this helpful:](#you-may-find-this-helpful-)

# Horizontal Sheet Multiple GST with Common tally tax ledger

Here we will guide you to map common tally tax ledgers in case where your data is of multiple GST rate applicability.

---

### Horizontal Sheet with Multiple GST Rates and Common Tally Tax Ledger

If your sheet has multiple GST percentages in a horizontal format, follow these steps to map and post tax amounts into respective Tally tax ledgers.

![1Image S8.png](https://strapi.suvit.io/uploads/1_Image_S8_426c019237.png)

#### Step 1:Sheet Modifications

![2Image S10_Pending.png](https://strapi.suvit.io/uploads/2_Image_S10_Pending_c4e9780089.png)

* Modify your sheet as shown in the image above.
* In the **Particulars** column, add one of the ledgers corresponding to the GST rates in your sheet.
  + Example: If your sheet has **Sales Exempt**, **Sales @ 5%**, **Sales @ 12%**, **Sales @ 18%**, and **Sales @ 28%**, select **Sales @ 5%** for illustration.

#### Step 2: Map Sales Account Amounts

![3 img.png](https://strapi.suvit.io/uploads/3_img_84d5715264.png)

* If there are multiple sales accounts, choose a specific one (e.g., **Sales @ 5%**) and map its amount to the **Amount** field in field mapping.

#### Step 3: Map GST Ledgers

![3Common GST.png](https://strapi.suvit.io/uploads/3_Common_GST_c36319f637.png)

* In the **GST Ledger** section, select the common tax ledgers used in Tally, such as **SGST**, **CGST**, and **IGST**.

#### Step 4: Map Other GST Rates

![4mapping3.png](https://strapi.suvit.io/uploads/4mapping3_4b585a387f.png)

* For other GST rates like **Sales @ 12%**, **Sales @ 18%**, **Sales @ 28%**, and **Sales Exempt**, map them in the **Ledger Mapping** section.
* Under **Your Sheet Header**, find the corresponding headers from your uploaded sheet.
* Under **Select Your Ledger**, choose the respective tax ledgers available in Tally.

##### Summary ✍

* By mapping GST percentages and ledgers correctly, Suvit ensures that tax amounts are posted accurately into respective Tally tax ledgers.

#### You may find this helpful:

* For a detailed step-by-step guide on mapping horizontal tax rates and using common duties and taxes in Suvit, [Learn more](https://help.suvit.io/articles/horizontal-tax-rate-common-duties-and-taxes).