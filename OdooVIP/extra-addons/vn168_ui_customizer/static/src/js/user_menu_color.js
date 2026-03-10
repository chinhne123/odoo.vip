/** @odoo-module **/
import { registry } from "@web/core/registry";
import { session } from "@web/session";

const menuItems = registry.category("user_menuitems");

// ==== 1. INJECT CSS MÀU SẮC VÀO BACKEND ====
function injectUserColors() {
    const linkId = "vn168-user-colors";
    if (document.getElementById(linkId)) return;
    const link = document.createElement("link");
    link.id = linkId;
    link.rel = "stylesheet";
    link.type = "text/css";
    link.href = `/ui_colors/user.css?t=${Date.now()}`;
    document.head.appendChild(link);
}
injectUserColors();

// ==== 2. DỌN DẸP MENU ODOO ====
for (const id of ["odoo_account", "documentation", "support"]) {
    if (menuItems.contains(id)) menuItems.remove(id);
}


