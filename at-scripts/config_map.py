configMap = {
    "./Banamex 2015/Banamex 2015.xls.bnx oro-2636.csv" : {
        'delimiter' : ',',
        'colum_names' : ['No. De Tarjeta', 'Nombre Cliente', 'Domicilio del cliente', 'C.P.', 'Particular', 'Oficina','RFC'],
        'entities' : [
            {
                "@type" : "Person",
                "name" : ["Nombre Cliente"]
            },
            {
                "@type" : "CreditCard",
                "name" : ["No. De Tarjeta"]                                       
            },
            {
                "@type" : "PostalAddress",
                "name" : ['Domicilio del cliente','C.P.'],
                "postalCode": ['C.P.'],
                "streetAddress": ['Domicilio del cliente']
            }
        ]
    },
    "./Banamex 2015/Banamex 2015.xls.Hoja2.csv" :{
        'delimiter' : ',',
        'colum_names' : ['TDC','Nombre','Direccion','Colonia','Entidad','RFC','Casa','Oficina','CP'],
        'entities' : [
            {
                "@type" : "Person",
                "name" : ['Nombre']
            },
            {
                "@type" : "PostalAddress",
                "name" : ['Direccion','CP', 'Entidad','Colonia'],
                "postalCode": ['CP'],
                "streetAddress": ['Direccion'],
                "addressRegion" : ['Entidad'],
                "addressLocality" : ['Colonia']
            }
        ]
    },
    "./Banamex 2015/Banamex 2015.xls.bnx 2125.csv" :{
        'delimiter' : ',',
        'colum_names' : ['ID Folio','RFC','Folio','Tarjeta Premia','fcctenombre','fccteapaterno','fccteamaterno','estado','fcctelada','fcctetel','lada ofna','tel ofna','extension','fccteemail','anio_nac','mes_nac','dia_nac'],
        'entities' : [
            {
                "@type" : "Person",
                "name" : ['fcctenombre','fccteapaterno','fccteamaterno'],
                "firstName" : ['fcctenombre'],
                "lastName1" : ['fccteapaterno'],
                "lastName2" : ['fccteamaterno']
            },
            {
                "@type" : "CreditCard",
                "name" : ['Tarjeta Premia']
            }
        ]
    },
    "./Banamex 2015/Banamex 2015.xls.Hoja1.csv" :{
        'delimiter' : ',',
        'colum_names' : ['nombre','apaterno','amaterno','Fec_Nac','tel_casa','tel_oficina','Empresa','Puesto','Domemp','NEEmp','NIEmp','ColEMP','DoMEmp2','EdpEmp','CPEmp','Tel_Oficina2','Ext','Ant_Años','Ant_Mes','Ing_Fijo','Tdc1Num','Tdc1Bco','OtrosBco','RNom','RApe','RTEL','Rext'],
        'entities' : [
            {
                "@type" : "Person",
                "name" : ['nombre','apaterno','amaterno'],
                "firstName" : ['nombre'],
                "lastName1" : ['apaterno'],
                "lastName2" : ['amaterno']
            },
            {
                "@type" : "Person",
                "name" : ['RNom','RApe'],
                "firstName" : ['nombre'],
                "lastName1" : ['RApe']
            },
            {
                "@type" : "Organization",
                "name" : ['Empresa'] 
            },
            {
                "@type" : "Organization",
                "name" : ['Tdc1Bco'] 
            },
            {
                "@type" : "PostalAddress",
                "name" : ['Domemp','NEEmp','NIEmp','ColEMP','DoMEmp2','EdpEmp','CPEmp'],
                "postalCode": ['CPEmp'],
                "streetAddress": ['Domemp'],
                "addressRegion" : ['EdpEmp'],
                "addressLocality" : ['ColEMP']
            }
        ]
    },
    "./Banamex 2015/Banamex 2015.xls.bnx clasica-800.csv" :{
        'delimiter' : ',',
        'colum_names' : ['ID Folio','RFC','Folio','Tarjeta Premia','fcctenombre','fccteapaterno','fccteamaterno','estado','fcctelada','fcctetel','lada','ofna','tel','ofna','extension','fccteemail','anio_nac','mes_nac','dia_nac'],
        'entities' : [
            {
                "@type" : "Person",
                "name" : ['fcctenombre','fccteapaterno','fccteamaterno'],
                "firstName" : ['fcctenombre'],
                "lastName1" : ['fccteapaterno'],
                "lastName2" : ['fccteamaterno']
            },
            {
                "@type" : "CreditCard",
                "name" : ['Tarjeta Premia']
            }
        ]
    },
    "./Bancomer 2017/BANCOMER-Clientes.mdb.b'BD_FINAL'.csv" :{
        'delimiter' : ';',
        'colum_names' : ['NOMBRE_COMPLETO','NOMBRES','APATERNO','AMATERNO','CALLE','COLONIA','CIUDAD','ESTADO','COD_POSTAL','TELEFONO1','TELEFONO2','INGRESOS','CVE_SEXO','RFC','NIVEL_ECONIMOC','BANCO'],
        'entities' : [
            {
                "@type" : "Person",
                "name" : ['NOMBRES','APATERNO','AMATERNO'],
                "firstName" : ['NOMBRES'],
                "lastName1" : ['APATERNO'],
                "lastName2" : ['AMATERNO']
            },
            {
                "@type" : "PostalAddress",
                "name" : ['CALLE','COLONIA','CIUDAD','ESTADO','COD_POSTAL'],
                "postalCode": ['COD_POSTAL'],
                "streetAddress": ['CALLE'],
                "addressRegion" : ['COLONIA'],
                "addressLocality" : ['CIUDAD'],
                "addressState" : ['ESTADO']
            }
        ]
    },
    "./Ife 2015/BCS.accdb.b'BCS'.csv" :{
        'delimiter' : ';',
        'colum_names' : ['cve','nombre','paterno','materno','e','d','mpo','secc','loc','mza','guion','colonia','cp','calle','ext','int','edad','sexo','guion2','ln','credencial'],
        'entities' : [
            {
                "@type" : "Person",
                "name" : ['nombre','paterno','materno'],
                "firstName" : ['nombre'],
                "lastName1" : ['paterno'],
                "lastName2" : ['materno']
            },
            {
                "@type" : "PostalAddress",
                "name" : ['mpo','secc','loc','mza','guion','colonia','cp','calle','ext'],
                "postalCode": ['cp'],
                "streetAddress": ['calle'],
                "addressRegion" : ['colonia'],
                "addressLocality" : ['loc'],
                "addressState" : ['mpo']
            },
            {
                "@type" : "Ife",
                "name" : ['cve']
            }
        ]
    },
    "./Santander/Tarjetas-Credito_Santander.xls.Sheet1.csv" :{
        'delimiter' : ',',
        'colum_names' : ['NombreCompleto','Direccion','Colonia','Ciudad','InicialesEstado','Numero1','Tarjeta','Numero2','Numero3','Numero4','Visible'],
        'entities' : [
            {
                "@type" : "Person",
                "name" : ['NombreCompleto']
            },
            {
                "@type" : "CreditCard",
                "name" : ['Tarjeta']
            },
            {
                "@type" : "PostalAddress",
                "name" : ['Direccion','Colonia','Ciudad','InicialesEstado'],
                "streetAddress": ['Direccion'],
                "addressRegion" : ['Colonia'],
                "addressLocality" : ['Ciudad'],
                "addressState" : ['InicialesEstado']
            }
        ]
    },
    "./Telmex 2012/Aguascalientes 32.900.xls.Aguascalientes.csv" :{
        'delimiter' : ',',
        'colum_names' : ['ID','TELEFONO','TIPO_DIREC','CVE_SERV','PATERNO','MATERNO','NOMBRE','DOMICILIO','CP','COLONIA','CIUDAD','MUNICIPIO','ENTIDAD','NIVEL'],
        'entities' : [
            {
                "@type" : "Person",
                "name" : ['NOMBRE','PATERNO','MATERNO'],
                "firstName" : ['NOMBRE'],
                "lastName1" : ['PATERNO'],
                "lastName2" : ['MATERNO']
            },
            {
                "@type" : "PostalAddress",
                "name" : ['DOMICILIO','CP','COLONIA','CIUDAD','MUNICIPIO','ENTIDAD'],
                "postalCode": ['CP'],
                "streetAddress": ['DOMICILIO'],
                "addressRegion" : ['COLONIA'],
                "addressLocality" : ['CIUDAD'],
                "addressState" : ['MUNICIPIO']
            },
            {
                "@type" : "Telephone",
                "name" : ['TELEFONO']
            }
        ]
    }
}
