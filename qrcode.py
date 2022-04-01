#Qrcode Generator
import pyqrcode
from pyqrcode import QRCode

import frappe
  
s = "hunainiqbal"
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)

def generate_qrcode():
    itemname =  frappe.db.sql(""" select name from tabitems """ , as_dict=True)
    sname = []
    count = 0
    for i in itemname.item:
        count+1
        sname.append(i)
        url = pyqrcode.create(sname[count])
        url.svg(sname+".svg", scale = 8)

        frappe.db.sql("""Update tabitem  set qr_code = %s
                where name = %s """, (url, itemname))
        
        frappe.db.commit()  





# qrdata = sale_invoice.name
# doctype = sale_invoice.doctype
# docname = sale_invoice.name
# filename = qr
# qr_image = io.BytesIO()
# url = qrcreate(str(qrcode), error=(‘L’)
# url.png(qr_image, scale=2, quiet_zone=1)
# file = frappe.get_doc({
# “doctype”: “File”,
# “file_name”: filename,
# “attached_to_doctype”: doctype,
# “attached_to_name”: docname,
# “attached_to_field”: “qr_code”,
# “is_private”: 0,
# “content”: qr_image.getvalue()})
# _file.save()
# frappe.db.commit()
# sale_invoice.qr_code = _file.file_url
# frappe.db.sql("""Update tabSales Invoice set qr_code = %s
# where name = %s """, (_file.file_url,
# sale_invoice.name))
# frappe.db.commit()


