function odoo_amount_text(instance,module){
    var QWeb = instance.web.qweb;
	var _t = instance.web._t;

    //Reemplazamos y agregamos la propiedad 'name' al model original para ver el nombre de la moneda ejmp: PEN
    module.PosModel.prototype.models.splice(12,1,{
        model: 'res.currency',
        fields: ['symbol','position','rounding','accuracy','name','rate_silent'],
        ids:    function(self){ return [self.pricelist.currency_id[0]]; },
        loaded: function(self, currencies){
            self.currency = currencies[0];
            if (self.currency.rounding > 0) {
                self.currency.decimals = Math.ceil(Math.log(1.0 / self.currency.rounding) / Math.log(10));
            } else {
                self.currency.decimals = 0;
            }
        },
    });

    //Extendemos el model Order para agregarle una nueva funcion amount_tex()
    module.Order = module.Order.extend({
        amount_text1: function(){
            var model_tex = new instance.web.Model("ir.translation");
            //console.log("ERROR1", this.pos.currency.name.toLowerCase().substring(0, 2) );
            model_tex.call('amount_to_text_pos',{'nbr':this.getTotalTaxIncluded(),'lang':this.pos.currency.name.toLowerCase().substring(0, 2),'currency':''}).then(function(monto2text){
                //console.log("ERROR1", monto2text );
                $('#montotext').html('SON: '+ monto2text);                          
            });        
        },
        amount_text2: function(){ // para INGLES

            var th = ['','thousand','million', 'billion','trillion'];            
            var dg = ['CERO','UNO','DOS', 'TRES','CUATRO','CINCO','SEIS','SIETE','OCHO','NUEVE'];
            var tn = ['DIEZ','ONCE','DOCE','TRECE','CATORCE','QUINCE','DIECISEIS','DIECISIETE','DIECIOCHO','DIECINUEVE',];
            var tw = ['VENTI','TREINTA','CUARENTA','CINCUENTA','SESENTA','SETENTA','OCHENTA','NOVENTA',];
            s = this.getTotalTaxIncluded();
            s = s.toString();
            s = s.replace(/[\, ]/g,''); 
            if (s != parseFloat(s)) return 'not a number'; 
            var x = s.indexOf('.'); 
            if (x == -1) x = s.length; 
            if (x > 15) return 'too big'; 
            var n = s.split(''); 
            var str = ''; 
            var sk = 0; 
            for (var i=0; i < x; i++) {
                if ((x-i)%3==2) {
                    if (n[i] == '1') {
                        str += tn[Number(n[i+1])] + ' '; 
                        i++; 
                        sk=1;
                    } 
                    else if (n[i]!=0) {
                        str += tw[n[i]-2] + ' ';
                        sk=1;
                    }
                } 
                else if (n[i]!=0) {
                        str += dg[n[i]] +' '; 
                        if ((x-i)%3==0) str += 'hundred ';
                        sk=1;
                } 
                if ((x-i)%3==1) {
                        if (sk) str += th[(x-i-1)/3] + ' ';
                        sk=0;
                    }
            } 
            if (x != s.length) {
                var y = s.length; 
                str += 'point '; 
                for (var i=x+1; i<y; i++) str += dg[n[i]] +' ';
            } 
            return str.replace(/\s+/g,' ');
        },
        amount_text: function () { // PARA ESPAÑOL
            var number_in = this.getTotalTaxIncluded();
            var converted = '' ;                            
            if (typeof(number_in) != 'string') {
                var number = number_in.toFixed(2);
            }
            else{                       
              var number = number_in;
            }
            var number_str = number ;                                    
            lista = number_str.split("."); //comprobamos si tiene decimal
            if (lista.length>1) {
                var number_int = lista[0]; // parte entera
                var number_dec = lista[1]; // parte decimal
            } 
            else {
                number_int = number_str;                              
                number_dec = "";
            }

            number_str = ('000000000' + number_int).slice(-9); // copletamos con 0 a la izquierda

            millones = number_str.substring(0,3); // extrae las tres primeros caracteres de la izquierda      
            //console.log("ERROR1", millones );
            miles = number_str.substring(3,6);       
            cientos = number_str.substring(6);

            if (parseInt(millones)>0) {
                if (millones == '001') {
                    converted += 'UN MILLON ';
                }
                else if (parseInt(millones) > 0) {    
                    converted +=  this.convertNumber(millones) + 'MILLONES ';
                }
            }

            if (parseInt(miles)>0) {                                                    
                if (miles == '001') {                                       
                    converted += 'MIL ';
                    }                                 
                else if (parseInt(miles) > 0) {                                     
                    converted += this.convertNumber(miles) + 'MIL ' ;
                }
            } 

            if (parseInt(cientos)>0) {                                                  
                if (cientos == '001') {                                     
                    converted += 'UN ';
                }                                   
                else if (parseInt(cientos) > 0) {                                   
                    converted += this.convertNumber(cientos) + ' ' ;
                }
            }

            if (number_dec == "") {
                number_dec = "00";
            }

            if (number_dec.length < 2 ){
              number_dec+='0';
            }

            converted += 'LEMPIRAS' + ' CON ' + number_dec + "/100 "; 
            
            return converted ;          
            //return this.convertNumber('856');
        },
        convertNumber: function (n){
            var UNIDADES = ['','UNO ','DOS ','TRES ','CUATRO ','CINCO ','SEIS ','SIETE ','OCHO ','NUEVE ','DIEZ ', 'ONCE ','DOCE ','TRECE ','CATORCE ','QUINCE ','DIECISEIS ','DIECISIETE ','DIECIOCHO ','DIECINUEVE ','VEINTE '];
            var DECENAS = ['VENTI','TREINTA ','CUARENTA ','CINCUENTA ','SESENTA ','SETENTA ','OCHENTA ','NOVENTA ','CIEN '];
            var CENTENAS = ['CIENTO ','DOSCIENTOS ','TRESCIENTOS ','CUATROCIENTOS ', 'QUINIENTOS ','SEISCIENTOS ','SETECIENTOS ','OCHOCIENTOS ','NOVECIENTOS '];
            var output = '';
            if(n == '100'){
                output = "CIEN ";
            }
            else if (n[0] != '0') {
                output = CENTENAS[parseInt(n[0])-1];
            }
            var k = parseInt(n.substring(1));
            if (k <= 20) {
                output += UNIDADES[k];
            }
            else {
                if((k > 30) & (n[2] != '0')){
                    //output += '%sY %s' % (DECENAS[parseInt(n[1])-2], UNIDADES[parseInt(n[2])]);
                    output += DECENAS[parseInt(n[1])-2] + 'Y ' + UNIDADES[parseInt(n[2])];
                }
                else {
                    //output += '%s%s' % (DECENAS[parseInt(n[1])-2], UNIDADES[parseInt(n[2])]);
                    output += DECENAS[parseInt(n[1])-2] + UNIDADES[parseInt(n[2])];
                }
            }
            return output;
        },
    });


}



