============================================================
Connect an Internet of Things (IoT) box to the Odoo database
============================================================

The Internet of Things (IoT) box is a micro-computer device that allows for the connection of
devices to an Odoo database. A :abbr:`IoT (Internet of Things)` box subscription is required in
order to use the :abbr:`IoT (Internet of Things)` box with a secured connection. A computer is also
required to setup the :abbr:`IoT (Internet of Things)` box.

.. seealso::
   `IoT Box FAQ <https://www.odoo.com/app/iot-faq>`_

:ref:`Install <general/install>` the :menuselection:`Internet of Things (IoT)` app on the
Odoo database.

.. image:: connect/install-iot-app.png
   :align: center
   :alt: The Internet of Things (IoT) app on the Odoo database.

Go to the :menuselection:`IoT` app and click on :guilabel:`Connect` on the :abbr:`IoT (Internet of
Things)` Boxes page.

.. image:: connect/connect-iot.png
   :align: center
   :alt: Connecting an IoT box to the Odoo database.

Follow the steps to connect the :abbr:`IoT (Internet of Things)` Box either via wired ethernet
connection or via WiFi.

.. image:: connect/connect-iot-box.png
   :align: center
   :alt: Connection steps for a wired connection or WiFi connection.

.. note::
   Ensure the :abbr:`IoT (Internet of Things)` box is flashed with the most up-to-date :abbr:`IoT
   (Internet of Things)` disk image (of the :abbr:`IoT (Internet of Things)` box version according
   to the database version).

Ethernet connection
===================

#. Connect all the devices that have to be connected with cables to the :abbr:`IoT (Internet of
   Things)` box (ethernet, :abbr:`USB (Universal Serial Bus)` devices, etc.).
#. Power on the :abbr:`IoT (Internet of Things)` Box.
#. Read the :guilabel:`Pairing Code` from a screen or a receipt printer connected to the :abbr:`IoT
   (Internet of Things)` Box.

   .. note::
      If no screen is attached to the :abbr:`IoT (Internet of Things)` box then the pairing code can
      be accessed from the :guilabel:`IoT Box Home Page` by clicking on :guilabel:`POS Display`. For
      instructions on how to access the :guilabel:`IoT Box Home Page`, visit
      :ref:`iot_connect/token`.

#. On the computer, input the :guilabel:`Pairing Code` on the :menuselection:`IoT` app of the
   database and click on the :guilabel:`Pair` button.

WiFi connection
===============

#. Connect all the devices that have to be connected with cables to the :abbr:`IoT (Internet of
   Things)` box (ethernet, :abbr:`USB (Universal Serial Bus)` devices, etc.).
#. Power on the :abbr:`IoT (Internet of Things)` Box.
#. From the computer, copy the :guilabel:`Token` from the :guilabel:`WiFi connection` section in
   :menuselection:`IoT` app of the Odoo database.
#. On the computer, connect to the :abbr:`IoT (Internet of Things)` Box WiFi network (make sure
   there is no ethernet cable plugged into the computer). The WiFi network dispersed by the
   :abbr:`IoT (Internet of Things)` Box  will start with `IoTBox-xxxxxxxxxx`.

   .. image:: connect/connect-iot-wifi.png
      :align: center
      :alt: WiFi networks available on the computer.

#. Upon connecting to the :abbr:`IoT (Internet of Things)` Box WiFi, a browser will automatically
   redirect to the :abbr:`IoT (Internet of Things)` Box Home Page. Name the :abbr:`IoT (Internet of
   Things)` Box, paste the previously copied token into the :guilabel:`Server Token` field, and then
   click on :guilabel:`Next`.

   .. image:: connect/server-token.png
      :align: center
      :alt: Enter the server token into the IoT box.

   .. note::
      If the :abbr:`IoT (Internet of Things)` Box WiFi connection wizard doesn't start, see
      :ref:`iot_connect/token`.

#. On the computer, choose the WiFi network that the :abbr:`IoT (Internet of Things)` box will
   connect with (enter the password if there is one) and click on :guilabel:`Connect`. Wait a few
   seconds before being redirected to the database. The computer may need to be manually
   re-connected back to the original WiFi connection.

   .. image:: connect/configure-wifi-network-iot.png
      :align: center
      :alt: Configuring the WiFi for the IoT box.

The :abbr:`IoT (Internet of Things)` box should appear in the :menuselection:`IoT` app of the Odoo
database.

.. image:: connect/iot-box-connected.png
   :align: center
   :alt: The IoT box has been successfully configured on the Odoo database.

.. important::
   The :abbr:`IoT (Internet of Things)` box may need to be manually reset upon successfully
   connecting via WiFi for the :abbr:`IoT (Internet of Things)` box to appear in the
   :menuselection:`IoT` app of the Odoo database.

.. _iot_connect/token:

Manually connecting the IoT box with the Token
==============================================

A manual connection of the :abbr:`IoT (Internet of Things)` box to the :menuselection:`IoT (Internet
of Things)` app can be made with the :guilabel:`Token`. The :guilabel:`Token` can be found after
clicking on :guilabel:`Connect` in the :menuselection:`IoT` app. The :guilabel:`Token` will be
inputted into the :guilabel:`IoT Box Home Page`.

#. Access the :guilabel:`IoT Box Home Page` by entering the :abbr:`IP (Internet Protocol)` address
   of the :abbr:`IoT (Internet of Things)` box into a browser window.

   .. note::
      The :abbr:`IP (Internet Protocol)` address can be accessed by the router the :abbr:`IoT
      (Internet of Things)` box is connected to or by connecting a printer to the :abbr:`IoT
      (Internet of Things)` box (a receipt will print out with the :abbr:`IoT (Internet of Things)`
      box's :abbr:`IP (Internet Protocol)` address on it).

#. Enter the :guilabel:`Token` under the :guilabel:`Server` section by clicking on
   :guilabel:`Configure`.
#. Paste the :guilabel:`Token` into the :guilabel:`Server Token` field and click
   :guilabel:`Connect`.

IoT box schema
==============

Raspberry Pi 4
--------------

.. figure:: connect/iot-box-schema.png

   Odoo IoT box (Raspberry Pi 4) schema with labels.

Raspberry Pi 3
--------------

.. figure:: connect/iox-box-schema-3.png

   Odoo IoT box (Raspberry Pi 3) schema with labels.
