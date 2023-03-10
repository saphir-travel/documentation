============================
Create a new field component
============================

Assume that we want to create a field that displays a simple text in red.

#. Create the new Owl component representing our new field

   .. code-block:: js

      /** @odoo-module */

      import { standardFieldProps } from "@web/views/fields/standard_field_props";
      import { Component, xml } from "@odoo/owl";
      import { registry } from "@web/core/registry";

      export class MyTextField extends Component {
          static template = xml`
              <input t-att-id="props.id" class="text-danger" t-att-value="props.value" onChange.bind="onChange" />
          `;
          static props = {
              ...standardFieldProps,
          };
          static supportedTypes = ["char"];

          /**
          * @param {boolean} newValue
          */
          onChange(newValue) {
              this.props.update(newValue);
          }
      }

   The imported `standardFieldProps` contains the standard props passed by the `View` such as
   the `update` function to update the value, the `type` of the field in the model, the
   `readonly` boolean, and others.

#. In the same file, register it to the fields registry.

   .. code-block:: js

      registry.category("fields").add("my_text_field", MyTextField);

   This ensures the mapping between the widget name in the arch and its actual component.

#. Add the widget in the view arch

   You can now use your new widget in the appropriate view by using the `widget` keyword as the
   field attribute in the arch.

   .. code-block:: xml

      <field name="somefield" widget="my_text_field"/>
