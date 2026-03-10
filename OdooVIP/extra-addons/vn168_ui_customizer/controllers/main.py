from odoo import http
from odoo.http import request, Response

DEFAULTS = {
    'primary': '#714B67',
    'navbar_bg': '#714B67',
    'navbar_txt': '#ffffff',
    'btn': '#00A09D',
}


class VN168ColorController(http.Controller):

    @http.route('/ui_colors/user.css', type='http', auth='user', csrf=False)
    def get_user_colors(self, **kwargs):
        """Trả về CSS màu sắc cá nhân. An toàn tuyệt đối."""
        colors = dict(DEFAULTS)
        try:
            uid = request.env.uid
            if uid:
                request.env.cr.execute("""
                    SELECT vn168_primary_color,
                           vn168_navbar_color,
                           vn168_navbar_text_color,
                           vn168_button_color
                    FROM res_users WHERE id = %s
                """, (uid,))
                row = request.env.cr.fetchone()
                if row:
                    colors['primary']    = row[0] or colors['primary']
                    colors['navbar_bg']  = row[1] or colors['navbar_bg']
                    colors['navbar_txt'] = row[2] or colors['navbar_txt']
                    colors['btn']        = row[3] or colors['btn']
        except Exception:
            pass

        css = """
/* VN168 User Colors - Generated dynamically */
:root {{
    --vn168-primary:    {primary};
    --vn168-navbar-bg:  {navbar_bg};
    --vn168-navbar-txt: {navbar_txt};
    --vn168-btn:        {btn};
    --o-brand-primary:  {btn};
    --bs-primary:       {btn};
}}

/* ===== NAVBAR ===== */
.o_main_navbar {{
    background-color: {navbar_bg} !important;
    background: {navbar_bg} !important;
}}
.o_main_navbar .o_menu_brand,
.o_main_navbar a,
.o_main_navbar i,
.o_main_navbar span,
.o_main_navbar button,
.o_main_navbar .dropdown-toggle {{
    color: {navbar_txt} !important;
}}

/* ===== NUT BAM (Buttons) ===== */
.btn-primary,
.o_form_button_save,
.o_statusbar_status button.btn-primary,
.o_form_button_edit {{
    background-color: {btn} !important;
    border-color: {btn} !important;
    color: #fff !important;
}}
.btn-primary:hover,
.btn-primary:focus {{
    background-color: {btn} !important;
    border-color: {btn} !important;
    filter: brightness(0.88);
}}

/* ===== ACCENT thong nhat theo mau nut bam ===== */

/* Links trong noi dung (khong override navbar) */
.o_content a:not(.btn):not(.dropdown-item):not(.nav-link),
.o_form_view a:not(.btn),
.o_list_view a:not(.btn),
.o_field_widget a:not(.btn) {{
    color: {btn} !important;
}}

/* Tab active */
.nav-tabs .nav-link.active,
.nav-tabs .nav-item.show .nav-link,
.o_notebook .nav-tabs .nav-link.active {{
    color: {btn} !important;
    border-bottom: 2px solid {btn} !important;
}}

/* Input focus ring */
.form-control:focus,
.o_field_widget input:focus,
.o_field_widget textarea:focus,
.o_field_widget select:focus {{
    border-color: {btn} !important;
    box-shadow: 0 0 0 0.15rem {btn}44 !important;
    outline: none !important;
}}

/* Checkbox / Radio */
.form-check-input:checked,
.custom-control-input:checked ~ .custom-control-label::before {{
    background-color: {btn} !important;
    border-color: {btn} !important;
}}

/* Badge */
.badge.bg-primary,
.badge-primary {{
    background-color: {btn} !important;
    color: #fff !important;
}}

/* Breadcrumb link */
.o_breadcrumb a,
.breadcrumb-item a {{
    color: {btn} !important;
}}

/* Progress bar */
.progress-bar {{
    background-color: {btn} !important;
}}

/* Text selection */
::selection {{
    background-color: {btn}55 !important;
}}

/* Status bar selected state */
.o_statusbar_status .o_arrow_button.btn-primary {{
    background-color: {btn} !important;
    border-color: {btn} !important;
}}

/* An menu Odoo mac dinh */
[data-menu="odoo_account"],
[data-menu="documentation"],
[data-menu="support"] {{
    display: none !important;
}}
""".format(**colors)

        headers = [
            ('Content-Type', 'text/css; charset=utf-8'),
            ('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0'),
            ('Pragma', 'no-cache'),
        ]
        return Response(css, headers=headers)
