from odoo import api, fields, models


class NewModule(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    x_kategori = fields.Char(string="Kategori", required=False, )
    x_jenis = fields.Char(string="Jenis", required=False, )
    x_mapel = fields.Char(string="Mapel", required=False, )
    x_kelas = fields.Char(string="Kelas", required=False, )
    x_peruntukan = fields.Char(string="Peruntukan", required=False, )
    x_jenjang = fields.Char(string="Jenjang", required=False, )
    x_penulis = fields.Char(string="Penulis", required=False, )
    x_penerbit = fields.Char(string="Penerbit", required=False, )
    x_tahun_cetak = fields.Char(string="Tahun", required=False, )
    x_total_hal = fields.Integer(string="Total Hal", required=False, )
    x_ukuran = fields.Char(string="Ukuran", required=False, )
    x_warna = fields.Char(string="Warna", required=False, )
    x_bahan_cover = fields.Char(string="Cover", required=False, )
    x_kertas_isi = fields.Char(string="Kertas isi", required=False, )
    x_finishing = fields.Char(string="Finishing", required=False, )
    x_isbn = fields.Char(string="ISBN", required=False, )
    x_no_sk = fields.Char(string="No.SK", required=False, )
