from odoo import http  # pyre-ignore[21]
from odoo.http import request, Response  # pyre-ignore[21]
import os

try:
    from odoo.addons.web.controllers.home import Home  # pyre-ignore[21]
except ImportError:
    Home = object


class VN168Branding(http.Controller):
    """
    Intercepts all Odoo logo/icon requests and returns the VN168 logo instead.
    This effectively replaces all Odoo branding across the entire platform.
    """
    
    VN168_LOGO_PATH = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'static', 'src', 'img', 'logo.png'
    )

    def _serve_vn168_logo(self, content_type='image/png'):
        """Return the VN168 logo.png as a PNG image response."""
        with open(self.VN168_LOGO_PATH, 'rb') as f:
            logo_data = f.read()
        return Response(
            logo_data,
            status=200,
            headers={
                'Content-Type': content_type,
                'Cache-Control': 'no-cache, no-store, must-revalidate',
            }
        )

    # Intercept Odoo logo files
    @http.route('/web/static/img/odoo_logo_tiny.png', type='http', auth='none')
    def odoo_logo_tiny(self, **kw):
        return self._serve_vn168_logo()

    @http.route('/web/static/img/odoo_logo.svg', type='http', auth='none')
    def odoo_logo_svg(self, **kw):
        return self._serve_vn168_logo()

    @http.route('/web/static/img/odoo_logo_dark.svg', type='http', auth='none')
    def odoo_logo_dark_svg(self, **kw):
        return self._serve_vn168_logo()

    @http.route('/web/static/img/odoo-icon.svg', type='http', auth='none')
    def odoo_icon_svg(self, **kw):
        return self._serve_vn168_logo()

    @http.route('/web/static/img/odoo-icon-512x512.png', type='http', auth='none')
    def odoo_icon_512(self, **kw):
        return self._serve_vn168_logo()

    @http.route('/web/static/img/odoo-icon-192x192.png', type='http', auth='none')
    def odoo_icon_192(self, **kw):
        return self._serve_vn168_logo()

    @http.route('/web/static/img/odoo-icon-ios.png', type='http', auth='none')
    def odoo_icon_ios(self, **kw):
        return self._serve_vn168_logo()

    @http.route('/web/static/img/logo_inverse_white_206px.png', type='http', auth='none')
    def odoo_logo_inverse(self, **kw):
        return self._serve_vn168_logo()

    @http.route('/web/static/img/favicon.ico', type='http', auth='none')
    def odoo_favicon(self, **kw):
        return self._serve_vn168_logo('image/x-icon')

    @http.route('/web/binary/favicon', type='http', auth='none')
    def odoo_binary_favicon(self, **kw):
        return self._serve_vn168_logo('image/x-icon')

    @http.route('/web/binary/company_logo', type='http', auth='none')
    def odoo_company_logo(self, **kw):
        return self._serve_vn168_logo()


class VN168Home(Home):
    """
    Custom Home controller for VN168.
    Handles branded routes (/vn168) and redirections from the original /odoo path.
    """

    @http.route('/vn168/apps', type='http', auth="user")
    def vn168_apps(self, **kw):
        return request.redirect('/vn168#action=base.action_module_main')

    @http.route(['/vn168', '/vn168/<path:subpath>'], type='http', auth="none")
    def vn168_web_client(self, s_action=None, **kw):
        if not request.db:
            return request.redirect('/web/database/selector')
        if hasattr(super(), 'web_client'):
            return super().web_client(s_action=s_action, **kw)  # pyre-ignore[16]
        return Home.web_client(self, s_action=s_action, **kw)  # pyre-ignore[16]

    @http.route(['/odoo', '/odoo/<path:subpath>'], type='http', auth="none")
    def web_client(self, s_action=None, **kw):
        if request.httprequest.path.startswith('/odoo'):
            new_path = request.httprequest.path.replace('/odoo', '/vn168', 1)
            query_string = request.httprequest.query_string.decode('utf-8')
            if query_string:
                new_path += '?' + query_string
            return request.redirect(new_path, code=301)
        if hasattr(super(), 'web_client'):
            return super().web_client(s_action=s_action, **kw)  # pyre-ignore[16]
        return Home.web_client(self, s_action=s_action, **kw)  # pyre-ignore[16]
