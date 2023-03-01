function incrementProy(start) {
  let result = '';

  for (let i = 1; i <= 10; i++) {
    let num = (parseInt(start) + i).toString().padStart(4, '0');
    result= (`PROY${num}`);
    return result;
  }
}



