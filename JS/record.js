function formatRecord(num) {
  formattedNum = num.toString().padStart(6, '0');
  resultado = "SPA-" + formattedNum;
  return resultado; 
}