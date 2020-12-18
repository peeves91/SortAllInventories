--control.lua

require "shared"

script.on_event(defines.events.on_gui_opened, function(event)
  if event.entity then
    for entityName, inventoryDefine in pairs(entityInventoryToSort) do
      if event.entity.type == entityName then
        if type(inventoryDefine) ~= "table" then
          event.entity.get_inventory(inventoryDefine).sort_and_merge()
        else
          -- used if there are multiple inventory defines for an entity; problem orignially originated with the roboport
          for k, v in ipairs(inventoryDefine) do
            event.entity.get_inventory(v).sort_and_merge()
          end
        end
      end
    end
  end
end)