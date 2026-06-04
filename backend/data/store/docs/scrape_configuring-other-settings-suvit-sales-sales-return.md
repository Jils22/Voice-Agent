# Configuring Other Settings in Suvit Sales

Source: https://taxone.vyapar.com/help/articles/configuring-other-settings-suvit-sales-sales-return

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Configuring Other Settings in Suvit Sales](/help/articles/configuring-other-settings-suvit-sales-sales-return)

[How It Works](#how-it-works)[Example Workflow](#example-workflow)[Why This Matters](#why-this-matters)[Configuration](#configuration)[1. Party Details](#1-party-details)[Buyer Details](#buyer-details)[Consignee Details](#consignee-details)[3. Dispatch Details](#3-dispatch-details)[Key Fields](#key-fields)[4. Order Details](#4-order-details)[Key Fields](#key-fields)[5. Export Details](#5-export-details)[Key Fields](#key-fields)

# Configuring Other Settings in Suvit Sales

Manage key fields like Voucher No., Cost Center, Party, Buyer, Consignee & Dispatch details in Suvit for accurate data entry and smooth accounting integration.

##### How to use other settings?

* Follow the steps below:

![1 path.png](https://strapi.suvit.io/uploads/1_path_7ce80ba0e8.png)

* Go to -> **Mapping Screen** -> **Configuration (in upper right corner)**

![1 main image - Copy.png](https://strapi.suvit.io/uploads/1_main_image_Copy_018ce46e77.png)

* Above is the configuration screen

### **How It Works**

* **Checkboxes**: Each field has a checkbox. By selecting specific boxes, you determine which data fields to transfer to your accounting system.

```
**Note** - Main fields cannot be unchecked.
```

* **Checked fields** will be mapped and imported.
* **Unchecked fields** will be ignored.

```
**Note** - Make sure the field which are selected those field should be there in the excel sheet.
```

---

### **Example Workflow**

Let’s say you want to transfer only the **Buyer (Bill to)**, **Invoice Date**, and **GSTIN/UIN** fields:

1. In the **Party Details** section, check **Buyer (Bill to)**.
2. In the **Dispatch Details** section, check **Invoice Date**.
3. Leave other checkboxes unchecked.
4. Save the configuration to import only these selected fields.

---

### **Why This Matters**

This granular control prevents unnecessary data clutter and ensures only the required fields are imported. It also helps avoid errors during data mapping, especially when dealing with large datasets or multiple fields.

---

### Configuration

* **Date:** This is for the invoice date.
* **Voucher Date:** Voucher date of the Bill.
* **Voucher Number:** Voucher number of the bill.
  + In Tally, if you have **Method of Voucher Numbering -> Manual**, then this field is required.
  + **How to check:** Go to Alter -> Voucher Type -> Sales -> Method of Voucher Numbering.
* **Reference Number:** Reference number for the bill.
* **Voucher Type:** By default, the system will pick **Sales** as a voucher type. If you have created a Custom Voucher Type, you can select it from the transaction screen.
* **Party A/C Name:** The party account name in sales is the customer name.

---

### **1. Party Details**

The "Party Details" section focuses on information about the entities involved in a transaction, most commonly the *customer* (buyer) and sometimes the *vendor* (seller, especially in purchase transactions).

#### **Buyer Details**

* **Buyer (Bill to) / Customer Name:** The legal or trading name of the customer being billed for the transaction.
* **Mailing Name (Buyer):** The official name used for correspondence with the customer.
* **Address (Buyer):** The customer's billing address, including street, city, state, and postal code.
* **State (Buyer):** The state or province where the customer is located, crucial for GST calculations.
* **Pincode (Buyer):** The postal code or zip code of the customer's billing address.
* **GSTIN/UIN:** The customer's GST identification number, essential for tax compliance.
* **Place of Supply:** The state where goods are supplied or delivered, critical for GST calculations.

```
Note: The "Consignee Details" section covers information about the recipient of the goods or services (if different from the buyer).
```

#### **Consignee Details**

* **Mailing Name (Consignee):** The name of the consignee to whom goods are shipped.
* **Consignee GSTIN/UIN:** The GST identification number of the consignee.
* **Consignee Address:** The shipping address, including street, city, state, and postal code.
* **State (Consignee):** The state of the consignee, essential for determining GST rates.
* **Pincode (Consignee):** The postal code of the consignee's shipping address.

---

### **3. Dispatch Details**

This section tracks shipment and delivery information to ensure accurate logistics records.

#### **Key Fields**

* **Delivery Note No(s):** The delivery note numbers linked to the transaction.
* **Invoice Date:** The date the invoice was issued.
* **Dispatch Doc No.:** The document number associated with the dispatch.
* **Dispatched Through:** The mode of transportation (e.g., courier, truck).
* **Destination:** The final delivery location for the goods.
* **Carrier Name/Agent:** The transport company's name or the agent managing the dispatch.
* **Bill of Lading/LR-RR no.:** Refers to the Lorry/Railway Receipt number and date. The LR/RR number and date are entered in the Bill of Lading/LR-RR No. & Dt. under the Party Details sub-screen
* **Bill of Lading date:** The date when the goods are loaded onto the ship.

---

### **4. Order Details**

This section includes details about the original sales order.

#### **Key Fields**

* **Order No(s):** The sales order numbers related to the transaction.
* **Order Date:** The date the sales order was created.
* **Mode/Terms of Payment:** Payment terms (e.g., cash, credit, or bank transfer).
* **Other References:** Additional reference numbers or related documents.
* **Terms of Delivery:** Delivery terms, such as FOB (Free on Board) or CIF (Cost, Insurance, and Freight).

---

### **5. Export Details**

This section applies to export transactions and helps track international shipping.

#### **Key Fields**

* **Place of Receipt by Shipper:** The location where goods are handed over to the shipper.
* **Vessel/Flight/Motor-Vehicle No.:** The identifier of the transport used for export.
* **Shipping Bill Date:** The date the shipping bill was issued.
* **Port of Loading:** The port where goods are loaded for shipment.
* **Port of Discharge:** The port where goods will be unloaded.
* **Shipping Bill No.:** The unique number assigned to the shipping bill.
* **Tracking Date:** The date the shipment becomes trackable.
* **Port Code:** A unique code identifying the port.