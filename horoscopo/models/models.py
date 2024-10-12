# -*- coding: utf-8 -*-
from odoo import models, fields, api

class horoscopo(models.Model):
    #heredamos este modelo res.partner
    _inherit = "res.partner"

    #añadimos tres campos
    #la edad NO SE ALMACENA EN LA BASE DE DATOS
    cumple = fields.Date("Fecha de nacimiento")
    edad = fields.Integer(string="Edad", readonly=True, compute="_calcula_edad", store=True)
    signo = fields.Char(string="Signo zodiaco", readonly=True, compute="_calcula_signo", store=True)

    #los metodos
    #puede que nos llegue mas de un registro por eso esta definido el bucle for
    #si cambia el atributo cumple
    @api.depends("cumple")
    def _calcula_edad(self):
            for registro in self:
                #si existe cumple le asigno 99 sino lo dejo a nulo
                if registro.cumple: 
                    #inserta aqui el codigo para calcular la edad
                    edad = 99
                    registro.edad = edad
    
    #si cambia el atributo cumple
    @api.depends("cumple")
    def _calcula_signo(self):
        try:
            #con esto ensure_one() estamos asegurandonos que en el self solo llega un registro
            self.ensure_one()
            #insertar aqui el codigo para calcular el signo del zodiaco
            self.signo = "Sin signo"
        except Exception:
             print("Varios registros en el dataset de _calcula_signo")
        
