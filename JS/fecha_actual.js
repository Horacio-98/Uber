function convertDate() {
    const now = new Date();
    const year = now.getUTCFullYear();
    const month = (now.getUTCMonth() + 1).toString().padStart(2, '0');
    const day = now.getUTCDate().toString().padStart(2, '0');
    const hour = now.getUTCHours().toString().padStart(2, '0');
    const minute = now.getUTCMinutes().toString().padStart(2, '0');
    const second = now.getUTCSeconds().toString().padStart(2, '0');
  
    const isoFecha = year+"-"+month+"-"+day+"T"+hour+":"+minute+":"+second+"Z";
    var fecha_actual = isoFecha; 
    return fecha_actual;
  }

