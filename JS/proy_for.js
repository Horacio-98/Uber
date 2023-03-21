function incrementProy(start,P1) {
    results = [];
    P1 = true;
    i=0;  
  
    while (P1 == true) {
      i++;   
      num = (parseInt(start)).toString().padStart(4, '0');
      result = `PROY${num}`;
      results.push(result);
      return results[i-1];
    }  

}
  