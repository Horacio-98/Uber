function getTipo(code) {
    const tipos = {
      100: "CLIENTES",
      101: "PROVEEDORES",
      102: "CXC CLIENTES",
      103: "CREDITO",
      104: "PAGOS RECURRENTES",
      105: "ESPORADICOS",
      106: "CXC VARIAS",
      107: "CXC EMLPEADOS",
      108: "PRESUPUESTOS",
      109: "CONTRATISTA",
      110: "COLABORADOR",
      111: "COLABORADORES",
      112: "TARJETAS DE CREDITO",
      113: "BONO DE REFERIDOS"
    };
    
    salida = tipos[code] 
    return salida;
  }