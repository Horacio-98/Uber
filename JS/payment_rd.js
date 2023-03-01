function incrementRecord(start) {
    let result = '';
  
    for (let i = 1; i <= 10; i++) {
      let num = (parseInt(start) + i).toString().padStart(6, '0');
      result= (`SPA-${num}`);
      return result;
    }
  }
  