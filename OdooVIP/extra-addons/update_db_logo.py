import base64

def run():
    with open('/mnt/extra-addons/vn168_theme/static/src/img/logo.png', 'rb') as f:
        logo_data = base64.b64encode(f.read())
        
    for c in env['res.company'].search([]):
        c.write({'logo': logo_data, 'logo_web': logo_data})
        
    if 'website' in env:
        for w in env['website'].search([]):
            w.write({'logo': logo_data})
            
    env.cr.commit()
    print("Logo successfully written to database!")

run()
