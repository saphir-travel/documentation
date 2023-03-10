
====================================
Subclass an existing JavaScript view
====================================

Assume we need to create a custom version of a generic view. For example, a kanban view with some
extra ribbon-like widget on top (to display some specific custom information). In that case, this
can be done in a few steps:

#. Extend the kanban controller/renderer/model and register it in the view registry:

   .. code-block:: js

      /** @odoo-module */

      import { KanbanController } from "@web/views/kanban/kanban_controller";
      import { kanbanView } from "@web/views/kanban/kanban_view";
      import { registry } from "@web/core/registry";

      // the controller usually contains the Layout and the renderer.
      class CustomKanbanController extends KanbanController {
          // Your logic here, override or insert new methods...
          // if you override setup(), don't forget to call super.setup()
      }

      CustomKanbanController.template = "my_module.CustomKanbanView";

      export const customKanbanView = {
          ...kanbanView, // contains the default Renderer/Controller/Model
          Controller: CustomKanbanController,
      };

      // Register it to the views registry
      registry.category("views").add("custom_kanban", customeKanbanView);

   In our custom kanban we defined a new template, we can either inherit the kanban controller
   template and add our template pieces or we can define a completely new template.

   .. code-block:: xml

      <?xml version="1.0" encoding="UTF-8" ?>
      <templates>
          <t t-name="my_module.CustomKanbanView" t-inherit="web.KanbanView" owl="1">
              <xpath expr="//Layout" position="before">
                  <div>
                      Hello world !
                  </div>
              </xpath>
          </t>
      </templates>

#. Using the view in the kanban arch.

   We created our new view, we can now use it with the `js_class` attribute in the arch

   .. code-block:: xml

      <kanban js_class="custom_kanban">
          <templates>
              <t t-name="kanban-box">
                  <!--Your comment-->
              </t>
          </templates>
      </kanban>

The possibilities for extending views are endless. While we have only extended the controller
here, you can also extend the renderer to add new buttons, modify how records are presented, or
customize the dropdown, as well as extend other components such as the model and buttonTemplate.
