function incrementProy(start) {
    let proyect = '';
    let record = ''; 
  
    for (let i = 1; i <= 10; i++) {
      for (let i = 1; i <= 10; i++) {

        let num = (parseInt(start) + i).toString().padStart(4, '0');
        proyect= (`PROY${num}`);

        let numero = (parseInt(start) + i).toString().padStart(6, '0');
        record= (`SPA-${numero}`);

        return record;
      }
    }
  }
  
  