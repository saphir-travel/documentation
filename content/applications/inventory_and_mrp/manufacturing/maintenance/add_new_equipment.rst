=================
Add new equipment
=================
Using Odoo Maintenance, it is possible to track individual pieces of equipment, along with
information about their maintenance requirements. To add a new piece of equipment, navigate to the
:guilabel:`Maintenance` module, select :menuselection:`Equipments --> Machines & Tools --> Create`,
and configure the equipment as follows:

- :guilabel:`Equipment Name`: the product name of the piece of equipment
- :guilabel:`Equipment Category`: the category that the equipment belongs to
- :guilabel:`Company`: the company that owns the equipment
- :guilabel:`Used By`: Specify if the equipment is used by a specific employee, department, or both.
  Select :guilabel:`Other` to specify both an employee and a department.
- :guilabel:`Maintenance Team`: the maintenance team responsible for servicing the equipment
- :guilabel:`Technician`: the specific technician responsible for servicing the equipment
- :guilabel:`Used in location`: the location where the equipment is used
- :guilabel:`Work Center`: the work center where the equipment is used

.. image:: add_new_equipment/new_equipment_form.png
   :align: center
   :alt: An example of a fully configured new equipment form.

Include additional product information
--------------------------------------
The :guilabel:`Product Information` tab at the bottom of the form can be used to provide further
details about the piece of equipment:

- :guilabel:`Vendor`: the vendor that the equipment was purchased from
- :guilabel:`Vendor Reference`: the reference code assigned to the vendor
- :guilabel:`Model`: the specific model of the piece of equipment
- :guilabel:`Serial Number`: the unique serial number of the equipment
- :guilabel:`Effective Date`: The date that the equipment became available for use. This is used to
  calculate the :abbr:`MTBF (Mean Time Between Failures)`.
- :guilabel:`Cost`: the amount the equipment was purchased for
- :guilabel:`Warranty Expiration Date`: the date on which the equipment's warranty will expire

.. image:: add_new_equipment/new_equipment_product_information.png
   :align: center
   :alt: The product information tab for the new piece of equipment.

Add maintenance details
-----------------------
The :guilabel:`Maintenance` tab includes information that can be useful to maintenance teams:

- :guilabel:`Preventive Maintenance Frequency`: specifies how often maintenance should be
  performed to prevent equipment failure
- :guilabel:`Maintenance Duration`: the amount of time required to fix the equipment when it fails
- :guilabel:`Expected Mean Time Between Failure`: the average amount of time that the equipment is
  expected to operate before failing

.. image:: add_new_equipment/new_equipment_maintenance.png
   :align: center
   :alt: The maintenance tab for the new piece of equipment.

.. Note::
    The :guilabel:`Maintenance` tab also includes sections for :guilabel:`Mean Time Between Failure`,
    :guilabel:`Estimated Next Failure`, :guilabel:`Latest Failure`,
    and :guilabel:`Mean Time To Repair`. These values are calculated automatically based on
    maintenance requests, if any exist.

.. tip::
    To see the maintenance requests for a piece of equipment, go to the page for the equipment and
    select :guilabel:`Maintenance` in the top right corner of the form.
