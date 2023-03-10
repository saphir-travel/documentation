====================================
Subclass an existing field component
====================================

Let's take an example where we want to extends the `BooleanField` to create a boolean field
displaying "Late!" in red whenever the checkbox is checked.

#. Create a new widget component extending the field we want to extend

   The first step is to create the component that represents our new widget field, we do it by
   extending the existing `BooleanField` component.

   .. code-block:: javascript

      /** @odoo-module */

      import { registry } from "@web/core/registry";
      import { BooleanField } from "@web/views/fields/boolean/boolean_field";
      import { Component, xml } from "@odoo/owl";

      class LateOrderBooleanField extends BooleanField {
          static template = "my_module.LateOrderBooleanField";
      }

#. Create the field template

   The component uses a new template with the name `my_module.LateOrderBooleanField`. We can now
   create it by inheriting the current template of the `BooleanField`.

   .. code-block:: xml

      <?xml version="1.0" encoding="UTF-8" ?>
      <templates xml:space="preserve">
          <t t-name="my_module.LateOrderBooleanField" t-inherit="web.BooleanField" owl="1">
              <xpath expr="//CheckBox" position="after">
                  <t t-if="props.value">
                      <span class="text-danger"> Late! </span>
                  </t>
              </xpath>
          </t>
      </templates>

#. Register it to the fields registry

   .. code-block::

      registry.category("fields").add("late_boolean", LateOrderBooleanField);

#. Add the widget in the view

   You can now use your new widget in the appropriate view by using the `widget` keyword as the
   field attribute in the arch.

   .. code-block:: xml

      <field name="somefield" widget="late_boolean"/>
