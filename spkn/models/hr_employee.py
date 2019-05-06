from odoo import api, fields, models


class hr_employee(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    # field - field tambahan
    npwp = fields.Char(string="NPWP", required=False, help="Masukkan nomor NPWP",)
    bpjs_nomor = fields.Char(string="NO BPJS", required=False, )
    tgl_masuk = fields.Date(string="TGL MASUK", required=False, )
    tgl_percobaan = fields.Date(string="Tgl Percobaan", required=False, )
    tgl_kontrak_1 = fields.Date(string="Tgl Kontrak 1", required=False, )
    tgl_kontrak_2 = fields.Date(string="Tgl Kontrak 2", required=False, )
    tgl_tetap = fields.Date(string="Tgl Tetap", required=False, )



